import logging
import os
from datetime import datetime

# ----------------------------
# Create logs folder
# ----------------------------

LOG_DIR = os.path.join(
    os.path.dirname(__file__),
    "logs"
)

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

# ----------------------------
# Daily log filename
# ----------------------------

today = datetime.now().strftime("%Y-%m-%d")

LOG_FILE = os.path.join(
    LOG_DIR,
    f"mediassist_{today}.log"
)

# ----------------------------
# Logger Configuration
# ----------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("MediAssistAI")