#@Imports
from flask import Flask
from flask_jwt_extended import JWTManager

#@Self-modules
from config import JWT_SECRET_KEY

#@APIConfigs
app = Flask(__name__)
app.json.sort_keys = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
jwt = JWTManager()
jwt.init_app(app)

#@Routes    @Carros
from routes.carro import carros_bp
app.register_blueprint(carros_bp, url_prefix='/api')

#@Routes    @Users
from routes.user import users_bp
app.register_blueprint(users_bp, url_prefix='/api')

app.run()