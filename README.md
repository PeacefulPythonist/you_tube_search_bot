# YouTube Search Bot

## Overview

This project is a Telegram bot deployed on AWS Lambda that facilitates YouTube searches and provides users with relevant video links. The bot allows users to search for videos, retrieve links from playlists, and obtain all videos from a channel.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [How to Use](#how-to-use)
4. [Dependencies](#dependencies)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Deployment](#deployment)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

This project aims to provide a convenient way for users to search YouTube and obtain video links directly through a Telegram bot. The project is deployed on AWS Lambda, making it scalable and easily accessible.

## Project Structure

- **api_keys.py:** Contains API keys and constants used in the project.
- **consts.py:** Stores various constants and configuration settings.
- **base_lambda.py:** Provides essential functions for working with AWS Lambda.
- **tgbot.py:** Contains functions for interacting with the Telegram bot.
- **yt_search.py:** Includes functions for searching YouTube and retrieving video links.
- **main.py:** AWS Lambda handler for processing incoming messages and providing YouTube links.

## How to Use

Users interact with the bot through Telegram. They can send messages containing search queries, playlist links, or channel links to receive relevant video links.

## Dependencies

- **youtubesearchpython:** Library for searching YouTube.
- **requests:** Library for making HTTP requests.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/YouTube-Search-Bot.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

- **api_keys.py:** Update API keys and constants.
- **consts.py:** Adjust configuration settings.
- **main.py:** Customize the main AWS Lambda handler if needed.

## Deployment

1. Deploy the code on AWS Lambda.
2. Set up the Telegram bot and obtain API keys.
3. Configure the bot by updating API keys and constants.
4. Test the bot on Telegram.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
