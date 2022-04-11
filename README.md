# Dns server admin

Basically the main idea here was to build a backend api for our PowerDNS server.
Besides that we needed to have another api to manipulate the DNS records.

## Dependencies
- `docker`
- `docker-compose`

## Running it
- `docker-compose up --build`

## Using it
DISCLAIMER: I'm not a frontend person so I only created a simple page to insert/delete/list the records.
You can access the app frontend on your `localhost:5000`

### API
POST /records
Body:
```json
{
  "qtype": "A",
  "qname": "test.kinexon.com.",
  "content": "10.1.2.3",
  "ttl": 0
}
```
Response:
```json
[
  {
    "qtype": "A",
    "qname": "test.kinexon.com.",
    "content": "10.1.2.3",
    "ttl": 0
  }
]
```

GET /records
Response:
```json
[
  {
    "qtype": "A",
    "qname": "test.kinexon.com.",
    "content": "10.1.2.3",
    "ttl": 0
  },
  {
    "qtype": "A",
    "qname": "test.another.com.",
    "content": "10.1.2.10",
    "ttl": 0
  }
]
```

PUT /records/{record_id}
Body:
```json
{
  "qtype": "A",
  "qname": "test.kinexon.com.",
  "content": "10.1.2.3",
  "ttl": 0
}
```
Response:
```json
[
  {
    "qtype": "A",
    "qname": "test.kinexon.com.",
    "content": "10.1.2.3",
    "ttl": 0
  }
]
```

DELETE /records/{record_id}
Response:
 ```json
 [{record_id}]
```

### PowerDNS Endpoint
Here I only use the fields `method`, `qtype` and `qname`. 
But the api allows more parameters since it follows this basic format, it will only ignore the extra fields.

POST /dns
```json
{
  "method": "lookup", 
  "parameters": {
    "qtype": "A",
    "qname": "test.kinexon.com.",
    "remote": "192.0.2.24",
    "local": "192.0.2.1",
    "real-remote": "192.0.2.24",
    "zone-id": -1
  }
}
```


## About the code
I'll list here what libraries I used for this project and the motivation behind it.
- `Flask`
  I chose flask because it is a quite simple framework that allows you to use its resources separately and build an structure by your own. 
  Different from Django that creates an structure for you and use your code inside it (you can change it? yes, but its no so easy).
  In order to avoid boilerplate from the web framework, with flask you can build your own tools or import some of it.
- `blueprint`
  Since I create the application in this approach of modules by each entity, blueprint is a great tool to organize the routes and register it in the same application
  context.
- `Pytest`
  I could test all of it with the `unittest` of python native library but rather use pytest to facilitate the work with fixtures and to find the test files. 
- `SQLAlchemy`
  When you have to work with some database and flask, in my opinion, sqlalchemy is the best ORM. It is easy to use because it abstract the sql language for python code
  (in most commom cases), a very mature tool even to compare with the Django ORM.

## The code design
I tried to split the problem in two domains: the records and the powerdns. Basically in the records module we have all the CRUD that our Frontend is going to use and
the Powerdns module handle the PowerDNS server requests/queries. 
Then I have used the mvp approach to organize each of them and implemented the `service` layer to write the business logic. For a more complexe project I would have
implement some `repository` to handle all the database logic between the services and the api or external modules.

I have skiped almost all fields validation for this project because of the time I had available. Anyways I let some TODOs in the code so I could implement it latter.
