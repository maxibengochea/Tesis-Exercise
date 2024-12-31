import os
from dotenv import load_dotenv

#usar las variables de entorno
load_dotenv()




from flask import Flask

#inicializar la app
def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
  return app