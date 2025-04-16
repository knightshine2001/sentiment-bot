from flask import Flask, render_template, request, redirect
import json
import os
import datetime
import random

app = Flask(__name__)

CONFIG_FILE = "config.json"
LOG_FILE = "log.txt"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

@app.route("/")
def index():
    config = load_config()
    return render_template("index.html", config=config)

@app.route("/update", methods=["POST"])
def update_config():
    config = load_config()
    config["interval"] = int(request.form["interval"])
    save_config(config)
    return redirect("/")

@app.route("/trade/<symbol>/<action>")
def manual_trade(symbol, action):
    log(f"Manual {action.upper()} trade triggered for {symbol}")
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
