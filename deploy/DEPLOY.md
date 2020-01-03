# Deployment

## Configuration Management ##

We deployed our bot to a remote ubuntu system from AWS lightsail. You can configure the remote one by running playbook at your local machine. But first of all, we need to add the public key of your local machine to the host. Since the github repository is private and it's hard for the host to git clone directly, we first git clone the repository to the local machine and synchorize the folder to the remote one. So, we also need to add your public key of your local machine to get granted from github. 

To run the playbook locally in your machine:
* Add your public ssh key to the host (contact our team)
* Add your public ssh key to github repository (contact our team)
* Know the bot token and bot signing secrete (contact our team)
* Run the command below:

        ansible-playbook -i \path\to\inventory.txt \Path\to\bot-playbook.yml --extra-vars "secret1=<BOT TOKEN> secret2=<BOT SIGNING SECRET>"

## Acceptance Testing ##

QuestionHelperBot is built to help users with their questions and provide with most relevant information about their questions in slack platform. As an AIbot, QuestionHelperBot uses well-trained offline machine learning models for question classification and incorporate StatckOverFlow as extra resources to provide user help for their questions. QuestionHelper bot will be triggered when the input content contains possible "Question Pattern" such as including question words "How/When/What/Why/Where" or question maker. Once the bot is triggered, the conversation begins and user could interact with the bot to get help. 

### To initiate conversation with QuestionHelperBot

        1. Log-in to slack, enter workspace “csc510-projecthq.slack.com"
        2. Login Account: Email: csc510team15@gmail.com  Password: SEproject2019. The account name is set as “Test Account”. 
        3. After successfully logging-in navigate to "general" channel and execute the test cases given in the acceptance test plan below

![signin](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/signin.jpg)
![workspace](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/workspace.jpg)
![usrpd](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/usrpd.jpg)
![channel](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/channel.jpg)

### Three user cases to be tested:

#### USE CASE 1: User asks a question, bot classify the question and get the related tag and related question links<br>

This use case shows how bot could be triggered and what replies user will receive when bot is triggered. As explained above, **the bot will only be triggered when they input content contains questions words (how/when/what/why/where) and question mark (?)**. Since it is possible that users may have some question-like words but not a real question in daily conversation (like "how are you today?"), we don't want our bot to be annoying and work for those "fake" questions, we add additional confirmation step for user to confirm the triggering content is real question they want help from bot. 

```
Input: enter question content

Output: the bot asks the user whether it’s a question.

Input: click the button ‘yes’ or ‘no’

Output: classification result and related links`
```


**Example 1**:

User confirmed that the content is a real question they want to ask by clicking 'yes' button. 

```
Input: enter the question “What is pointer?”

Output: the bot asks the user whether it’s a question. (see the screenshot below)

Input: click ‘Yes’

Output: 1. the question category/tag learned from machine learning model 

2. top three related tags in StackOverFlow. 

3. Top three related questions with title and link under this category in stackoverflow. 

(see the screenshot below)
```

![usecase1](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/usecase1-1.jpg)

**Example 2**: 

User confirmed the input content is not a question he/she seeks for help.

```
Input: enter the question “What is pointer?”

Output: the bot asks the user whether it’s a question. You can choose ‘Yes’ or ‘No’

Input: click ‘No’

Output: “Sorry to bother！”
```

![usecase1](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/usecase1-2.jpg)

#### USE CASE 2: User questions are redirected to Stack Overflow to find answers<br>

QuestionHelperBot will further ask user whether he/she wants to search their question on StackOverFlow. User decides whether to get further help by clicking the button.

```
Input: click the button ‘yes, search it on StackOverFlow’ or ‘No, thanks’

Output: the link question in StackOverFlow
```
**Example 1**: 

```
Input: the user clicks the button “Yes, search it on StackOverFlow”

Output: a link directed to StackOverFlow
```
The link returned is the search result for this question in StackOverFlow.

![usecase2](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/4.jpg)

By clicking the link providede, you are directed to the following stackoverflow page:

![usecase2](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/stackoverflow.jpg)


**Example 2**: 

```
Input: the user clicks the button “No, Thanks”, 

Output: “It’s great to help you!”
```

![usecase2](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/5.jpg)

#### Use case 3: Return questions summary<br>

Question summary give user a good overview of questions asked in conversations. This event is triggered by word "summary".

```
Input: enter message ‘get summary’
Output: question total number and their titles that have been asked so far.`<br>
```

![0q](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/0q.jpg)
![2q](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/deploy/CSC510%20figures/2q.jpg)

## Exploratory Testing and Code Inspection
The implementation of all use-cases in the bot can be inspected here
1. Main framework of the bot service: [QuestionHelper.py](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/bot/QuestionHelper.py)
1. Offline trained machine learning model: [QuestionPredictiveModel.py](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/bot/QuestionPredictiveModel.py) 
2. The connection part of Predictive Model: with main bot service[QuestionTagModel.py](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/bot/QuestionTagModel.py)
3. The connection part of StackOverFlow API with main bot service: [StackOverFlowApi.py](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/bot/StackOverFlowApi.py)

## Screencast
The link to the screencast for the deployment milestone is https://drive.google.com/drive/u/0/folders/1itQNzRqu5bwTG_BkoLP3GNex9Qc08qGX.
