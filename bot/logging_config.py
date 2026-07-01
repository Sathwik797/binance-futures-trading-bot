"""
Logging configuration for the trading bot.
"""

import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

if not logging.getLogger().handlers:
    logging.basicConfig(
        filename="logs/trading.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
    )

logger = logging.getLogger(__name__)