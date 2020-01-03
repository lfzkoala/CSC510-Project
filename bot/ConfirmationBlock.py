class ConfirmationBlock:

    def __init__(self, channel, text, user):
        self.channel = channel
        self.username = "pythonboardingbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False
        self.reply_attachment = text
        self.user = user

    
    def get_Confirmation_Block(self, questionContent:str, user_id: str):
        text = "Nice to help you!!  <@%s> " % user_id

        attachments = [
            {
                "text": "Are you asking the question : %s" % questionContent,
                "fallback": questionContent,
                "callback_id": "question_confirmation",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "actions": [
                    {
                        "name": "isQuestion",
                        "text": "Yes",
                        "type": "button",
                        "value": "yes"
                    },
                    {
                        "name": "isQuestion",
                        "text": "No",
                        "type": "button",
                        "value": "no"
                    }  
                ]
            }
        ]

        return  text, attachments       