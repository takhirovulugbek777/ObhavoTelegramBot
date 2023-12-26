# Telegram Weather Bot

This Telegram bot provides weather information for cities using the Yahoo Weather API.

## Prerequisites

Before running this bot, make sure you have Python installed on your machine.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain API keys:

    - You'll need a Telegram Bot API token and a RapidAPI key for the Yahoo Weather API.
    - Place the Telegram Bot token in `main.py` (`token = "Telegram bot token"`) and the RapidAPI key in `api.py` (`"X-RapidAPI-Key": "RapiApiToken"`).

## Usage

Run the bot using the following command:

```bash
python main.py
