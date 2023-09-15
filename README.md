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

## Usage

run the Server_up.sh script on linux:<br>
-> chmod +x Server_up.sh<br>
-> ./Server_up.sh<br>
* will install the docker and docker-compose<br>
* will mount volume sdb into /mnt/data for volume storage of mysql database
* will clone the git repo and initiate the docker-compose

## License
Use at will... :)