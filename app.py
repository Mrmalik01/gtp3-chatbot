from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import ask_ai, append_the_conversation

app = Flask(__name__)
app.config['SECRET_KEY'] = "23!#@#!@#!@RFfdfjidfjidfni$423232"

@app.route("/bot", methods=['POST'])
def bot():
    print(request.values)
    incoming_msg = request.values['Body']
    chat_log = session.get("chat_log")

    #answer = ask_ai(incoming_msg, chat_log)
    #session['chat_log'] = append_the_conversation(incoming_msg, answer, chat_log)
    answer = "Hello, I am a bot built by Khizar"
    response = MessagingResponse()
    response.message(answer)
    print("New message received : {}".format(incoming_msg))
    print("Answered : {}".format(answer))
    return response.__str__()

if __name__ == "__main__":
    app.run(debug=True)

