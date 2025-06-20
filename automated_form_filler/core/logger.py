import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_success(msg):
    logging.info(f"✅ {msg}")

def log_error(msg):
    logging.error(f"❌ {msg}")
