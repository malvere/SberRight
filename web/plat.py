import os
import platform

from bot.config import BotConfig, Webapp, Webhook


def whoami():
    current_platform = platform.system()

    if current_platform == "Windows":
        # Code to run on a local Windows machine
        print("Running on a local Windows machine.")
    elif current_platform == "Linux":
        # Code to run on a Linux server
        print("Running on a Linux server.")
        return "parsers/sber-scrape-linux-amd64"
    else:
        # Code to run on an unknown platform (you can add more cases as needed)
        print(f"Running on an unknown platform: {current_platform}")
        
        return "parsers/sber-scrape"

def is_docker() -> bool:
    current_platform = platform.system()
    if current_platform == "Linux":
        print(f"Webhook URL: {Webhook.webhook_url}\n Webapp port: {Webapp.web_app_port}\nBot token: {BotConfig.token}")
        return True
    else:
        print(f"Running locally: {current_platform}")
        return False