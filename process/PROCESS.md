

## Iteration 1

### Process
#### WorkSheet Record ####

Tasks we left from last milestone include: 
* Build and train predictive model which can predict a tag for a question asked by user. (Use case 1)
* Integrating with StackOverFlow API to extract needed information. (Use case 1 & 2)
* Implement question summary functionality.(Use case 3)

We divided those tasks into three big parts with : Predictive Model, StackOverFlow API, Question Summary function implementation. Details of tasks assignment and completing process could see in https://github.ncsu.edu/csc510-fall2019/CSC510-15/projects

Below is our record for task completion at the end of iteration 1

| Task Name| Assigned | Points |  Task Category | Status(Oct 23) | Status (Oct 25) | Status (Oct 31) | Status (Nov 1st)
| ---------|----------|--------|--------------- | -----------------| ----------------| ----------------| ----------------
| Find training dataset | Pei Liu | 2 | Predictive Model |To DO | In progress | Complete |Complete
| Clean and Preprocess training data | Pei Liu | 3 | Predictive Model | To Do | In progress| Complete |Complete
| Conduct Feature Engineering for data | Ziwei Wu | 3 | Predictive Model |To Do | In progress | In progress |Complete
| Explore different machine learning algorithms, train offline predictive Model |Ziwei Wu| 4 | Predictive Model | To Do | In progress| In progress |Complete
| Integrate trained offline model to Bot service | Pei Liu | 3 | Predictive Model |To Do | In progress | In progress |Incomplete
| Find and Learn how to use StackOverflow API Key and page through results | Linfeng Zhou | 4 | StackOverFlow API |To Do |In progress| Complete |Complete
| Implement StackOverFlow APIs and Interfaces | Linfeng Zhou | 4 | StackOverFlow API |To Do |In progress| In progress |Incomplete
| Update summary function, get problems list | Yuan Xu | 3 | Bot implementation | To Do |In progress |Complete |Complete
| Implement Stack Overflow APIs about question solution | Yuan Xu | 5 | StackOverFlow API |To Do |In progress |In progress|Incomplete 


#### Scrum meeting 1 
Date: Oct 25th

In this meeting, we discussed remaining tasks, refined story board and assigned tasks to each team member.

First, we add cards on Github in the link and each person is assigned equal points and tasks. 

Linfeng asked: "What's the desired process of implementing StackOverFlow API?"
we discussed several steps and found there is a list of interfaces and APIs in this link: https://api.stackexchange.com/docs, so we decided to use this link as a reference link. 

Finally we make an agreement on the next meeting time, which is next Wednesday night. 

We rescheduled the meeting to Thursday night. 

#### Scrum meeting 2
Date: Oct 31st

This meeting is for progress updating. Each developer updated his/her current achievements.

#### QuestionTagModel part: ####

Ziwei and Pei worked collaboratively for the question tag predictive model. Ziwei shared the dataset of StackOverFlow. Pei collected useful resources for our question predictive models and already finished the first stage of data preprocessing. Pei is going to begin feature engineering as next step. Ziwei begun to explore the machine learning algorithms which can be used for the model and try to figure out input format from slack and how to convert them input the predictive model. 

#### StackOverFlow API part: ####

Linfeng and Yuan worked on implementing the APIs. Yuan shared how to use the API of StackOverFlow. Linfeng discussed a framework of the implementation in the project and proposed a plan about how to achieve it. Yuan presented some improvements of the framework. 

Meeting Schedule:

We plan to have the initial demo on Nov 5th. 

## Iteration 2

#### WorkSheet Record ####
**Nov 1st**:
After the first iteration, Predictive Model part is almost done. StackOverFlow API are in progress. We assigned our tasks for iteration 2.

| Task Name| Assigned | Points |  Task Category | Status
| ---------|----------|--------|--------------- | -------
| Improve predictive model | Ziwei | 3 | Predictive Model | In progress
| Integrate trained offline model to Bot service | Pei Liu | 3 | Predictive Model |In progress
| Implement StackOverFlow APIs and Interfaces | Linfeng Zhou | 4 | StackOverFlow API | In Progress
| Implement Stack Overflow APIs about question solution | Yuan Xu | 5 | StackOverFlow API | In Progress

**Nov 3th**:

All separate functions were finished. StackOfOverflow API part was done. The first version of trained offlined model was done. 

**Nov 4th**:

Developers met together to intergrate each part together. Since we defined interfaces well at the beginning, it was relatively easy for us to integrate each functionalities together. We spent about 2 hours to set everything done.

| Task Name| Assigned | Points |  Task Category | Status
| ---------|----------|--------|--------------- | -------
| Improve predictive model | Ziwei | 3 | Predictive Model | Complete
| Integrate trained offline model to Bot service | Pei Liu | 3 | Predictive Model |Complete
| Implement StackOverFlow APIs and Interfaces | Linfeng Zhou | 4 | StackOverFlow API | Complete
| Implement Stack Overflow APIs about question solution | Yuan Xu | 5 | StackOverFlow API | Complete

### Practice
As what we discussed above, we followed "scrumban" methodology.
* Story and kanban board: https://github.ncsu.edu/csc510-fall2019/CSC510-15/projects/1

What's more, we implemented a collary practice: **Shared Code**, feature driven development and team continuity. On Oct 31st meeting, Ziwei found something wrong when she was pushing code to Github and the whole group identified what the conflict was and then fixed it. Until the team has developed a sense of collective responsibility, no one is responsible and quality will deteriorate. From then on, we got to know that some techniques like pair programming and continuous integration are interesting to try to avoid individual conducts.



