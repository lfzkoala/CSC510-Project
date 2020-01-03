import json
import os

class MessageManager:

    def __init__(self, form_json):
        # self.channel = channel
        self.timestamp = ""
        self.payload = form_json

    def selectIsnotQuestion(self):
        message = {
                "ts":self.payload["message_ts"],
                "channel": self.payload["channel"]["id"],
                "blocks" : [
                    {
                    "type": "section",
                    "text": {
                    "type": "mrkdwn",
                    "text": "Sorry to bother!" 
                        }
                    }
                ]
            }
        return message

    
    def selectIsQuestion(self, tag, linklist, titlelist, taglist):
        content = ""
        for i in range(len(linklist)):
            content += titlelist[i] + ":"+"\n"+ linklist[i] + "\n\n"
        related_tags = ""
        for i in taglist:
            related_tags += i + "    "
        message = {
                "ts":self.payload["message_ts"],
                "channel": self.payload["channel"]["id"],
                "blocks" : [
                    {
                    "type": "section",
                    "text": {
                    "type": "mrkdwn",
                    "text": (
                        f" :blush: Based on our classification model, your question belongs to: *{tag}*  \n\n"
                        "*Relevant tags of the predict tag are:*\n\n"
                        f"{related_tags}"
                        "\n\n"
                        "*Relevant frequent questions in StackOverFlow are shown below:*\n\n"
                        f"{content}"
                        ),    
                        }
                    }
                ]
            }

        return  message     

    def selectIsSearch(self, searchlist):

        message = {
            "ts" : self.payload["message_ts"],
            "channel": self.payload["channel"]["id"],
            "blocks" : [
                {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                             ":thinking_face: *Your searching results in Stack Overflow:*\n\n"
                        f"{searchlist}"
                        ),
                    }
                }
            ]
        }
        return message

    def getSearchingBlock(self, questionContent:str):
        attachments = [
            {
                "text": "Searching your question on StackOverFlow?",
                "fallback": questionContent,
                "callback_id": "question_search",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "actions": [
                    {
                        "name": "search",
                        "text": "Yes, search it on Stack Overflow",
                        "type": "button",
                        "value": "yes"
                    } ,

                    {
                        "name": "search",
                        "text": "No, Thanks",
                        "type": "button",
                        "value": "no"
                    }

                ]
            }
        ]
        return attachments
      