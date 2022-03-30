# Hackernews clone REST API

## Description of the project

This is a hackernews clone RESTful API, where users can view, create and delete posts, upvote and delete upvotes for posts, comment on posts and delete them as well.


## Languages and tools


<img align="left" alt="Python" width="50px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />
<img align="left" alt="Django" width="50px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/django/django.png" /> </br> </br>
<br> <br>
Also there were used such tools as Black formatting, flake8 linter check, djoser (with jwt integrated), decouple (for dealing with environment variables)
and the library named apscheduler, which is great tool for dealing with periodic tasks.
You can find documentation here - https://apscheduler.readthedocs.io/en/3.x/ <br>
In this project apscheduler was used to reset number of upvotes count every day in 9:00 AM
<br> <br>

## USAGE

#### First you should clone the repository into your local machine

```shell
git clone https://github.com/hiki0505/Hackernews_clone_REST_API
```

#### WARNING: there are environment variables, which are placed in .env file
Just create .env file with following structure
```
SECRET_KEY=<put your custom secret key here>
DEBUG=<set it to True or False>
POSTGRES_DB=<postgres database name>
POSTGRES_USER=<postgres username>
POSTGRES_PASSWORD=<postgres password>
```
and place it in main folder (where manage.py is placed)

#### After that, follow the commands below to build a container using django and postgres images
```shell
# make sure to change to the root directory of project, where docker commands will run
$ cd Hackernews_clone_REST_API
# building the container with following images and settings, specified in Dockerfile and docker-compose.yaml files
$ docker-compose build
# command above will migrate database and create superuser, where you will be needed to specify password
$ docker-compose run django bash -c "python manage.py migrate && python manage.py createsuperuser --email testadmin@example.com --username testadmin"
# then you just run your container and open the link http://127.0.0.1:8000/
$ docker-compose up
```

# POSTMAN COLLECTION AND API ENDPOINTS
After entering the REST API, you have bunch of api endpoints, which allows you to interact with users, posts, comments and upvotes.
### API ENDPOINTS 
<ul>
  <li>
    <b> /api-auth/users </b>   # For creating a new user
  </li>
  <li>
    <b> /api/jwt/login </b>   # For login, where you get token and use it in headers (Authorization) with JWT prefix
  </li>
  <li>
    <b> /api/user-list </b>   # For view users list and create user
  </li>
  <li>
    <b> /api/user-activity </b>   # For view user activity (number of upvotes and comments they made)
  </li>
  <li>
    <b> /api/posts </b>   # For view posts and create (only for authenticated users) posts
  </li>
  <li>
    <b> /api/posts/post_id </b>   # For retrieve particular post, and delete them (if you are the post owner)
  </li>
  <li>
    <b> /api/posts/post_id/like </b>   # For upvoting or deleting upvote for particular post (if you are authenticated)
  </li>
  <li>
    <b> /api/posts/post_id/comment </b>   # For creating comments to the particular post
  </li>
  <li>
    <b> /api/comments/comment_id </b>   # For view or delete (if you are owner of the comment) particular comment to the particular post
  </li>
</ul>

### POSTMAN COLLECTION

Below you will find the POSTMAN collection link, where you can test API endpoints, with two enviroments, local (or dockerized) and production (heroku), 
where environment variables are already used. <br>
link: https://www.getpostman.com/collections/0aa539c1e094671ba3f9 <br>
<b> Note: </b> Make sure that you go through the endpoints one by one, because some of the variables are set dynamically on pre and post requested scripts, otherwise you can face errors

# HEROKU DEPLOYMENT

API was deployed to Heroku. The link is following - https://hackernewscloneapp.herokuapp.com/



