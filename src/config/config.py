import logging
import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class BotConfig:
    api_token: str


@dataclass
class DbConfig:
    host: str
    port: str
    username: str
    password: str
    database: str


@dataclass
class Config:
    bot: BotConfig
    database: DbConfig


def load_config() -> Config:
    load_dotenv()

    api_token: str = os.getenv("API_TOKEN")

    db_host: str = os.getenv("DB_HOST")
    db_port: str = os.getenv("DB_PORT")
    db_username: str = os.getenv("DB_USERNAME")
    db_password: str = os.getenv("DB_PASSWORD")
    db_database: str = os.getenv("DB_DATABASE")

    return Config(
        bot=BotConfig(api_token=api_token),
        database=DbConfig(
            host=db_host,
            port=db_port,
            username=db_username,
            password=db_password,
            database=db_database
        )
    )
