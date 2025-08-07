from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

CONFIG_FOLDER = 'config'
config_data = {}

# Load all configs
for file in os.listdir(CONFIG_FOLDER):
    if file.endswith(".json"):
        with open(os.path.join(CONFIG_FOLDER, file), 'r') as f:
            data = json.load(f)
            config_data.update(data)

@app.route("/<key>", methods=["GET"])
def get_value(key):
    value = config_data.get(key, "Key not found")
    return jsonify({key: value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
