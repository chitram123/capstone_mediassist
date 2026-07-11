import os
import pandas as pd
from datetime import datetime

LOG_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "usage_logs.csv"
    )
)


def log_chat(
    question,
    source,
    executed_agent,
    response_time
):

    row = {

        "Timestamp": datetime.now(),

        "Question": question,

        "Source": source,

        "Executed_Agent": executed_agent,

        "Response_Time": response_time

    }

    if os.path.exists(LOG_FILE):

        df = pd.read_csv(LOG_FILE)

    else:

        df = pd.DataFrame()

    df = pd.concat(
        [
            df,
            pd.DataFrame([row])
        ],
        ignore_index=True
    )

    df.to_csv(
        LOG_FILE,
        index=False
    )