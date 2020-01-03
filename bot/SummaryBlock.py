class SummaryBlock:

    def __init__(self):
        self.summary_statistics = 0
        self.questions = []
    
    def get_Summary_Block(self):
        # question = "%s questions have been asked today\n" % self.summary_statistics
        if self.summary_statistics == 0:
            question = "No question has been asked\n"
        elif self.summary_statistics == 1:
            question = str(self.summary_statistics) + "   "+"question has been asked\n"
        else:
            question = str(self.summary_statistics) + "   "+"questions have been asked\n"

        for q in self.questions:
            question += str(q) + '\n'

        attachments = [
                {
                    "text" : question
                }
            ]

        return attachments   

    def update_summary(self, q):
        self.summary_statistics += 1
        self.questions.append(q)

    def update_questions(self, q):
        self.questions.append(q)
    

