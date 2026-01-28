from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    WEBHOOK_SECRET: str = os.getenv("WEBHOOK_SECRET")

    def __init__(self):
        if not self.DATABASE_URL:
            raise RuntimeError("DATABASE_URL not set")
        if not self.WEBHOOK_SECRET:
            raise RuntimeError("WEBHOOK_SECRET not set")

settings = Settings()
