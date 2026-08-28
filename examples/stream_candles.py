import time
from src.core.client import BrokerApiClient
from src.utils.logger import logger

def stream():
    client = BrokerApiClient()
    logger.info("Streaming 24/7 OTC candles for Quotex...")
    for _ in range(3):
        feed = client.get_live_price()
        logger.info(f"Tick received: {feed}")
        time.sleep(1)

if __name__ == "__main__":
    stream()
