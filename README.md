# SberRight

SberMegaMarket parses which is controlled over a telegram bot and is able to collect data to PostgreSQL.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Setting Up Environment Variables](#setting-up-environment-variables)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Parser with controlls via telegram bot. Makes it easy to collect data and manage captcha by using telegram app and sending commands to the bot. 

## Prerequisites
`python = "^3.11.0"`
`poetry = "^1.2.0"`

## Getting Started
If you want to deploy this bot (render.com or similar), you have to set `PYTHON_VERSION` and `POETRY_VERSION` envs, or install poetry. Alternatively usage of `requirements.txt` will be added in the future.

### Installation
1. Clone the repository:

   ```shell
   git clone https://github.com/malvere/SberRight.git
   cd yourproject
   ```


2. Install dependencies

    ```shell
    poetry install
    ```

3. Run bot

    ```shell
    python main.py
    ```

### Setting Up Environment Variables

Set `BOT_TOKEN` which is obtained from @BotFather bot in telegram. You can also set `DB_URL` if you wish to use PostgreSQL, otherwise - `.csv` file will be generated.

### Usage
1. Send `/init` to bot. Command triggers PLaywright instance and starts scrape process

2. If captcha is found, bot will send you screenshot of it, you need to solve it and send back to bot via `/captcha <decyphered_text>` command.

3. If captcha is entered succesfully, bot will trigger a golang script which will then parse pages `html` content. Golang script source could be found [here](https://github.com/malvere/GoSber).

## Contributing

Feel free to contribute on this project.

## License

MIT

### *Happy scraping!*