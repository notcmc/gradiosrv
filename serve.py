from flask import Flask, make_response, request

app = Flask(__name__)

"""
Beta version of GradioSRV
"""


html_template = """
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
        <p>{info}</p>
    </body>
</html>
"""


def get_response(title, heading, info, status):
    return make_response(
        html_template.format(
            title=title,
            heading=heading,
            info=info
        ),
        status
    )


@app.route("/")
def root():
    return get_response(
        "OK",
        "200 OK",
        "GradioSRV is online",
        200
    )


@app.route("/validate", methods=["GET"])
def validate():
    token = request.args.get("token")
    role = request.args.get("role")

    if token is None or role is None:
        return get_response(
            "Bad Request",
            "400 Bad Request",
            "Missing token or role parameter(s)",
            400
        )

    if role not in ["Admin", "QA", "Beta"]:
        return get_response(
            "Bad Request",
            "400 Bad Request",
            "Invalid role",
            400
        )

    if len(token) != 37 or (not token.startswith("hf_")):
        return get_response(
            "Bad Request",
            "400 Bad Request",
            "Malformed HuggingFace token",
            400
        )
    
    # TODO: perform auth check with HuggingFace and return 401 if invalid
    # TODO: return temporary API key to user for making genuine requests

    return get_response(
        "OK",
        "200 OK",
        "Validation successful",
        200
    )


@app.route("/query", methods=["GET"])
def query():
    return "Query endpoint not yet implemented", 501


if __name__ == "__main__":
    app.run(debug=True)
