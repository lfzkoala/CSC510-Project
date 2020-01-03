import json
import requests

class StackOverFlowApi:

    def __init__(self):
        return
    
    def search_question_on_stackoverflow(self, q):
        link = "https://stackoverflow.com/search?q="
        tmp = q.replace(" ", "+")
        link += tmp
        return link

    # Get top relevant StackOverFlow links for relevant questions
    # API site
    # https://api.stackexchange.com/docs/faqs-by-tags
    def get_Frequent_Questions_of_a_tag(self, tag):
        api_call = "https://api.stackexchange.com/2.2/tags/" + tag + "/faq?site=stackoverflow"
        text = requests.get(api_call).text
        items = json.loads(text)["items"]
        linklist = []
        titlelist = []
        for i in range(3):
            print(i)
            linklist.append(items[i]["link"])
            titlelist.append(items[i]["title"])
        return linklist, titlelist

    
    # API site
    # https://api.stackexchange.com/docs/related-tags
    # get related tag by given tag
    # e.g. give:java return android, spring
    def get_related_tag(self, tag):
        api_call = "https://api.stackexchange.com/2.2/tags/" + tag + "/related?site=stackoverflow"
        text = requests.get(api_call).text
        items = json.loads(text)["items"]
        tag1 = items[1]["name"]
        tag2 = items[2]["name"]
        tag3 = items[3]["name"]
        taglist = [tag1, tag2, tag3]
        return taglist
    
    # API site
    # https://api.stackexchange.com/docs/questions
    # get top voted question by given tag
    def get_recommend_question(self, tag):
        api_call = "https://api.stackexchange.com/2.2/questions?order=desc&sort=votes&tagged=" + tag + "&site=stackoverflow"
        text = requests.get(api_call).text
        items = json.loads(text)["items"]
        q1_link = items[0]["link"]
        q1_title = items[0]["title"]
        q2_link = items[1]["link"]
        q2_title = items[1]["title"]
        linklist = [q1_link, q2_link]
        return linklist
