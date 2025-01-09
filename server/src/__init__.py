from dotenv import load_dotenv
from flask import Flask
from src.routes.csr import csr
from flask_cors import CORS
import os

#usar las variables de entorno
load_dotenv()

#inicializar la app
def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
  app.register_blueprint(csr)
  CORS(app)
  return app