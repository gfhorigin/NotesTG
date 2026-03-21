from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

# --------Constants


#callback data
CB_FULL = 'full'
CB_FULL_VIEW = 'full_view'
CB_DELETE = 'delete'