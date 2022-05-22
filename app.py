
from flask import Flask, send_from_directory

path = "static/uploads/"

# Импортируем blueprints
from main.main import main_blueprint

from loader.loader import loader_blueprint


app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# регистрируем в приложении main_blueprint
app.register_blueprint(main_blueprint)

# Регистрируем в приложении loader_blueprint
app.register_blueprint(loader_blueprint)


@app.route("/post_uploaded/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

if __name__ == '__main__':
    app.run(debug='on')

