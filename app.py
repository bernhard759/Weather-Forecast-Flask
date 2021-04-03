# import
import api
from flask import Flask, render_template, request
import datetime


# flask app object
app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def forecast():

    if request.method == "POST":
        city = request.form.get("city")
        
        try:
            lat, lon, part, name, country = api.getGeo(city)
        except:
            return render_template("error.html", city=city)
        
        temp_forecast, w_forecast = api.getWeather(lat, lon, part)
        date_list = [date for date in temp_forecast]
        temp_list = [value for _, value in temp_forecast.items()]
        w_list = [value for _, value in w_forecast.items()]

        return render_template("forecast.html", name=name, temps=temp_list, dates=date_list, w_list=w_list, country=country)
    
    else:
        
        return render_template("home.html")
    

# run app on test server
if __name__ == "__main__":
    app.run(debug=True)