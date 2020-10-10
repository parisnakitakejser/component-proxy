import os
import nginx
from dotenv import load_dotenv

load_dotenv()

components = [{
    'env': 'COMPONENT_AUTH_ENABLED',
    'upstream': 'component_authentication',
    'path': 'auth'
}, {
    'env': 'COMPONENT_LOGGING_ENABLED',
    'upstream': 'component_logging',
    'path': 'logging'
}]


def setup_components(all_components: list):
    for component in all_components:
        host = component['upstream']
        server = host.replace('_', '-')
        name = host.split('_')[1]
        path = component['path']

        if os.getenv(component['env']) == '1':
            # setup upstream config
            c = nginx.Conf()
            u = nginx.Upstream(host,
               nginx.Key('server', f'{server}:5000')
            )
            c.add(u)
            nginx.dumpf(c, f'upstreams/{name}.conf')

            # setup enabled location config
            c = nginx.Conf()
            l = nginx.Location(f'~* ^/{path}/',
               nginx.Key('rewrite', f'^/{path}/(.*) /$1 break'),
               nginx.Key('proxy_set_header', 'Host $host'),
               nginx.Key('proxy_set_header', 'X-Real-IP $remote_addr'),
               nginx.Key('proxy_pass', f'http://{host}'),
               nginx.Key('proxy_pass_request_headers', 'on'),
            )
            c.add(l)
            nginx.dumpf(c, f'locations/{name}.conf')
        else:
            # setup disabled location config
            c = nginx.Conf()
            l = nginx.Location(f'~* ^/{path}/',
               nginx.Key('return', '503'),
           )
            c.add(l)
            nginx.dumpf(c, f'locations/{name}.conf')


setup_components(all_components=components)
