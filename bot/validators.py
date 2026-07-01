"""
Validation functions for user input.
"""

VALID_SIDES = ("BUY", "SELL")
VALID_ORDER_TYPES = ("MARKET", "LIMIT")


def validate_symbol(symbol: str) -> str:
    """
    Validate the trading symbol.

    Args:
        symbol: Trading pair (e.g. BTCUSDT)

    Returns:
        Uppercase trading symbol.

    Raises:
        ValueError: If the symbol is empty.
    """
    if not symbol.strip():
        raise ValueError("Symbol cannot be empty.")

    return symbol.upper()


def validate_side(side: str) -> str:
    """
    Validate order side.

    Args:
        side: BUY or SELL

    Returns:
        Uppercase order side.

    Raises:
        ValueError: If the side is invalid.
    """
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate order type.

    Args:
        order_type: MARKET or LIMIT

    Returns:
        Uppercase order type.

    Raises:
        ValueError: If the order type is invalid.
    """
    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate order quantity.

    Args:
        quantity: Order quantity.

    Returns:
        Validated quantity.

    Raises:
        ValueError: If quantity is less than or equal to zero.
    """
    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return quantity


def validate_price(price: float | None, order_type: str) -> float | None:
    """
    Validate limit order price.

    Args:
        price: Order price.
        order_type: MARKET or LIMIT.

    Returns:
        Validated price or None for MARKET orders.

    Raises:
        ValueError: If LIMIT order price is missing or invalid.
    """
    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValueError("Price is required for LIMIT orders.")

        price = float(price)

        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        return price

    return None