
# General Notes
- Docker Image Deployment: Up to 10 GB for lambda functions
- Use lambda fortasks less than 15 minutes and don't need a GPU - so anything you're doing on a mac air
- Use ec2 for stuff you couldn't serve locally on your mac air even if you wanted to
- Don't discount docker desktop - it's a GUI that can help you keep track of all this, even when you're comfortable with CLI

# Specific notes
* `cdk init app --language typescript` to create this file and directory from scratch (bare bones, less clear)
- Amazon CDK creates a node-like project with abstractions to interact with their services in the cloud easier
- Use <lib> to define infrastructure selections like timeouts, runtimes, etc
- The image/src was created by us, and that's where you write your python and docker scripts
- this build was made using this video <https://www.youtube.com/watch?v=wbsbXfkv47A>

---
## Testing locally
> Quick note: this is good for testing your function, but if you're just messing with a script and preppign, do that elsewhere. When it's ready to become a function, then incorporate this - otherwise your dev iteration loop takes a hit not really for a reason. 
* ` cd image ` 
* ` docker build -t docker-image:<image_name> . ` 
* ` docker run -d -p 9000:8080 -v $(pwd)/src:/var/task --name <container_name> docker-image:<image_name> `  
### To view logs real-time
> Open new terminal side-by-side with main
* `docker logs <container_name>` 
### To SAVE AND RUN:
* ` docker container restart <container_name> && sleep 2 && curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"arg1": 1, "arg2": 2}' ` 
### TO SAVE CHANGES
* ` docker container restart <container_name> ` 

## Testing python locally
- it's recommended to just ` cd src ` and run ` python3 main.py `. focus on gettignt he script down. then worry about making it a working function
---

## Deploying to lambda
* `cd ..`   return to cdk project directory
* `aws sts get-caller-identity`   sanity check for aws cli setup, should give you a json 3 lines deep if configured right
* `cdk bootstrap --region us-east-1`   build infrastructure needed
> click yes to deploy
* `cdk deploy.`   deploy to 
> click link to test the function url
* NOTE- any updates just need `cdk deploy.` no need to rebuild anything in docker











---

# How to set this up on your machine 
* clone this repo `git clone https://github.com/nbened/AWS-Lambda-Python-Docker-Boilerplate.git` 
* rename your project`mv AWS-Lambda-Python-Docker-Boilerplate <custom_project_name> ` 
* navigate to your root o `cd <custom_project_name>` 
* install npm packages to your local directory `npm install` 

--- 

# Welcome to your CDK TypeScript project

This is a blank project for CDK development with TypeScript.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template


