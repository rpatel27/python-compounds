# Compounds list
Web service to get compounds data thur API calls and store them into local database.

## Docker Deployment:

### To deploy docker containers, run this from project's root:
```Linux Kernel Module
$ docker-compose up -d --build
```
### Check the running docker containers:
```Linux Kernel Module
$ docker ps
```
OR
```Linux Kernel Module
$ docker-compose images
```

### To get all the compounds data from API and store in database table:
```Linux Kernel Module
$ docker exec -it {CONTAINER_ID} python manage.py get_compounds
```

OR

```Linux Kernel Module
$ docker-compose exec web python manage.py get_compounds
```
### To list the compounds data from database table:
<b>NOTE:</b> Data is trimmed to 10 chars if the length is greater than 13 chars
```Linux Kernel Module
$ docker exec -it {CONTAINER_ID} python manage.py list_compounds
```

OR

```Linux Kernel Module
$ docker-compose exec web python manage.py list_compounds
```

## Flask:
The Flask app is running at http://127.0.0.1:5000 <br>
Once the data is loaded into database table, the above URL also shows untruncated data.
<br><br>

## Turn off Docker containers: 
Run this from project's root:
```Linux Kernel Module
docker-compose down -v
```