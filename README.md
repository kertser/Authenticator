# Authenticator - server application

Simple script for client-server authentication (in development)

## Table of Contents

- [Project Name](#project-name)
  - [About](#about)
  - [Usage](#usage)
  - [License](#license)

## About

This is a basic server, running containerized.<br>
- Async Server is operated at port 5000 in container "server"<br>
- MySQL db is operated at port 3306 in container "db-mysql"<br>
- Everything is orchestrated with docker-compose<br>
- GUI client for testing is available at port 8080, in separate container <br>
  (http://46.243.233.79:8080/)
  - <For the moment, the database has the following table format for the users:<br><i>
  id [int]<br>
  username [varchar(255)]<br>
  phone_number [varchar(15)]<br>
  password [varbinary(128)]<br>
  token [varbinary(128)]<br>
  registration_date [date]<br>
  last_connection_date [date]<br>
  telegram_profile [varchar(255)]<br>
  active [y/n]<br></i>

## Usage

run the Server_up.sh script on linux:<br>
-> chmod +x Server_up.sh<br>
-> ./Server_up.sh<br>
* will install the docker and docker-compose<br>
* will mount volume sdb into /mnt/data for volume storage of mysql database
* will clone the git repo and initiate the docker-compose

## License
Use at will... :)