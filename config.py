from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("21816509"))
API_HASH = getenv("82f9a4ab5502f79c213d16300d2a5aa7")

BOT_TOKEN = getenv("7630834160:AAHSc6v_w80Dx3PmjbrCX6Nkf8NGi013NPI", None)
DURATION_LIMIT = int(getenv("90", "90"))

OWNER_ID = int(getenv("8163557664"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("None", None)

SUPPORT_CHAT = getenv("https://t.me/Abar_Phire_Chol"),
SUPPORT_CHANNEL = getenv("https://t.me/abar_phire_cholll"),

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
