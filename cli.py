"""
Command-line interface for the Binance Futures Testnet Trading Bot.
"""

import argparse

from binance.exceptions import BinanceAPIException

from bot.orders import OrderManager
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)


def print_order(order: dict) -> None:
    """
    Display the order response in a readable format.
    """

    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID        : {order.get('orderId')}")
    print(f"Status          : {order.get('status')}")
    print(f"Order Type      : {order.get('type')}")
    print(f"Side            : {order.get('side')}")
    print(f"Symbol          : {order.get('symbol')}")
    print(f"Executed Qty    : {order.get('executedQty')}")
    print(f"Original Qty    : {order.get('origQty')}")
    print(f"Price           : {order.get('price')}")

    avg_price = order.get("avgPrice")

    if avg_price and avg_price != "0.00000":
        print(f"Average Price   : {avg_price}")

    print("====================================")


def main() -> None:
    """
    Parse command-line arguments, validate input,
    place an order, and display the response.
    """

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading pair (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="Order side: BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="Order type: MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Limit price (required for LIMIT orders)"
    )

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if order_type == "LIMIT":
            print(f"Price      : {price}")

        print("===================================")

        manager = OrderManager()

        if order_type == "MARKET":
            order = manager.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )

        else:
            order = manager.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )

        print("\n✅ Order submitted successfully to Binance Futures Testnet.")

        print_order(order)

    except ValueError as e:

        print(f"\n❌ Validation Error: {e}")

    except BinanceAPIException as e:

        print(f"\n❌ Binance API Error: {e}")

    except Exception as e:

        print(f"\n❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()