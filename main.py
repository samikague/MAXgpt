import asyncio
import logging

from bot.initialize import run

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # TODO: Перенести на loguru

if __name__ == "__main__":
    asyncio.run(run())