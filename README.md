# How to host your python flask website free in Heroku 🔥
## What is Flask?

Flask is a web application framework written in Python. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects. This post revolves around how to deploy a flask app on Heroku. To demonstrate this, we are first going to create a sample application for a better understanding of the process. 

## Prerequisites: 

- Python
- pip
- Git
- VS code(editor)

**STEP 1 :** Let’s create a simple flask application first and then it can be deployed to heroku. Create a folder named ["eagle_programming"](https://www.instagram.com/eagle_programming/?hl=en) on your computer. Open that folder in VS code editor and create a “Procfile” and write the following code.


![image](https://user-images.githubusercontent.com/70682152/171404121-4006618e-262e-4355-a4f0-75d818b8739c.png)


**STEP 2 :** Create “requirements.txt” and write the following requirements.


![image](https://user-images.githubusercontent.com/70682152/171404234-a58f25e6-66a8-4ad0-b547-1d640825db36.png)



**STEP  3:** Create app.py and write the following code.

![image](https://user-images.githubusercontent.com/70682152/171404294-d061fc39-b88a-43c6-8e1d-dcccaa0e7433.png)



**STEP 4:** Initialize an empty repo, add the files in the repo and commit all the changes.

![image](https://user-images.githubusercontent.com/70682152/171404352-eae4e047-768a-4519-a509-6f8ca0a96555.png)



**STEP 5 :** Create account in [Heroku](https://dashboard.heroku.com/login) and Login to heroku CLI using "heroku login" command and Now, Create a unique name for your Web app.

![image](https://user-images.githubusercontent.com/70682152/171404418-aa5aed61-603e-499c-9b28-d53167ab69e6.png)



**STEP 6:** Push your code from local to the heroku remote. 
![image](https://user-images.githubusercontent.com/70682152/171404477-8cbb02ee-80cd-4f79-a219-eb181bcd5f00.png)


Finally, our web app will be deployed on https://eagleprogramming.herokuapp.com/
 
