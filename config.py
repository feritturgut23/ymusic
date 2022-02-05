import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Talia Müzik Projesi")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/0f6f8a8a5ad69fe5ecf3d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/a4fa687ed647cfef52402.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/a4fa687ed647cfef52402.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/a4fa687ed647cfef52402.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "Mp3dinleme_Bot ")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SesMusicAsistan")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Sohbetdestek")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EfsaneMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "Mahoaga") # kullanıcı adınızı semboller olmadan doldurma @
DEV_NAME = getenv("DEV_NAME", "mahoaga")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
