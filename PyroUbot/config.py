import os
#Jangan Di hapus kontol, kalo mah tambahin aja memek
DEVS = [
    943015049,
]

API_ID = int(os.getenv("API_ID", "29320516"))

API_HASH = os.getenv("API_HASH", "bcc68b59eb17c36b951965de3247a59d")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6629903582:AAHMbinTvDkOLFHdBbk1LuL2-2qM09yAjUs")

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

