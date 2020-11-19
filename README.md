# DNA_backend
## Debt Notification App
**Manage all your loans with a personal loan tracker.**

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/49aa75c6402d45019082dd8280abaa09)](https://app.codacy.com/gh/WuraLab/DNA_backend?utm_source=github.com&utm_medium=referral&utm_content=WuraLab/DNA_backend&utm_campaign=Badge_Grade_Dashboard)

# Nigerian API Application


[Website](https://nigeria-api.netlify.app/) • [Docs]() • [Example](#examples)
## Contents

- [About](##About)
- [Getting Started](##getting-started)
- [Usage](#USAGE)
- [Set up the backend](##Set-up-the-backend)
- [Set up backend](##Setting-it-up-locally)
- [Community](#community)
- [Top-level directory layout](#Top-level-directory-layout)
- [Contributing](#contributing)

## About
Nigeria API is an open-source project which was initiated at Automation Cube(wuralab)

The Projects aims at solving the problem of difficulties to find API that exposes DATA about Nigeria. Sometime we have project to work on where we need to display DATA about nigeria, such as University in nigeria, industry in nigeria.

The end goal of this project is to have enough DATA on nigeria which can be accessed through an API.

We want to take away the stress faced by developers when working on projects that involves or needs nigeria data.

## Getting Started


# USAGE
1. Set up the backend

To make use of the API, There are two ways to set it up
2. Setting it up locally 
3. Setting it using docker-compose

## Set up the backend
 Let's start by setting up a database with some sample data. We'll use PostgreSQL and our example e-commerce dataset for this tutorial. You can download and import it by running the following commands.

```
$ curl <https://github.com/WuraLab/NigeriaApi/blob/sqlDump/output.sql> > outpput.sql
$ createdb <DBNAME>
$ psql --dbname <DBNAME> -f output.sql
```
For example,

```bash
$ curl <https://github.com/WuraLab/NigeriaApi/blob/sqlDump/output.sql> > outpput.sql
$ createdb nigeriaapidb
$ psql --dbname nigeriaapidb -f output.sql
```

The project uses environment variables for configuration, which starts with DEV_DATABASE_. To configure the connection to our database, we need to specify the DB name, user, password, and host. In the root project folder create a file called ```.env``` and fill it with the content in the ```.env.example``` file:

## Setting it up locally

This method is suitable for anyone who wish to run the project locally without docker.

To run this application locally on your PC, you should have the following installed

1. [Node js](https://nodejs.org/en/)

2. [PostgreSql](https://www.postgresql.org/)


### Fork the Repo

### Clone the repository 

    ```
    git clone https://github.com/<username>/NigeriaApi.git
    ```



### Install all dependencies

Using npm

    ```
    npm install
    ```


### To start the App and run locally

Using node

    ```
    npm start
    ```    
or nodemon(make sure you have nodemon installed on your local sysytem, perhaps installed globally using)

    ```
    npm install -g nodemon
    ```    
then you run the app with 

    ```
    npm run dev
    ```    
By default, the applictaion is running on PORT 3000, this port can be changed in ```api/bin/www``` file on line 8.

To test the application, open you browser and type this in the address bar
```localhost:3000```

### Setting it using docker-compose
The application can be run using docker also, you should the following installed

1. [docker](https://www.docker.com/get-started)
2. [docker compose](https://docs.docker.com/compose/install/)

run ```docker-compose build .``` to build the docker file.
run ```docker-compose up -d``` to run the application

Application runs on port 3000

## To see the application live

[https://nigeria-api.netlify.app/](https://nigeria-api.netlify.app/)


# Stack
JavaScript 

## Community

If you have any questions or need help send a DM on  <a href="https://twitter.com/" alt="Twitter"><img src="https://raw.githubusercontent.com/WuraLab/NigeriaApi/sqlDump/readme/twitter-fill.svg"></a>to any of the amazing developers.

- [Fawas](https://www.twitter.com/fawas_ola)
- [Isreal](https://twitter.com/Aminu_Israelb)
- [Suen](https://twitter.com/Eazyjazz02)
- [Adefemi](https://www.twitter.com/daycrawller)

# Top-level directory layout

    📦NigeriaAPI
        ┗ 📦.github
            ┗ 📦workflows
                ┣ 📜ci.yml
        📦.vscode
            ┣ 📜settings.json
        📦api
            ┗ 📦bin
                ┣ 📜www
            ┗ 📦config
                ┣ 📜config.js
            ┗ 📦controllers
                ┗ 📦email
                    ┗ 📦templates
                        ┣ 📜signup.html
                    ┣ 📜helper.js
                ┣ 📜user.js
            ┗ 📦helpers
                ┣ 📜authHelper.js
                ┣ 📜mailer.js
                ┣ 📜validationSchema.js
            ┗ 📦middlewares
                ┣ 📜validationMid.js
            ┗ 📦migrations
                ┣ 📜20200711012227-create-users.js
            ┗ 📦models
                ┣ 📜index.js
                ┣ 📜users.js
            ┗ 📦routes
                ┣ 📜index.js
            ┗ 📦test
                ┣ 📜test.js
        ┣ 📜app.js
        ┣ 📜.env.example
        ┣ 📜.eslintrc.js
        ┣ 📜.gitignore
        ┣ 📜.sequelizerc
        ┣ 📜package.json
        ┣ 📜package-lock.json
        ┣ 📜README.md


## Contributing

There are many ways you can contribute and help this project. Here a few ones:

* Star this repo.
* Upvote issues with 👍 reaction so we know what's the demand for particular issue to prioritize it within road map.
* Create issues every time you feel something is missing or goes wrong.
* Provide pull requests for all open issues and especially for those with [help wanted]() and [good first issue]() labels as those are out of Cube.js Core Team roadmap scope.
