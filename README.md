# Distinctiveness and Complexity

This project is a twitter bot built on the Tweepy library that uses Python and developed on the web with Django using the tweeter API, so it is very important to install them beforehand, where you can schedule the dates you want to publish your tweets. They can work together from different accounts or individually.

It should be noted that for its use, you must have a tweteer application to use the access codes that tweeter provides us.

## Features

1. Authentication system:
	- User register.
	- Login.
	- Logout.
	- Smart detection for when there are no records under your id.
	
![](https://i.imgur.com/AnKHO11.png)

2. Records management: the management of the bot has a registry of tweets that contain the characteristics.
	- tweet title.
	- tweet content.
	- tweet date which has an integrated calendar.
	
![](https://i.imgur.com/OVKrqZN.png)

![](https://i.imgur.com/53z4v5o.png)

> 	These records (tweets) are saved with the date on which you want to be sent to tweeter, these records also have two actions, "Edit" if desired and "Send" for the home section, if we go to all.

3. Mentions system: The mentions system is responsible for collecting the last 3 tweets that have been mentioned to us, only the name of the user who mentioned us will be shown as relevant information, but clicking on the record will take us to another tab with the complete information.

## Usage

First we clone the repository

Completed the previous step and located in the root of the project in the console, install all the dependencies with the following command:

**`pip install -r requirements.txt`**

Once the necessary dependencies are installed, the database must be migrated, entering this first code in the console:

**`python manage.py makemigrations`**

and then:

**`python manage.py migrate`**

if you have trouble doing the migrations, try **`python manage.py makemigrations daily`** subsequently **`python manage.py migrate`**

Finally, run **`python manage.py runserver`** to start the web application.

# Documentation

The "TweeterDaily" project has the application called "daily" previously configured.

In the file "models" are the two models with which the application works "User" and "Entry" (the latter is the model of tweets).

admin has registered the models to be treated from the Django administrator and the forms file converts and adds characteristics of the Entry model in a form through the Django classes.

Finally, the "views" file maintains a large part of the information about the management of the page, it maintains most of the logic of the app and there are the access keys to access the tweeter api, so there will be clearly the variables to which we have to assign them. You must request the access codes from the twitter page and place them in the corresponding variables, (if you do not do this step, the application will not work).

![](https://i.imgur.com/4634NmJ.png)

### In the page "home" we will obtain:

- Tweets in which the date provided coincides with the date the application is being used will be shown in "Daily Tweets" and will have two actions: Send or Edit, if there is no match it shows a nice message. When sending a tweet the page will reload and it will be removed from the records

- It will also be in the "New daily" button which directs us to a form to create a new tweet.

- Finally the Mentions section that I already mentioned its use in the features.

![](https://i.imgur.com/88fR2YX.png)

## To end

In the navigation area, the "Tweets" section will show us all the tweets that we have registered with 3 possible options: Send, Edit or Delete

![](https://i.imgur.com/7Ded5Lg.png)
