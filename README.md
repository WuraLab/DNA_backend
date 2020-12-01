# DNA_back-end

### Debt Notification Application
**Manage all your loans with a personal loan tracker.**

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/49aa75c6402d45019082dd8280abaa09)](https://app.codacy.com/gh/WuraLab/DNA_backend?utm_source=github.com&utm_medium=referral&utm_content=WuraLab/DNA_backend&utm_campaign=Badge_Grade_Dashboard)

[Personal Loan Application](https://nigeria-api.netlify.app/) • [API Documentation](https://documenter.getpostman.com/view/6711768/T1DjjKXv) 

### Contents

- [DNA_backend](#dna_backend)
  - [Debt Notification App](#debt-notification-app)
  - [Contents](#contents)
  - [About](#about)
  - [Getting Started](#getting-started)
- [USAGE](#usage)
  - [Set up the backend  locally](#set-up-the-backend-locally)
    - [Fork the Repo](#fork-the-repo)
    - [Clone the repository](#clone-the-repository)
    - [Install all dependencies](#install-all-dependencies)
    - [To start the App and run locally](#to-start-the-app-and-run-locally)
    - [Setting it using docker-compose](#setting-it-using-docker-compose)
  - [To see the application live](#to-see-the-application-live)
- [Stack](#stack)
- [Community](#community)
- [Top-level directory layout](#top-level-directory-layout)
- [Contributing](#contributing)

### About
DNA is an open-source project which was initiated at Automation Cube(Wuralab).
It's a personal loan tracker with mobile client, it aims to solve innefficient tracking and payments of loans by applying  digital documentation and tracking of loan records.
Thus  an individual is well aware  of how much debt they've incurred or have given out;  and the further details as capital, interest,expiry date and all payments asscociated with the loan can be easily retrieved and updated conveniently. Notifications can also be sent to the phone number, push notifications and  emails depending on user needs. 
This app could be Used by Individulas and Agencies who want to track their loan record through a smart process 
😁.

### Getting Started
// Some Information

## Usage
Set up the back-end To make use of the API; 

There are two ways to set it up
- Setting it up locally 
- Setting it using docker-compose



### Set up the back-end  locally


The project uses environment variables for configuration, which starts with DEV_DATABASE_. To configure the connection to our database, we need to specify the DB name, user, password, and host. In the root project folder create a file called ```.env``` and fill it with the content in the ```.env.example``` file:
```
SECRET_KEY=_37@a5jgf3g)5+n4*5lg-0j8jr_sb7+w707uo)oclh=jd
RESETPASS_URL=localhost:3000
DEBUG=false
ALLOWED_HOSTS=localhost


DATABASE_NAME=dnadb
DATABASE_USER=postgresuser
DATABASE_PASSWORD=postgresuser
DATABASE_HOST=db
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_PORT=5432

FACEBOOK_SOCIAL_CLIENT_ID=3296313279158218337
FACEBOOK_SOCIAL_SECRET=f63d610c89cwe1317fdea68c13ebf493ce

GOOGLE_SOCIAL_CLIENT_ID=45970062485da2-uf0jsku7r8e03mlu5oeahph3rqr0k1fj.apps.googleusercontent.com
GOOGLE_SOCIAL_SECRET=tRfCB1Ay5W6D2cd1dadymSaBwxn

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=debtapp@gmail.com
EMAIL_HOST_PASSWORD=gfrxcvcawjggnnedcirz
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

This method is suitable for anyone who wish to run the project locally without docker.


To run this application locally on your PC, you should have the following installed

1. [Python](https://www.python.org/downloads/)
2. [PostgreSql](https://www.postgresql.org/)
3. [Pip3](https://pip.pypa.io/en/stable/installing/)
4. [Pipenv](https://pypi.org/project/pipenv/)


### Fork the Repository

### Clone the Repository 


    git clone https://github.com/WuraLab/DNA_backend.git


### Create and Activate Virtual Environement

Using Pipenv
```
   pipenv shell
```

### Install all dependencies

Using pip3

    pip3 install -U -r requirements.txt 

### To start the App and run locally

Using Python manage.py 

    python manage.py runserver


To test the application, open your browser and type this in the Url address bar
```localhost:8000```

### Setting it using docker-compose
The application can be run using docker also, you should the following installed

1. [docker](https://www.docker.com/get-started)
2. [docker compose](https://docs.docker.com/compose/install/)

- run ```docker-compose build ``` to build the docker image
- run ```docker-compose up -d``` to run the application 

Application runs on port 8000

### Download the mobile client to see the application 

[Download the Personal Loan Tracker App]()


## Stack
Python/Django + PostgreSQLDB

## Community

If you have any questions or need help send a DM on  <a href="https://twitter.com/" alt="Twitter"><img src="https://raw.githubusercontent.com/WuraLab/NigeriaApi/sqlDump/readme/twitter-fill.svg"></a>to any of the amazing developers.

- [Peterson Oaikhenah](https://www.twitter.com/i_am_nextwebb)
- [Azeez Lukman](https://twitter.com/robogeek95)
- [Emmanuel](https://twitter.com/)

## Top-level directory layout

    📦DNA_backend
        ┗ 📦.github
            ┗ 📦workflows
                ┣ 📜ci.yml
        📦DNA
            ┣ 📜__init__.py
            ┣ 📜asgi.py
            ┣ 📜settings.py
            ┣ 📜urls.py
            ┣ 📜wsgi.py
        📦api
            ┗ 📦migrations
                ┣  📜__init__.py
            ┣ 📜__init__.py
            ┣ 📜admin.py
            ┣ 📜apps.py
            ┣ 📜models.py
            ┣ 📜serializers.py
            ┣ 📜tests.py
            ┣ 📜urls.py
            ┣ 📜views.py
        📦templates
            ┣ 📜password_reset_emai.html
            ┣ 📜password_reset_emai.txt
           
        ┣ 📜.env.example
        ┣ 📜.gitignore
        ┣ 📜Dockerfile
        ┣ 📜LICENSE
        ┣ 📜Procfile
        ┣ 📜README.md
        ┣ 📜docker-compose.yml
        ┣ 📜manage.py
        ┣ 📜requirements.txt



## Contributing

There are many ways you can contribute and help this project. Here a few ones:

* Star this Repository.
* Up vote issues with 👍 reaction so we know what's the demand for particular issue to prioritize it within road map.
* Create issues every time you feel something is missing or goes wrong.
* Provide pull requests for all open issues and especially for those with [help wanted]() and [good first issue]() labels.
