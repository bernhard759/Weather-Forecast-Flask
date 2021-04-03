# import
import api
from flask import Flask, render_template, request


# flask app object
app = Flask(__name__)


# route
@app.route("/", methods=["POST", "GET"])
def forecast():

    # check for post request
    if request.method == "POST":
        city = request.form.get("city")
        
        # error handling
        try:
            lat, lon, part, name, country = api.getGeo(city)
        except:
            return render_template("error.html", city=city)
        
        # get forecast data
        temp_forecast, w_forecast = api.getWeather(lat, lon, part)
        date_list = [date for date in temp_forecast]
        temp_list = [value for _, value in temp_forecast.items()]
        w_list = [value for _, value in w_forecast.items()]

        # render the forecast template
        return render_template("forecast.html", name=name, temps=temp_list, dates=date_list, w_list=w_list, country=country)
    
    else:
        
        # render the home template
        return render_template("home.html")
    

# run app on test server
if __name__ == "__main__":
    app.run(debug=True)