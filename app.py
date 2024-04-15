import time
import rasa_request_manager
import response_message_from_intent

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)

def chatbot_response(msg):
    res = getResponse(msg)
    return res

def getResponse(msg):
    responseJson = rasa_request_manager.send_request_to_rasa(msg)
    intent = rasa_request_manager.get_intent_from_rasa_response(responseJson)
    entities = rasa_request_manager.get_entities_from_rasa_response(responseJson)
    response_message = response_message_from_intent.get_message_from_intent(intent, entities)
    return response_message


if __name__ == '__main__':
    app.run()
