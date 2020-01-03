### Use Case Refinement
Use case 1: User asks a question, bot classify the question and get the related tag
```
1) Preconditions:
User is a member of the group chatting and Bot is tagged along with the question.
2) Main Flow:
The user asks a question[S1]. Bot asks whether the user is asking a question[S2]. Bot replies with the question category and relevant questions on Stack Overflow[S3] and asks whether the user needs to find a solution on Stack Overflow[S4].
3) Subflows:
[S1] User asks a question. (On general channel or private channel)
[S2] Bot asks the user if he/she is asking a question.
[S3] Bot assigns a question category to the asked question through a classification model and return the category with relevant questions.
[S4] Bot asks the user whether he/she needs to search the solution in Stack Overflow
4) Alternative Flows
[E1] There is no recognized category in database. No relevant questions returned.
[E2] User is asking a question
```
Use case 2: User questions are redirected to Stack Overflow to find answers
```
1) Preconditions
The provided relevant questions are not helpful for users.
2) Main Flow
User asks the QuestionHelperBot[S1] to find the solutions on Stack Overflow[S2].
3) Subflows
[S1] User provides the request he/she wants more information not only what has been discussed within the Slack channel.
[S2] QuestionHelperBot will return the link of Stack Overflow based on the relevance.
4) Alternative Flows
[E1] The requested category doesn’t exist in the list which the bot provides and return the “cannot find” message, then it is prompted to try again.
```
Use case 3: Return questions summary
```
1) Preconditions
Bot and ‘QuestionSummary’ label is tagged by user.
2) Main Flow
User asks the Bot to provide question summary[S1]. QuestionHelperBot will return the number of questions asked today and their titles[S2].
3) Subflows
[S1] User asks Bot to provide question summary.
[S2] Bot return the number of questions and titles.
4) Alternative Flows
[E1] Nobody has asked question today.
```
We change the question search from searching in the channel history to search on Stack Overflow

### BOT IMPLEMENTATION
The bot is a slack chat bot, the bot entry is in https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/bot/QuestionHelper.py

### Mock Service
The main functionality of the service is to provide a question tag for a question asked by user and call StackOverFlow API to extract relevant questions link. For this part, we defined interface for predictive model and stackOverFlow APIs. Currently we used fake mock data as service returns.

QuestionTagModel provides a tag of a question predicted by offline trained predictive model. We hardcode a fake tag as mock data.
https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/bot/QuestionTagModel.py

StackOverFlowAPI parts include functions of calling stackoverflow api to get wanted question hyperlinks. We filled fake questions links as mock data service will return.
https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/bot/StackOverFlowApi.py

### Selenium Testing

We use Selenium to verify that the bot is returning the correct response, please check as below:

https://github.ncsu.edu/csc510-fall2019/CSC510-15/tree/master/bot/SeleniumTest

### Screencast

#### Bot Implementation
https://drive.google.com/file/d/1nEE8GktlwRXlijGFa1S3_cjNLpkjdDKa/view?usp=sharing


#### Selenium Testing
https://drive.google.com/file/d/1LoaPo0zuuzPrnNXkBZ6c6Z-nOiI46iE0/view?usp=sharing
