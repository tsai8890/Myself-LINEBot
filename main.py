import os
from flask import Flask
from flask import Blueprint
from aboutMe_bot import aboutMe_bot

app = Flask(__name__)
app.register_blueprint(aboutMe_bot)

@app.route('/')
def welcome():
    return 'Welcome to My first Website!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
