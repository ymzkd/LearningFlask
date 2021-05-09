from flask import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def index():
    return jsonify({"language": "パイソン"})


if __name__ == "__main__":
    app.run(debug=True)
