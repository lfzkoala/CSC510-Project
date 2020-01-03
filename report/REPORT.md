# Final Presentation
https://drive.google.com/file/d/11-i89xz-H-zLsgNIuJIvDLlIEJTEM4wJ/view?usp=sharing

# Report 
### Problem Statement
The QuestionHelperBot is an intelligent Slack chatbot that is built to  detect questions in a group chat and return helpful responses for users.

As what we've described in the problem statement, we are devoted to improve collaboration and efficiency of group chats and discussions on Slack (a common chat platform for teams). When team members launch various activities in Slack, such as sending messages in a public or private channel, searching previous asked questions. We came up with a solution that utilizes question-response mechanism sending questions to our question classification model. Our model trained using large amount of dataset from Stack Overflow assigns a relevant tag for the question. In this way the relevant questions and corresponding answers are ready to use by implementing StackOverflow API. Additionally, QuestionHelperBot can search for the user’s question directly on Stack Overflow.

For the AI part, we obtained the training data from Stack Overflow, preprocesed it and conducted feature selection. We explored several machine learning algorithms and chose the one with the highest accuracy. User messages are retrieved from Slack API and passed it to our tag-predicting model.

Our QuestionHelperBot improves user efficiency by searching only the relevant information in an intelligent way.

### Primary Features

Our QuestionHelperBot consists of multiple attractive features. In high level, the techniques include some advanced machine learning (classification) algorithms used to train our AI model. The data was extracted from the contents of StackOverFlow. During the implementation, we used Python programming language and interfaces of Slack and StackOverFlow to connect ingredients in our QuestionHelperBot. We used Java language to do Selenium Testing. Our QuestionHelperBot is executed on a remote server, which is an Amazon AWS (with Ubuntu Operating System). To run it on our server from the client side, we use Ansible-playbook. In addition, the bot provides many interesting featured functioanlities for Slack users. It can detect users' questions and help users automatically. In the following context, we list several most interesting features. 

**Hybrid Architecture Design**:

Our design architecuture follows the pattern of Hybrid Architecture, which includes ingredients of three types of architecture patterns: Data Centered, Call and Return, and Data Flow. 

![feature1](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/report/Figures/architecture.jpg)

**Fancy Machine Learning Classification Technique - RidgeClassifier**:

We trained our classification model using over 10K data from Stack Overflow dump. We explored different machine learning algorithms and compared with their predictive accuracy using test data. We chose RidgeClassifier as our final algorithms becuase of its high accuracy in prediction. The model trained offline could be used directly to our bot with low latency for getting results.

![feature2](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/report/Figures/RidgeClassifier.jpg)

**Great User Experience**

We guarantee users' experience when using our Bot. The bot will check with users whether they are asking questions once it detects questions. The bot will respond based on users reaction, which chooses 'Yes' or 'No' by users themselves, instead of answering questions unconditionally.  

![feature3](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/report/Figures/question.jpg)

**Thoughtful Prediction Results**

Our bot provides thoughtful prediction results. It not only provides answer links belong to only one tag, but also provides top relevant *relevant* tags. This allows users choosing what they want and let the bot more flexible to use.  

![feature4](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/report/Figures/relevant.jpg)

**Trusted Solution**

Our bot provides solutions using resources of StackOverFlow. We provide "Two-layer" guarantees to make sure those solutions are promising. The first layer returns the top predicted solution links back to the users. If users still felt unsatisfactory, they can click the corresponding button and receive an exact link on StackOverFlow about the question he/she asks. 

![feature5](https://github.ncsu.edu/csc510-fall2019/CSC510-15/blob/master/report/Figures/solution.jpg)

### Reflection on the Development Process and Project

Following the directions on different milestones, we participated in a complete software development process and understood what we should focus on in each phase of the development cycle.

In the first milestone, the primary goal was to define a problem we wanted to solve and figure out the use case and architecture design. We started with meeting together and brainstormed various ideas. A key point at this stage was the feasibility of the proposed solution. We proposed ideas and rejected a lot of them based on the feasibility. After several meetings and discussions, we finally formulated the idea of building a question helper bot on Slack. Further, we wrote down use cases and our architecture design. The design milestone is very important because it decides the project direction. The architecture design helped us to understand what components we needed to implement and helped us to create a project plan.

The second milestone was to implement the main framework of the bot and create mocking service and data for not-yet-implemented components. We chose to use python with slack-client and slack-event-api libraries to implement the core bot framework. At this stage, the bot could listen to the events happening in a group chat and give basic replies with mocked data from mock service. We ran integration tests (using selenium) to make sure our bot works properly. We learned the concepts of unit and integration testing.

In the Process milestone, we finished the main functionality of the bot and also focused on practice development process. We divided tasks and set up regular meetings to sync up on the  progress. We used scrumban methodology to track team member's progress and developed our project in two iterations. The two-iteration setting helped us speed up and smooth the development process. We tried different practices to help with the development process. As part of this milestone, we finished training our question prediction model and integrated it with the bot service. We also implemented the functionality of extracting information from Stack Overflow using its API. 

We deployed the bot to a ubuntu-based cloud instance on AWS Lightsail. We wrote a set of ansible playbooks to  do configuration management (install required packages and start the bot automatically). This allowed us to quickly migrate to a new instance (if needed) and feel more confident with regular deployments.

In genearl, we learned to develop software efficiently and work collaboratively as a team. 

 
### Limitation and Future Work

#### Limitations of question classification model:
1. Limited predictive accuracy and limited number of assigned tags.

We trained our model using over 10,000 Stack Overflow questions with 20 different tags. Training data includeed both questions titles and contents. The accuracy of the model is about 62% for 20 classes classification problem. We understand that a higher prediction accuracy and higher number of tags is needed in a real work environment.

2. Relevant questions

Currently, our bot provides relevant questions on Stack Overflow under the predicted tag for the asked question. Due to this, the relevancy is limited. 

#### Limitations of getting question summary:

1. Limited number of questions could be stored. 

User can request an overview of question summary asked in the channel. Current version does not use a database to store it, so the amount of stored historic data is limited (and reset on bot restart).

2. The summary right now only shows question titles.

The summary we get right now only contains question titles. An improvement can be made by adjusting the bot to also provide relevant questions for each of them. 

#### Future Work:

For question classification model, to improve the accuracy of predicting results, we could explore fancier machine learning or deep learning methods. We explored multiple machine learning models but we haven't had a chance to try deep learning methods in NLP. We could also increase the number of tags that the bot can recognized. To get more relevant questions, instead of getting frequent questions under the same tag, we could also measure the similarity between the asked questions and questions extracted from Stack Overflow.
