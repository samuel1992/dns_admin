# KINEXON DNS Server Coding Challenge

## What is this about?
This challenge is part of the KINEXON interview process for Infrastructure Engineers.
It gives you the opportunity to show us your skills, interests, motivation and how you work in general.

### Your task
With this challenge, we would like to ask you to implement a web application that serves as a configuration tool for 
DNS server records. At KINEXON, we need to manage our kinexon.com DNS zone which contains thousands of domains and IP 
addresses in a scalable and maintainable way. This configuration tool should help users to manage those records
in a user-friendly way without needing to manually edit DNS zone files on servers.
Your final solution should consist of two parts: a web frontend and a backend.

**Web frontend:**
The web frontend should show the current list of DNS records and allow the user to add, remove and modify DNS records 
dynamically. At the very minimum, it should support two types of records: 'A' records and 'CNAME' records (all other
record types can be ignored and do not need to be resolvable by the DNS server).
The frontend can be implemented in any JS framework you like and the design is totally up to your preference. It is not 
expected that you build a lot of stuff and that everything is 100% polished. Simply try to give us a glimpse of what 
we can expect from you.

**Backend**
The backend serves two main purposes.
First, it implements an HTTP API that is called from the frontend and supports adding, removing and modifying the 
DNS records. It is not expected that the DNS records are persisted through restarts, e.g. when the backend restarts,
DNS records that have previously been added may be deleted.

Second, it implements another HTTP API that is called by a PowerDNS server to transfer the DNS records from the backend 
to the DNS server. We already provide you with the running PowerDNS server and a backend skeleton that implements parts 
of this API. You can either try to refactor and extend the existing codebase or you may start from scratch with the 
programming language and framework of your choice.

### How will the solution be tested?
We will add, remove and modify DNS records through the web UI and query the running PowerDNS server using 'dig' to 
validate if the changes have been successfully synced the DNS server.

### Constraints
- The challenge is not time-boxed. You can invest as much or as little time as you want and need to. Most candidates 
spend something between two hours and one day depending on what they build.
- If your final solution requires additional setup (other than 'docker-compose up'), please document the necessary
steps in a README file.


## What is included?

### DNS server (PowerDNS)
PowerDNS is an open source DNS server with a modular structure that supports a large number of different backends. 
Those backends range from databases (e.g. PostgreSQL, MySQL) and process pipes to classic zone files and JSON HTTP APIs.
Instead of answering DNS queries directly, PowerDNS forwards incoming requests to the configured backend(s) which then 
provide the required information to PowerDNS by exchanging messages in a predefined format.

As part of this challenge we are going to use the "remote" backend type which allows connecting to a custom web backend 
through JSON HTTP requests. The PowerDNS server provided in this challenge is configured to make HTTP POST requests to 
the endpoint http://app:5000/dns (where 'app' is the DNS name that resolves to the docker container running the backend). 
Whenever the PowerDNS server receives a DNS query from a client, it posts one or multiple JSON encoded messages to this 
HTTP endpoint and expects the backend to reply with the result encoded as JSON. The message format and protocol is 
explained in more detail further below.

### App backend skeleton (NodeJS)
We provide a (not particularly well-structured) NodeJS backend that should help you to get started. This backend launches
a simple HTTP web server on port 5000 and waits for POST requests to /dns. It then parses the JSON body, decodes the 
message from PowerDNS and replies with a JSON object again. It currently implements the two methods 'lookup' and 
'getDomainMetadata' (both are required by PowerDNS) and returns a test record that resolves the domain test.kinexon.com 
to the IP address 10.1.2.3.


## Message protocol
The body of the POST request that is sent from PowerDNS to the app backend is a JSON object with two properties 
'method' (string) and 'parameters' (object), for example
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
In this case, the backend is asking for type 'A' records for the domain 'test.kinexon.com.'. The app backend should 
now reply with a JSON in the following structure
```json
{
  "result":[
    {
      "qtype": "A",
      "qname": "test.kinexon.com.",
      "content": "10.1.2.3",
      "ttl": 0
    }
  ]
}
```
This was a very basic example and the full documentation of the protocol is available on the PowerDNS website:
https://doc.powerdns.com/authoritative/backends/remote.html#api


## How to run the code?
The PowerDNS server and the NodeJS backend are shipped as Docker containers with individual Dockerfiles 
(app/Dockerfile and dns-server/Dockerfile). Additionally, a docker-compose.yml file is provided that connects the two
containers and allows them to communicate with each other.

To start the sample application, simply run 
```shell
docker-compose up --build
```

After some initial building time, this should launch two containers ('app' and 'dns-server').
The backend API is automatically exposed on your local machine on port 5000, so you should be able to access your 
backend by opening http://127.0.0.1:5000/ in your browser or by running the following curl command. 
```shell
curl http://127.0.0.1:5000/
```
Afterwards, you can make DNS queries to the dns-server using 'dig' which is included in the dns-server container.
```shell
docker exec dns-server dig @localhost test.kinexon.com +short 
```
This should print "10.1.2.3" on your console. If you query any other DNS name (besides "test.kinexon.com") the result 
should be empty.


## Hints
- For the scope of this challenge, it should be sufficient to only implement the required PowerDNS methods 'lookup' and 
'getDomainMetadata'. The result for 'getDomainMetadata' can simply be an empty array.
- To implement this challenge it is generally not required to change anything about the dns-server container but, 
of course, you can install additional debug tools into the container if you like.
