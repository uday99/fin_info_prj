# fin_info_prj
CRUD Operations

firstly install all the packages in requirements.txt



Use Database postgres

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fin_info',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}







Employee Crud operations


TO create employee
====================

URl=http://localhost:8000/create/emp/
payload in post
===================

{
"name": "jay kumar",
"email":"jay2@gmail.com",
"age": 26,
"gender": "male",
"phoneNo": "9640308823",
"addressDetails": {
"hno": "2-15-858",
"street": "ggiereri",
"city": "Hydderabad",
"state": "Telangana"
},
"workExperience": [
{
"companyName": "xyz",
"fromDate": "20-05-2019",
"toDate": "20-09-2021",
"address": "Madhapur"
}
],
"qualifications": [
{
"qualificationName": "MBA",
"fromDate": "20-05-2021",
"toDate": "20-05-2023",
"percentage": 89
}
],
"projects": [
{
"title": "xyz",
"description": "description of the project"
}
],
"photo": ""


}

GET api

=============



TO GET List of all the Employees


url: http://localhost:8000/list/emp/


To Get only specific employee

url:http://localhost:8000/one/emp/1/



PUT Method to Update
======================


url:http://localhost:8000/update/emp/1/


payload


{
"name": "jay kumar",
"email":"jay2@gmail.com",
"age": 26,
"gender": "male",
"phoneNo": "9640308823",
"addressDetails": {
"hno": "2-15-858",
"street": "ggiereri",
"city": "Hydderabad",
"state": "Telangana"
},
"workExperience": [
{
"companyName": "xyz",
"fromDate": "20-05-2019",
"toDate": "20-09-2021",
"address": "Madhapur"
}
],
"qualifications": [
{
"qualificationName": "MBA",
"fromDate": "20-05-2021",
"toDate": "20-05-2023",
"percentage": 89
}
],
"projects": [
{
"title": "xyz",
"description": "description of the project"
}
],
"photo": ""


}



DELETE API

url:http://localhost:8000/delete/emp/

payload:

{
    "regid":2
}

























