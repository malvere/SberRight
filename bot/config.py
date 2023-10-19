import logging
from dataclasses import dataclass
from os import getenv


@dataclass
class BotConfig:
    token: str = getenv("BOT_TOKEN")

@dataclass
class Webhook():
    project_name: str = getenv("PROJECT_NAME")
    webhook_host: str = f"https://{project_name}.onrender.com"
    webhook_url_path: str = "/webhook"
    webhook_url: str = f"{webhook_host}{webhook_url_path}"
    

@dataclass
class Webapp():
    web_app_host: str = getenv("localhost")
    web_app_port: int = getenv("PORT")
    

@dataclass
class Config:
        
    logging_level = int(getenv("LOGGING_LEVEL", logging.INFO))

    bot = BotConfig()
    webhook = Webhook()
    web_app = Webapp()



conf = Config()