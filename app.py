# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, world!"
if __name__ == "__main__":
    app.run()
