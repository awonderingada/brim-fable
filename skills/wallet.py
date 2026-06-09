"""fable's money. solana wallet, hard spend cap, no exceptions.

stub for now — balance checks land first, sending later. the cap in .env
is enforced here, not in the prompt. the model never gets to argue with it.
"""

import os

from dotenv import load_dotenv

load_dotenv()

SPEND_CAP_USD = float(os.getenv("WALLET_SPEND_CAP_USD", "10"))


def can_spend(amount_usd: float) -> bool:
    return amount_usd <= SPEND_CAP_USD


def balance() -> float:
    raise NotImplementedError("wallet not connected yet")
