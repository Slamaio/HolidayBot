# ⚠️ Repository Archived  

This repository has been archived because it is no longer maintained. The bot relied on data from an external website, which is no longer accessible. As a result, the functionality of HolidaysBot has been rendered obsolete.  

If you are looking for an alternative solution, consider checking other APIs or resources that provide holiday data.  

Thank you to everyone who used and contributed to this project!  

---

# HolidaysBot
Telegram bot that shows current holidays

## Environment variables:
- `TOKEN`: Bot API token from botfather
- `LOGGING_LEVEL`: logging level (optional), default - `info`

## Deploy

### Create deployment package
- Clone this repository: `git clone https://github.com/Slamaio/HolidaysBot.git`
- Run create-package bash script: `./create-package.sh`

### Create and configure API Gateway entrypoint
- Create and configure API Gateway entrypoint;
- Set webhook for your bot: follow the link through your browser or using curl – `https://api.telegram.org/bot{your_bot_api_token}/setWebhook?url={your_api_gateway_url}`
