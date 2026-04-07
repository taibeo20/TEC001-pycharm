from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

file_path = os.path.join(os.path.dirname(__file__), "airports.json")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        airports = json.load(f)
    print("Loaded airports:", airports)  # debug
except Exception as e:
    print("Lỗi đọc file:", e)
    airports = []

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    icao = icao.upper()

    for airport in airports:
        if airport["icao"] == icao:
            return jsonify(airport)

    return jsonify({"error": "Airport not found"}), 404



if __name__ == '__main__':
    app.run(debug=True)