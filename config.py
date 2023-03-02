from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import parse_mode
from pyrogram.enums import ChatType
from pyrogram.client import Client
from dotenv import load_dotenv
import os
load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')


app: Client = Client("my_group",str(api_id),str(api_hash))