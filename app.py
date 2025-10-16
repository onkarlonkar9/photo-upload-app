from flask import Flask, render_template, request, jsonify
import base64
import requests

app = Flask(__name__)

API_URL = "https://oqgyia4chg.execute-api.ap-southeast-1.amazonaws.com/prod/upload"

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    error = None

    if request.method == "POST":
        file = request.files.get("image")
        if not file:
            error = "Please select an image!"
        else:
            image_data = base64.b64encode(file.read()).decode("utf-8")
            try:
                response = requests.post(API_URL, json={"image": image_data})
                response.raise_for_status()
                image_url = response.json().get("url")
            except Exception as e:
                error = str(e)

    return render_template("index.html", image_url=image_url, error=error)

if __name__ == "__main__":
    app.run(debug=True)
