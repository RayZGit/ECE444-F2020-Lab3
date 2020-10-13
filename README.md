# ECE444-F2020-Lab4&5
## Activity
this repo is a clone of https://github.com/miguelgrinberg/flasky
- [x] Perform all development in a branch "lab4_Microservice_Experiment" in your Lab3 task
GitHub repository (you are experimenting after all). 
- [x] In addition to the code, this branch should contain a README.md file that describes how
to build and start the system (including the location of the Docker files and a screenshot of your
docker run command, Browser, and your docker image).

Docker image built shown in the following screenshot. Command: docker build -t lab4_activity .
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Week4%20and%205%20Assignment/lab4dockerbuild.PNG)
Docker run as shown in the following screenshot. Command: docker run --name lab4 -d -p 5000:5000 lab4_activity \
To check its status. Command: docker ps -a
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Week4%20and%205%20Assignment/lab4Dockerrunning.PNG)

Screenshoot for the prof of the docker image
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Week4%20and%205%20Assignment/lab4dockerdesktop.PNG)
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Week4%20and%205%20Assignment/lab4dockerImage.PNG)
- [x] Briefly summarize the differences between Docker and Virtual Machine.

# ECE444-F2020-Lab3
this repo is a clone of https://github.com/miguelgrinberg/flasky

## Activity 1
- [x] Create an empty public repository, name format: ECE444-F2020-Lab3
- [x] Create a readme file with your name and mention: this repo is a clone of
https://github.com/miguelgrinberg/flasky
- [x] Follow Chapter 3 examples and print “Hello [your name]”.
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/master/Week3%20Assignment/week3_activity1.PNG)

Screenshot of the webstite at localhost with port 5000
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Week4%20and%205%20Assignment/lab4website.PNG)
Screenshot for proof of docker image
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Week4%20and%205%20Assignment/lab4website.PNG)

## Activity 2
- [x] Reproduce example 4-7 in your repo, commit the code with reasonable commit message
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/master/Week3%20Assignment/gitlog.PNG)
- [x] Add one more field for filling in email address. Please check if the email address is an
UofT account (‘utoronto’ is a substring of the email address). If the email is an UofT
address, after submitting, the browser display the user name and the email, otherwise,
remind the user to fill in a UofT email (see screenshot below).
- [x] Submit a commit and Run the project and make a screenshot.
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/master/Week3%20Assignment/week3_activity2_stranger.PNG)
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/master/Week3%20Assignment/week3_activity2_email.PNG)
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/master/Week3%20Assignment/week3_activity2_email_error.PNG)
![alt text](https://github.com/RayZGit/ECE444-F2020-Lab3/blob/master/Week3%20Assignment/week3_activity2_email_notUT.PNG)

## Activity 3
- [x] Briefly summarize the difference between SQL or NoSQL database.
- SQL
  - SQL is a relational databse
  - SQL has structured query language with schema 
  - SQL vertically scalable 
  - Support join
  - Most support multi-threading with ACID as standard
  - Examples: MySQL, PostgreSQL, Oracle
- NoSQL
  - NoSQL is a non-relational databse 
  - NoSQL has unstructured data with dynamic schemas
  - NoSQL horizontally scalable 
  - No join
  - Most use queue for accessing data
  - Examples: MongoDB, Redis, CouchDB
  
