# DNS Server Admin

## Main requirements
The main goal is to make a tool to adminitrate the dns server records.
- It should allow to insert A records and CNAME records
- It doest need to persist the DNS records after the server restarts
- It has two APIs: one to be used by the frontend app and another to be used by the PowerDns server

## TODOS
- Setup the project initial structure #DONE
- Api to CRUD the DNS records via Frontend #DONE
- Api to query the DNS records via PowerDNS
  - filter method 'lookup':
    - filter by qtype == 'SOA'
      - retrieve from db the record with qname requested
      - return Array[Object(qtype:'SOA', qname:record.qname, content:record.content, ttl:)]
    - filter by qtype 'ANY' or 'A':
      - retrieve from db the record with qname requested
      - return Array[Object(qtype:'A', qname:record.qname, content:record.content, ttl:)]
  - filter method 'getDomainMetadata'
    - return an empty array []
- Add fields validation in model layer
- Add fields validation in schema layer
- Frontend to manage the records through the API

### Scratch

Entities:
  - dns record
    - qtype: Enum(A, CNAME)
    - qname: String
    - content: String (IP format)

Modules/Domains:
  - record: CRUD dns records
  - power_dns: implements the endpoints required by powerdns and comunicate with our modules

app/
  - record/ # Place the unittests within the model
    - model.py
    - schema.py
    - api.py
    - service.py
  - power_dns/
    - api.py
    - service.py
  app.py # Run the python Flask app
  config.py # Stores all the configuration by the project (mostly got from env)
  extensions.py # Setup the database configuration to avoid ciclic import on the files
  fixtures.py # Create some pytest fixtures to our unittests
