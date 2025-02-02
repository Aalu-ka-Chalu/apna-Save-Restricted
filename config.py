# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21008992"))
API_HASH = getenv("API_HASH", "da87f6dea5ed8cfe1a53617e33a35742")
BOT_TOKEN = getenv("BOT_TOKEN", "7833652782:AAH67YiP2e-3WwtVfBj-DMfRLbW2qt7WAJA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7570884654").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Test2:Monstersir123@cluster0.ltadb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002471376518")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002404933413"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "25"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "5cc622e06b9f408dca33e939b2864329eb39621e")
STRING = getenv("STRING", "AQFAkmAApf7Q9vYRxM4fXr89s5jQPwQMpBUWMNVqXx0b2zvRvMjhzk9FnAgOAx98_SMG_bR1JuiyQf75tW5c6c-A7h6lkVYQlvIs7hkdyTBctYptG6kbRXTHpP-sNPn3HQBp2sYoD1f6XP61f1CS02jfqqulI_jMz4M7VfGEFUC9BrCHGyKwFItT8kz704ZA0wkh-3M_gvz_DQkqsHxf4raS2s3DO8eTDeh20M3H_xAfgXJ99YG6METuldcUJXO2GWskw2bTDc5aSXDAECVte4DijynJK7CTg_Yna95FQH537-EJPDOAMUG4cJkMECnny0V_uBLaelV4VElY9aRbhQ10VTmj5gAAAAG7s_SZAA")
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
