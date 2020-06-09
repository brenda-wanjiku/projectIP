# Award

## Author
https://github.com/brenda-wanjiku/projectIP

## Description
An application that allows a user to post a project and be reviewed by other users.


### User Stories:
1. View posted projects and their details
1. Post a project to be rated/reviewed
1. Rate/ review other users' projects
1. Search for projects 
1. View projects overall score
1. View my profile page
1. To access admin page use the following credentials: Username: brendawanjiku29, password: brenda29

## Technolgies used
1. HTML and CSS
1. Python
1. Django
1. Postgres
1. Heroku
1. Git and GitHub

## Set up and Installation
### Prerequisites
The user will require git, django, postgres and python3.8 installed in their machine. To install these two, you can use the following commands

1. git
```$ sudo apt install git-all```

2. python3.8
```$ sudo apt-get install python3.8.```

3. django
``` pip install django```

4. postgres
```$ sudo apt-get install postgresql postgresql-contrib```

### Installation
1. To access this application on your command line, you need to clone it 
`https://github.com/brenda-wanjiku/projectIP.git`
2. You can then run the server with:
`python3.6 manage.py runserver`
3. You can make changes to the db with
`python3.6 manage.py makemigrations project`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test project`


### Creating the virtual environment
* Use the following commands in your terminal to create virtual environment

    $ python3.8 -m venv --without-pip virtual

    $ source virtual/bin/env

    $ curl https://bootstrap.pypa.io/get-pip.py | python



## Live Site
* Can be accessed here https://brenda-project.herokuapp.com/

* To log in as an admin you can use the following credentials:
      username : brendawanjiku29 and password: brenda29

## API calls
1. Use the following api end point to generate a token
    
    *Note all end points require authenticated users to access*

    * for the local environment
        `http://127.0.0.1:8000/api-token-auth`
    * To get user profiles 
        GET: `http://127.0.0.1:8000/api/profiles`
    * To get projects
        GET: `http://127.0.0.1:8000/api/projects`

## Author's Contact
If you need any clarifications or have feedback on this project , contact the author at brendawanjiku@gmail.com


## Licence
This project is under the [MIT]https://raw.githubusercontent.com/brenda-wanjiku/projectIP/master/LICENSE licence
