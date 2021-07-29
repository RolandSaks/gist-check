
# Github Gist Checker
## 1. Application

Python application which is checking github user gists and creates crm deal in pipedrive company.

## 2. Locally

In order to build a application locally

    docker-compose up -d
    
You will receive 4 conteiners = gistchecker, kibana, elasticsearch, jenkins.

(<img width="1212" alt="Screenshot 2021-07-30 at 01 25 04" src="https://user-images.githubusercontent.com/15733762/127573415-71eab95d-ef4b-4e5f-bfa8-3203a1aaf55b.png">




## 3. Configuration

## 5. Run application locally
### 5.1 Docker image
1.Build iamge locally/ see step "Build docker image" **OR** Pull latest image from public remote repository 
   
    docker pull testgistpipe/gist-checker
 
   

## 7. Provisioning in the AWS
Application can be provisioned into the AWS cloud using AWS Cloudformation template located in `cloudformation/template.yaml`. <br>
    
