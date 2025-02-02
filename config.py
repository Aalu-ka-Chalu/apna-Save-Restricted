# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21771444"))
API_HASH = getenv("API_HASH", "4162cac0a1a3e792023b8e9092030d8c")
BOT_TOKEN = getenv("BOT_TOKEN", "8074668619:AAFyGz3kc5XO_kpxyXv6Hmm1MOjeLbHH3b0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7570884654").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Test2:Monstersir123@cluster0.ltadb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002471376518")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002404933413"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "25"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "5cc622e06b9f408dca33e939b2864329eb39621e")
STRING = getenv("STRING", "BQFMNLQAg8JAWvvtARk6j5_-1_ITU9EwbPpvd2u8hxSuUu1F0CQVYp0tcxQwiJ2rMtd0UGrpHspuSHUAzUybylTolQ4O4EI4PN9mblRXu7o46VnADMRnrF6I4rPCLL1oR0r4cRKbNrz94bqnyQh9IRxA6CFaTf6OHEC7nz-26y7nyhAOWn08K3sKp9mUU3PxBmSL_o8CeUjohiH5Z3xg69XuY60XHPdXyxxLtX7px_0UJgTH6rcyO135-RpidlXlNHM47GpI6hpqIQj67lejqiwQ9zR1mwbBJQFMt90cZ4PoTIXFpfdWavsaWhEwmzzSQpQ9pHLHpp25KlvbbbbmrlPhnaLwHAAAAAGIiOaNAA")
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
