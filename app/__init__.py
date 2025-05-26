from flask import Flask
from config import Config
from app.controller_form import ControllerForm
from app.energia import Energia
from app.emergia import Emergia
from app.servidores import Servidores

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    energia = Energia()
    emergia = Emergia()
    servers = Servidores()

    controller_form = ControllerForm(emergia, energia, servers)
    app.register_blueprint(controller_form.blueprint)

    return app