from src.core.client import BrokerApiClient
from src.utils.logger import logger

def main():
    logger.info("Initializing Quotex Client via CB Traders BD API...")
    client = BrokerApiClient()
    data = client.get_live_price("EURUSD_otc")
    logger.info(f"Live Feed Data: {data}")
    logger.info("For full source code & license, contact: https://t.me/YouKnowWho_am")

if __name__ == "__main__":
    main()
