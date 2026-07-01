import os

from binance.client import Client
from dotenv import load_dotenv

from bot.logging_config import logger

load_dotenv()


class BinanceClient:
    """
    Creates and manages a Binance Futures Testnet client.
    """

    def __init__(self) -> None:

        api_key = os.getenv("API_KEY")
        secret_key = os.getenv("SECRET_KEY")

        if not api_key or not secret_key:
            logger.error("API credentials not found.")
            raise ValueError(
                "API_KEY or SECRET_KEY not found in .env file."
            )

        try:

            self.client = Client(
                api_key,
                secret_key,
                testnet=True
            )

            logger.info("Connected to Binance Futures Testnet.")

        except Exception:

            logger.exception(
                "Failed to connect to Binance Futures Testnet."
            )

            raise

    def get_client(self) -> Client:
        """
        Return the Binance client instance.
        """
        return self.client