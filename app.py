from ipaddress import ip_address
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/save-location', methods=['POST'])
def save_location():
    try:
        # Get JSON data from the request
        data = request.json
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        ip_address = data.get('ip')

        # Validate the data
        if latitude is None or longitude is None:
            return jsonify({"error": "Invalid data"}), 400

        # Save the data to a text file
        with open('locations.txt', 'a') as file:
            file.write(f"Latitude: {latitude}, Longitude: {longitude}, IP Address: {ip_address}\n")

        return jsonify({"message": "Location saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/job', methods=['GET'])
def job_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)