from flask import Flask, request, jsonify
import os

def create_app():
    app = Flask(__name__)
    # Set logs level
    app.logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))
    app.logger.info("ATF2 CMDB Listener starting up...")
    # loads all const from backend_config.py into app.config dictionary.
    app.logger.info("ATF2 CMDB Listener loading config...")
    app.logger.info("ATF2 CMDB Listener has started.")
    return app

app = create_app()


@app.route('/', methods=['POST'])
def hello_world():
    request_json = request.get_json()
    print(request_json)
    print(request)
    print(request.data)
    print(request.form["data"])
    if str(request.form["data"]) == "CLOUD ENTERPRISE SOLUTIONS":
        return "https://andresmontemayorsalinas.github.io/CodeWarsAugust/Challenges/Cipher2BaN9qbtd3h.html"
    else:
        return f'Try again!!'

if __name__ == "__main__":
    app.run()