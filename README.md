# Github Gist Checker 

<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" align="right"
     alt="logo" width="120" height="120">

Gist-checker is a python application which checks periodically github user gists. Based on found gists, the application will
also create a new CRM deal in pipedrive.



### How to run application locally

<details><summary><b>Show instructions</b></summary>

1. Clone the repo:

    ```sh
    $ git clone https://github.com/RolandSaks/gist-check.git
    ```

2. Add the `username` value who you want to check and the `interval` time in `configuration.json`:

    ```diff
    {
      "gists": {
        "monitor": {
           "usernames": [
             "RolandSaks",
             "yournewgithubuser"
      ],
       "interval": 15 
      }
    }
    ```
    
3. Add correct pipedrive `PIPEDRIVE_API_KEY` and `PIPEDRIVE_COMPANY` in `docker-compose` fail.

    ```diff
    command: sh wait_to_start.sh
    environment:
        - WAIT_COMMAND=timeout 300 bash -c "until curl --silent --output /dev/null http://elasticsearch:9200/_cat/health?h=st; do printf '.'; sleep 5; done; printf '\n'"
        - WAIT_START_CMD=python3 main.py
        - WAIT_SLEEP=60
        - WAIT_LOOPS=10
   +    - PIPEDRIVE_API_KEY=yourapikey
   +    - PIPEDRIVE_COMPANY=yourcompanyname
    links:
     - elasticsearch
     - kibana
    ```    

4. Run the application.
    ```sh
    $ docker-compose up -d
    ```
    
</details>


### How to run application in cloud

<details><summary><b>Show instructions</b></summary>

1. Clone the repo:

    ```sh
    $ git clone https://github.com/RolandSaks/gist-check.git
    ```

2. Launch the `gist-checker.yaml` cloudformation template in `aws`:


    ```sh
    $ NB: Stack name has to be `gist-checker`
    ```

5. Add correct parameters for your stack:

<img width="500" alt="Screenshot 2021-07-30 at 12 05 19" src="https://user-images.githubusercontent.com/15733762/127629717-fb9bc500-1b73-486f-b417-ca965122c1ff.png">

</details>


## Kibana

Kibana is a free and open user interface that lets you visualize your Elasticsearch data and navigate the Elastic Stack


<details><summary><b>Show instructions</b></summary>

1. After launching you application you can access kibana from:

   a) Locally
   
             $ localhost:5601
    
   b) AWS
   
             $ ec2publicip:5601
             
2. Please add `pipedrive_test` index in kibana in order to check Elasticsearch data. You can change the index name in `configuration.json` file:

   ```json
        "elasticsearch": {
           "index": "pipedrive_test",
           "host": "localhost",
           "port": "9200"
        }
   ```
    
    <img width="500" alt="Screenshot 2021-07-30 at 12 56 57" src="https://user-images.githubusercontent.com/15733762/127636537-6e048503-8738-43c9-b9d5-6f96efc64d12.png">
    
3. After successful index creation you can see application logs under `discover` panel in kibana

   <img width="500" alt="Screenshot 2021-07-30 at 01 34 49" src="https://user-images.githubusercontent.com/15733762/127574176-fffe9e03-da06-44c3-9e96-2205a2748660.png">

</details>

## Jenkins

Jenkins is used to build and test your software projects continuously making it easier for developers to integrate changes to the project, and making it easier for users to obtain a fresh build.

<details><summary><b>Show instructions</b></summary>

1. After launching you application you can access kibana from:

   a) Locally
   
             $ localhost:8080
    
   b) AWS
   
             $ ec2publicip:8080

2. Please log in to jenkins using `admin` account

3. Add your aws IAM user credentials in order to deploy new docker image to your cf stack.

<img width="500" alt="Screenshot 2021-07-30 at 13 12 12" src="https://user-images.githubusercontent.com/15733762/127638359-6a32b653-a8af-43ac-b642-6cc526704a9a.png">

4. Jenkins consist of two pipelines:

  a) `gist-image` using `Jenkinsfile`
  
  This pipeline clones github repo and builds docker image via dockerfile. After successful build the image is pushed to docker-hub.
  
  b) `gist-application-deploy` using `Jenkinsfile_deploy`
  
  This pipeline takes the last succesfful `gist-image` pipeline build and creates a new cloudformation stack 
  with updated  `GistDockerImage	testgistpipe/gist-checker:${gist-image-lastsucbuild}` parameter and executes it.

