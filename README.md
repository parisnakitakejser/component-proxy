# component-proxy
Get proxy container for to support all my project with microservice containers in docker, this proxy can control the traffic between each service, and you can disabled the services you did not want to use.

**🌟 Community 🌟**

- Subscribe my channel: https://www.youtube.com/c/ParisNakitaKejser?sub_confirmation=1
- Private website: https://www.pnk.sh
- Discord: https://discord.gg/6tcWjxV
- Donate: https://www.patreon.com/parisnakitakejser

**Component projects**

- Authentication: https://github.com/parisnakitakejser/component-authentication
- Logging: https://github.com/parisnakitakejser/component-logging

**System environments to set**

| Environment vars              | Required | Fallback           |
| ----------------------------- | -------- | ------------------ |
| COMPONENT_AUTH_ENABLED        | No       | None               |
| COMPONENT_LOGGING_ENABLED     | No       | None               |

**Build new images**

If you found eny bugs and want to build your own images, you can do it very quickly by using this command

docker build -t component-proxy:{version} . --no-cache