from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return {"message": "Hello World"}

if __name__ == "__main__":
    # Bind to 0.0.0.0 for Azure App Service
    app.run(host="0.0.0.0", port=8000)
