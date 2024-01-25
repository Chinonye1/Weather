from dotenv import load_dotenv
import os


import json
import urllib.parse

from flask import Flask, Response, render_template, request

app = Flask(__name__)

@app.route("/")
def student():
    return render_template("student.html")

@app.route("/result",methods = ["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html",result = result)
    
@app.route("/forecast", methods=[ "GET"])  
def get_forecast():
    data = {}
    data["q"] = request.args.get("city")
    data["appid"] = os.getenv('API_KEY')

    print("Data:", data)
    url_values = urllib.parse.urlencode(data)
    print(url_values)
    url =  "http://api.openweathermap.org/data/2.5/forecast"
    full_url = url + "?" + url_values
    print("Full URL:", full_url)
    data = urllib.request.urlopen(full_url)

    resp = Response()
    print(resp.status_code)
    return render_template("weather.html", title="Weather App", data=json.loads(data.read().decode("utf-8")))







if __name__ == "__main__":
    app.run(port=5001,debug=True)