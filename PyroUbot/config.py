import os
#Jangan Di hapus kontol, kalo mah tambahin aja memek
DEVS = [
    943015049,
]

API_ID = int(os.getenv("API_ID", "21508927"))

API_HASH = os.getenv("API_HASH", "b0a8dab063f3679621e10b64eb91c267")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6880487359:AAFLg_RvYMymP9XnT6FPkiYNRNxxHRxbvLY")

OWNER_ID = int(os.getenv("OWNER_ID",  "5366895595"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4132105015"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001994800407").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
)

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://zyric:1234@cluster0.bophvmo.mongodb.net/?retryWrites=true&w=majority",
)

