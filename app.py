from flask import Flask, render_template
import requests

app = Flask("__name__")
URL = "https://api.covid19api.com/summary"

@app.route('/')
def home():
	# data = requests.get(URL)
	# response = data.json()
	return render_template('index.html')


if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug = True, host="0.0.0.0")  