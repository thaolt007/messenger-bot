import os, sys
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

ACCESS_TOKEN = 'EAAU7uPzf6CwBAMOelEAnKrduXjdFbJw2lFg0Hds8NgLQcXRLZB2VlAtPMZAZCi9IBJZCHMZAgYOQiX1XLG099FVcyiRzZCmgUZB9ZCiAKFJX8qE9eqfJWXhIVZB0qB4P8XuEY1JgZAxX3jCJttDQY16ZB9XFonnVSV0aHI0heZC8ntmyHwZDZD'

bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "bot":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	#log(data)
	
	# Doc message tu facebook, lay ra id, text
	if (data['object'] == 'page'):
		for entry in data['entry']:
			for messaging_event in entry['messaging']:
				# ID nguoi gui
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']
				
				# Text nguoi dung nhan tin
				if messaging_event.get('message'):
					message = messaging_event['message']
					if 'text' in message:	
						text = message['text']
					else:
						text = 'no text'
						
					response = text
					bot.send_text_message(sender_id, response)
	
	return 'ok', 200
	
def log(message):

	print(message)
	sys.stdout.flush()
	
if __name__ == "__main__":
	app.run(debug = True, port = 80)