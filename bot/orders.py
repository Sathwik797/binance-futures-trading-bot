"""
Order management module for placing MARKET and LIMIT orders
on Binance Futures Testnet.
"""

from binance.exceptions import BinanceAPIException

from bot.client import BinanceClient
from bot.logging_config import logger


class OrderManager:
    """
    Handles MARKET and LIMIT order placement
    on Binance Futures Testnet.
    """

    def __init__(self) -> None:
        """
        Initialize the Binance client.
        """
        self.client = BinanceClient().get_client()

    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float
    ) -> dict:
        """
        Place a MARKET order.

        Args:
            symbol: Trading pair (e.g. BTCUSDT)
            side: BUY or SELL
            quantity: Order quantity

        Returns:
            Binance order response.
        """

        try:
            logger.info(
                f"MARKET ORDER | Symbol={symbol}, Side={side}, Quantity={quantity}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"MARKET ORDER RESPONSE | {order}")

            return order

        except BinanceAPIException:
            logger.exception("Binance API error while placing MARKET order.")
            raise

        except Exception:
            logger.exception("Unexpected error while placing MARKET order.")
            raise

    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float
    ) -> dict:
        """
        Place a LIMIT order.

        Args:
            symbol: Trading pair (e.g. BTCUSDT)
            side: BUY or SELL
            quantity: Order quantity
            price: Limit price

        Returns:
            Binance order response.
        """

        try:
            logger.info(
                f"LIMIT ORDER | Symbol={symbol}, Side={side}, "
                f"Quantity={quantity}, Price={price}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"LIMIT ORDER RESPONSE | {order}")

            return order

        except BinanceAPIException:
            logger.exception("Binance API error while placing LIMIT order.")
            raise

        except Exception:
            logger.exception("Unexpected error while placing LIMIT order.")
            raise