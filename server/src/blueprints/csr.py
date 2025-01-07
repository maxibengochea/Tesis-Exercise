#dependencias
from flask import Blueprint

#crear el blueprint 'auth' e importar las vistas
csr = Blueprint('csr', __name__)
import src.routes.csr