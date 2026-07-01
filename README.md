# Binance Futures Testnet Trading Bot

A command-line Python application that places **MARKET** and **LIMIT** orders on the **Binance USDT-M Futures Testnet**. The project follows a modular architecture with separate layers for API communication, validation, logging, and CLI interaction.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Support for both **BUY** and **SELL** orders
- Command Line Interface (CLI) using `argparse`
- User input validation
- Logging of API requests, responses, and errors
- Exception handling for invalid input and Binance API errors
- Secure API credential management using `.env`

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py            # Binance client wrapper
│   ├── orders.py            # Order placement logic
│   ├── validators.py        # Input validation
│   └── logging_config.py    # Logging configuration
│
├── tests/
│   ├── __init__.py
│   ├── test_client.py
│   ├── test_market_order.py
│   └── test_validators.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── .gitignore
├── .env                     # Not included in repository
└── README.md
```

---

## Requirements

- Python 3.10 or later
- Binance Futures Testnet Account
- Binance Testnet API Key and Secret Key

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd trading_bot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
SECRET_KEY=YOUR_BINANCE_TESTNET_SECRET_KEY
```

> **Note:** Never commit your `.env` file or API credentials to GitHub.

---

## Usage

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example Output

```text
========== ORDER REQUEST ==========
Symbol     : BTCUSDT
Side       : BUY
Type       : MARKET
Quantity   : 0.001
===================================

✅ Order submitted successfully to Binance Futures Testnet.

========== ORDER RESPONSE ==========
Order ID        : 18163728069
Status          : NEW
Order Type      : MARKET
Side            : BUY
Symbol          : BTCUSDT
Executed Qty    : 0.0000
Original Qty    : 0.0010
Price           : 0.00
====================================
```

---

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

Example Output

```text
========== ORDER REQUEST ==========
Symbol     : BTCUSDT
Side       : SELL
Type       : LIMIT
Quantity   : 0.001
Price      : 200000
===================================

✅ Order submitted successfully to Binance Futures Testnet.

========== ORDER RESPONSE ==========
Order ID        : 18163962198
Status          : NEW
Order Type      : LIMIT
Side            : SELL
Symbol          : BTCUSDT
Executed Qty    : 0.0000
Original Qty    : 0.0010
Price           : 200000.00
====================================
```

---

## Logging

The application logs:

- API connection status
- Order requests
- Order responses
- Errors and exceptions

Log file location:

```text
logs/trading.log
```

---

## Input Validation

The application validates:

- Trading symbol
- Order side (`BUY` / `SELL`)
- Order type (`MARKET` / `LIMIT`)
- Quantity greater than zero
- Price for LIMIT orders

---

## Error Handling

The application handles:

- Invalid user input
- Missing API credentials
- Binance API exceptions
- Unexpected runtime errors

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging

---

## Assumptions

- Binance Futures Testnet account is active.
- Valid API credentials are stored in the `.env` file.
- Internet connection is available.
- Orders are placed on the Binance Futures Testnet only.

---

## Future Improvements

- Support for additional order types (Stop-Limit, OCO, TWAP)
- Interactive CLI using Typer or Click
- Order cancellation functionality
- Position management
- Unit tests with pytest
- Lightweight web interface

---

## Author

**Obilipapannagari Sathwik Reddy**

Built as part of a Python Developer internship assignment using the Binance Futures Testnet.