# gist-check

# Github Gist Checker
## 1. Github API & Pipedrive API

Python application which is checking github user gists and creates crm deal in pipedrive company.

## 2. Launch cloudformation template fail.

In order to build a docker image run the following command from the projects root directory

    docker build -t gist-checker .

## 3. Configuration

## 5. Run application locally
### 5.1 Docker image
1.Build iamge locally/ see step "Build docker image" **OR** Pull latest image from public remote repository 
   
    docker pull testgistpipe/gist-checker
 
   

## 7. Provisioning in the AWS
Application can be provisioned into the AWS cloud using AWS Cloudformation template located in `cloudformation/template.yaml`. <br>
    
