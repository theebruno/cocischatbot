from chatbot import chatbot
from flask import Flask, render_template, request,jsonify
import mysql.connector

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/getmsg', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("query", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        det = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    # return jsonify(response)
    return jsonify({"response" : str(chatbot.get_response(name))})    

@app.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="chatbot"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        signup=request.form
        username = signup['username']
        password = signup['password']
        mycursor.excute("select * from reg where Username='"+username+"' and Password='"+password+"'")
        r=mycursor.fetchall()
        count=mycursor.rowcount
        if count==1:
            return render_template("index.html")
        else:
            return render_template("login.html")
        
    mydb.commit()
    mycursor.close()

if __name__ == "__main__":
    app.run() 