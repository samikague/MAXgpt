import asyncio
import logging

from bot.bot import run

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    asyncio.run(run())