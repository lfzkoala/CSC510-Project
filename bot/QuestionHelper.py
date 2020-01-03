from flask import Flask, request, make_response, Response
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import logging
from logging.handlers import RotatingFileHandler
import os
import json
from ConfirmationBlock import ConfirmationBlock
from MessageManager import MessageManager
from SummaryBlock import SummaryBlock
from StackOverFlowApi import StackOverFlowApi
from QuestionTagModel import QuestionTagModel

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = SlackClient(slack_bot_token)

# Flask webserver for incoming traffic from Slack
app = Flask(__name__)

summary_block = SummaryBlock()
prediction_model = QuestionTagModel()
stackOverFlowApi = StackOverFlowApi()

slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)


# Listening for message
# When message contains certain symbols, bot 
@slack_events_adapter.on("message")
def handle_message(event_data):
    #print(event_data)
    message = event_data["event"]
    channel = message["channel"]
    text = message.get('text')
    print(text)
    # user = message["user"]
    lower_text = text.lower()
    
    if message.get("subtype") is None and ("summary" in lower_text):
        print(text)
        slack_client.api_call("chat.postMessage", channel=channel, text="", attachments=summary_block.get_Summary_Block())

    # If the incoming message contains question pattern, the bot reply confirmation block
    if message.get("subtype") is None and message_pattern(lower_text):
        # user must get here
        user = message["user"]

        summary_block.update_summary(text)
        confirmation_block = ConfirmationBlock(channel, text, user)
        reply_text, reply_attachment = confirmation_block.get_Confirmation_Block(text, user)
        slack_client.api_call("chat.postMessage", channel=channel, text=reply_text, attachments=reply_attachment)


# Listening on user's actions for buttons
@app.route("/slack/message_actions", methods=["POST"])
def message_actions():
    # Parse the request payload
    payload = json.loads(request.form["payload"])

    selection_item = payload["actions"][0]["name"]
  
    selection_value = payload["actions"][0]["value"]

    reply_action = MessageManager(payload)
    # get tag using trained model


    if selection_item == "isQuestion":
        if selection_value == "yes":

            question_content = payload["original_message"]["attachments"][0]["fallback"]
            # print(question_content)
            tag = prediction_model.get_Question_tags(question_content)
            print(type(tag))
            linklist, titlelist = stackOverFlowApi.get_Frequent_Questions_of_a_tag(tag)
            taglist = stackOverFlowApi.get_related_tag(tag)
            message = reply_action.selectIsQuestion(tag, linklist, titlelist, taglist)
            response = slack_client.api_call("chat.postMessage", **message, attachments=reply_action.getSearchingBlock(question_content))
            
            return ""
        elif selection_value == 'no':
            #reply_is_question = MessageActions(payload)
            message = reply_action.selectIsnotQuestion()
            response = slack_client.api_call("chat.update", **message, attachments=[])
            return ""
        else:
            return ""

    if selection_item == "search":
        if selection_value == "yes":
            # reply_is_selection = MessageActions(payload)
            question_content = payload["original_message"]["attachments"][0]["fallback"]
            # get search link
            link = stackOverFlowApi.search_question_on_stackoverflow(question_content)
            message = reply_action.selectIsSearch(link)    
            response = slack_client.api_call("chat.postMessage", **message)
        else:
            response = slack_client.api_call("chat.postMessage", channel=payload["channel"]["id"], ts=payload["message_ts"], text="It's great to help you! :smile:")
            return ""

    return ""


# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

def message_pattern(message:str):
    if "why" in message or "what" in message or "how" in message or "where" in message or "?" in message:
        return True
    else:
        return False

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
# slack_events_adapter.start(port=3000)
if __name__ == "__main__":
    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
    logger = logging.getLogger('tdm')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    app.run(host = '0.0.0.0')
