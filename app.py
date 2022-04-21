import os
from flask import Flask
from flask import Blueprint
from LINEBot.LINEBot import LINEBot

app = Flask(__name__)
app.register_blueprint(LINEBot)

@app.route('/')
def welcome():
    return 'Welcome to My first Website!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
