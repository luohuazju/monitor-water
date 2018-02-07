

Run the Project

python manage.py runserver 

Curl the RESTful 

curl -H 'Accept: application/json;indent=4' http://localhost:8000/users/

WaterRecord Module

>curl http://localhost:8000/api/waterrecords/

>curl -X POST http://localhost:8000/api/waterrecords/ -d "waterName=MableFalls&released=true&releasedDate=2018-01-01"

>curl -X DELETE http://localhost:8000/api/waterrecords/1 

>curl -X PUT http://localhost:8000/api/waterrecords/2 -d "waterName=MableFalls&released=false&releasedDate=2018-01-01"