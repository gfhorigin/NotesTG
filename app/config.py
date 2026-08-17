from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

# --------Constants
NOTE_PREFIX = 'note'
DATABASE_NAME = 'data.db'

USERS_TABLE = 'users'
NOTES_TABLE = 'notes'