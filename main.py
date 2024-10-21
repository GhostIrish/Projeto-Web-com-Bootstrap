from flask import Flask
from routes.home import home_route
# url_for serve para montar url internas do nosso servidor web, de acordo com o nome da nossa func
app = Flask(__name__)

app.register_blueprint(home_route)

app.run(debug=True)