#!/usr/bin/python3
import os
import aiml
from flask import Flask, request, jsonify,render_template
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("query", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    BRAIN_FILE="bot_brain.brn"

    #initialize the kernel 
    k = aiml.Kernel()

    # To increase the startup speed of the bot it is
        # possible to save the parsed aiml files as a
        # dump. This code checks if a dump exists and
        # otherwise loads the aiml from the xml files
        # and saves the brain dump.
    if os.path.exists(BRAIN_FILE):
            print("Loading from brain file: " + BRAIN_FILE)
            k.loadBrain(BRAIN_FILE)
    else:
            print("Parsing aiml files")
            k.bootstrap(learnFiles = "startup.xml", commands = "'LOAD AIML B")
            print("Saving brain file: " + BRAIN_FILE)
            k.saveBrain(BRAIN_FILE)

    while True:
            input_text = name
            response = k.respond(input_text)
            det = response
            return jsonify({"response" : det})


# A welcome message to test our server
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)