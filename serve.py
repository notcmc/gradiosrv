"""
Beta version of GradioSRV
"""

from flask import Flask, request, jsonify, send_file


app = Flask(__name__)


@app.route("/")
def root():
    return send_file("validate.html")


@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    if not data or "role" not in data or "token" not in data:
        return jsonify({
            "success": False,
            "message": "Missing token or role parameter(s)"
        }), 400
    
    role = data["role"]
    if role not in ["Admin", "QA", "Beta"]:
        return jsonify({
            "success": False,
            "message": "Invalid role"
        }), 400
    
    token = data["token"]
    if len(token) != 37 or (not token.startswith("hf_")):
        return jsonify({
            "success": False,
            "message": "Malformed HuggingFace token"
        }), 400
    
    return jsonify({
        "success": True,
        "message": "Validation successful"
    }), 200


@app.route("/query", methods=["GET"])
def query():
    return "Query endpoint not yet implemented", 501


if __name__ == "__main__":
    app.run(debug=True)
