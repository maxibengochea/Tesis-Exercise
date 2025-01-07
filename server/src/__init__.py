from dotenv import load_dotenv
from flask import Flask
from src.blueprints.csr import csr
import os

#usar las variables de entorno
load_dotenv()

#inicializar la app
def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
  app.register_blueprint(csr)
  return app