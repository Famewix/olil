from dotenv import load_dotenv
import os

load_dotenv()

print(bool(os.getenv('FULLSCREEN')))