import os
from pydantic import BaseModel

class AppConfig(BaseModel):
    broker_name: str = "Quotex"
    api_url: str = "https://api1.api.cbtraderbd.xyz/docs"
    direct_contact: str = "https://t.me/YouKnowWho_am"
    telegram_channel: str = "https://t.me/+R_kEsY9yqkA1NDI1"
    demo_bot: str = "https://t.me/cbsignalsproai_bot?start=1"
    account_verify_bot: str = "https://t.me/cbtradersbd_bot?start=1"

config = AppConfig()
