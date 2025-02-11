# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29147137"))
API_HASH = getenv("API_HASH", "59b7c5f4f165db81be482d076d1f78a7")
BOT_TOKEN = getenv("BOT_TOKEN", "7755150258:AAHLU_CXlSlJurbr1T5VHUS7g2pFxSsPdhg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7570884654").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Test2:Monstersir123@cluster0.ltadb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002471376518")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002404933413"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "25"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "5cc622e06b9f408dca33e939b2864329eb39621e")
STRING = getenv("STRING", "BQG8wAEAq9KVwKyl6SPCpS2jCiN1UQIB3be-r-yhWLTMnv3HC8oC0dx9dw5s8rY3bpEJGHtdShMdc6Kmdktv7wOlc7ksqQhKvOJsto1pGHItOv0meQjUYi6Sg_SxKvVqvKLsSnRjIWAiEZVdSap6Fc313KZKjAsk7OVxwW6ZAb0utuhQsvB6AEu9RRjmORgM43TaoATWcY9q5po7wM5qJglu3hlbT8c0rd_1eayqpto5spbrmyMC-FHQoyRSXrzhHIgAB-Cl-JiDpO4mT4LZ1TSqqb5nv-EF9ASyhN8UHn_5NIxxJ0-NA3RDweAG9Cbew9SeWYceztY6iRbs8mkeBdktO6AZJAAAAAHWqw1PAA")
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
