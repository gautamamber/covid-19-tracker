from flask import Flask, render_template
import requests

app = Flask("__name__")
URL = "https://api.covid19api.com/summary"

@app.route('/')
def home():
	data = requests.get(URL)
	response = data.json()
	content = response['Global']
	country = response['Countries']
	return render_template('index.html', content=content, country=country)


if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug = False, host="0.0.0.0", port=8000)  