
# Github Gist Checker
## 1. Application

Python application which is checking github user gists and creates crm deal in pipedrive company.

## 2. Locally

In order to build a application locally. 

    1) Change in configuration.js file "host": "elasticsearch", to "host": "localhost"

    2) docker-compose up -d
    
You will receive 4 conteiners = gistchecker, kibana, elasticsearch, jenkins.

<img width="1212" alt="Screenshot 2021-07-30 at 01 25 04" src="https://user-images.githubusercontent.com/15733762/127573415-71eab95d-ef4b-4e5f-bfa8-3203a1aaf55b.png">

1) gistchecker is python application which runs periodically and checks github user gists and creats a deal to pipedrive

2) In kibana please create index for "pipedrive_test" and you will receive all the application logs.

<img width="1680" alt="Screenshot 2021-07-30 at 01 34 49" src="https://user-images.githubusercontent.com/15733762/127574176-fffe9e03-da06-44c3-9e96-2205a2748660.png">

3) Please log in to jenkins with "admin" account and you will have access to two pipelines.

<img width="1680" alt="Screenshot 2021-07-30 at 01 32 42" src="https://user-images.githubusercontent.com/15733762/127574001-ed270ebe-27b2-4c20-af01-7b9a7d932b91.png">

Pipeline gist-image is a pipeline which will build a docker image and push it to docker hub. 

Pipeline gist-application-deploy is a pipeline which will create a cf stack with a latest succesfull gist-image tag and execute this changeset


## 3. Configuration

Configuration is done in configuration.json file.

## 5. Run application aws
Application can be launched into the aws via cf/gist-checker.yaml template. 

Before launching to cloud then please revert configuration changes in step1.

Change in configuration.js file "host": "localhost", to "host": "elasticsearch"

It will create a ecs with 4 the same conteiners = gistchecker, kibana, elasticsearch, jenkins.

Kibana is accessbile from "<Ec2PublicIP:5601"

Jenkins is accessible from "<Ec2PublicIP:8080"
    
