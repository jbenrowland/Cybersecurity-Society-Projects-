from flask import Flask, request, jsonify
from flask_cors import CORS
import threat_api  # Import threat intelligence functions

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Backend is running!"})

@app.route('/api/check_ip', methods=['POST'])
def check_ip():
    data = request.json
    ip_address = data.get("ip")
    if not ip_address:
        return jsonify({"error": "No IP provided"}), 400
    result = threat_api.check_ip(ip_address)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
