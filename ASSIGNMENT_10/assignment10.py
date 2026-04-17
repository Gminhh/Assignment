from flask import Flask, jsonify, request
import requests
import csv

app = Flask(__name__)

# 1. CHUCK NORRIS JOKE

@app.route('/joke')
def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify({"joke": data["value"]})
    else:
        return jsonify({"error": "Failed to fetch joke"}), 500


#  2. WEATHER API

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    api_key = "4b3b3c823c2801a2cb414b722afdad06"  

    if not city:
        return jsonify({"error": "City is required"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        description = data["weather"][0]["description"]

        return jsonify({
            "city": city,
            "temperature_C": round(temp_c, 2),
            "description": description
        })
    else:
        return jsonify({"error": "City not found"}), 404



#  3. PRIME NUMBER API

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime/<int:number>')
def check_prime(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })



# 4. AIRPORT API

def find_airport(icao_code):
    with open("airports.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["icao"] == icao_code:
                return row
    return None

@app.route('/airport/<icao>')
def get_airport(icao):
    airport = find_airport(icao)

    if airport:
        return jsonify({
            "icao": airport["icao"],
            "name": airport["name"],
            "city": airport["city"],
            "country": airport["country"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404



if __name__ == '__main__':
    app.run(debug=True)