"""
Beta version of GradioSRV
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    return "GradioSRV is online", 200


@app.route("/validate", methods=["GET"])
def validate():
    token = request.args.get("token")
    role = request.args.get("role")

    if token is None or role is None:
        return "Missing `token` or `role` parameters", 401

    if role not in ["Admin", "QA", "Beta"]:
        return "Invalid role", 400

    if len(token) != 37 or (not token.startswith("hf_")):
        return "Invalid HuggingFace token", 401
    
    # TODO: perform auth check with HuggingFace
    # TODO: return temporary API key to user for making genuine requests
    return "Simple validation performed", 200


@app.route("/query", methods=["GET"])
def query():
    return "Query endpoint not yet implemented", 501


if __name__ == "__main__":
    app.run(debug=True)
