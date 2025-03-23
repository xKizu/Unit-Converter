from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/button-click", methods=["POST"])
def button_click():
    return redirect(url_for('home'))

@app.route("/length", methods=["GET", "POST"])
def length():
 
    LENGTHS = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,        
    }
    result = None
    to_unit_unit = None
    if request.method == "POST":
        length = float(request.form["length"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        to_unit_unit = request.form["to_unit"]
        from_unit = LENGTHS[from_unit]
        to_unit = LENGTHS[to_unit]
        result = length * from_unit / to_unit
    return render_template("length.html", result=result, to_unit_unit=to_unit_unit)

@app.route("/weight", methods={"GET", "POST"})
def weight():

    WEIGHTS = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "ounce": 28.35,
        "lb": 453.59,
    }

    result = None
    to_unit_unit = None
    if request.method == "POST":
        weight = float(request.form["weight"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        to_unit_unit = request.form["to_unit"]
        from_unit = WEIGHTS[from_unit]
        to_unit = WEIGHTS[to_unit]
        result = weight * from_unit / to_unit
    return render_template("weight.html", result=result, to_unit_unit=to_unit_unit)

@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    
    TEMPERATURES = {
        "Celsius": "°C",
        "Fahrenheit": "°F",
        "Kelvin": "K"
    }

    result = None
    to_unit_unit = None

    if request.method == "POST":
        temperature_value = float(request.form["temperature"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        to_unit_unit = request.form["to_unit"]
        from_unit = TEMPERATURES[from_unit]
        to_unit = TEMPERATURES[to_unit]

        match (from_unit, to_unit):
            case ("°C", "°F"):
                result = (temperature_value * 9/5) + 32
            case ("°F", "°C"):
                result = (temperature_value - 32) * 5/9
            case ('°C', 'K'):
                result = temperature_value + 273.15  
            case ('K', '°C'):
                result = temperature_value - 273.15  
            case ('°F', 'K'):
                result = (temperature_value - 32) * 5/9 + 273.15  
            case ('K', '°F'):
                result = (temperature_value - 273.15) * 9/5 + 32  
            case _:
                result = "Invalid conversion units!"  
        
    
    return render_template("temperature.html", result=result, to_unit_unit=to_unit_unit)



    





if __name__ == "__main__":
    app.run()