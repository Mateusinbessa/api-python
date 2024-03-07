from dotenv import load_dotenv
import os

load_dotenv()

#.ENV INFORMATIONS
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
DB_HOST= os.getenv('DB_HOST')
DB_NAME=os.getenv('DB_NAME')
DB_USER=os.getenv('DB_USER')
DB_PWD=os.getenv('DB_PWD')
