# recordpoint-tech-task

## Description
An application to satisfy the criteria describe in the RecodPoint Tech Task.

## Requirements
High-level: Using automation we want to spin up an environment which will allow us to connect to a web server on port 80 or 8080 and serve a bit of simple HTML content from a data storage source. You will be required to write a small application in the language/framework of your choice to connect to the database, query it, and return the result to the user. 

## Criteria
Developed within a git repository with frequent commits: 
*	Automated way to spin up/down single machine environment (vagrant, docker compose, minikube etc) 
*	OS installation/configuration (Windows or Linux, any versions) 
*	Configuration management (Chef/Puppet/Ansible, Dockerfile or kube deployment files) to install and configure applications 
*	Installation of a web tier and data tier (your choice, e.g. NGINX/Apache/IIS, MySQL/PostgreSQL/Redis/etc) 
*	Running a simple web application to query and return data 

## Process
Please establish a git repository from the beginning and demonstrate frequent commits. We would like to be able to spin up the environment using a single command (eg. `vagrant up` or `docker-compose up` or `kubectl apply -f ...`. We should only have to then connect to the instances IP address with a browser to see the resulting data returned. Finally, we recommend you spend a maximum of 3 hours on this activity, however you may spend longer if you wish. We would like to see your progress throughout that time period as the stack is developed.

## Usage
This Flask application with a PostgreSQL database will be run using `docker-compose up`. Navigate to http://localhost:8080 and sign your name. Your name will be written to the database and displayed on the page.