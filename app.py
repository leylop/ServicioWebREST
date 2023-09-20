from flask import Flask, jsonify
import app_service.modules.producto.routes as producto_routes

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger_send_request():
    producto_routes.send_request()
    return jsonify({"message": "send_request executed successfully!"})
