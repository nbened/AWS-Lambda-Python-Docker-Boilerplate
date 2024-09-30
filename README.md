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



# Nic Notes

## Overall Notes
- Docker Image Deployment: Up to 10 GB for lambda functions
- Use lambda fortasks less than 15 minutes and don't need a GPU - so anything you're doing on a mac air
- Use ec2 for stuff you couldn't serve locally on your mac air even if you wanted to

## Working notes
* `cdk init app --language typescript` to create this file and directory from scratch (bare bones, less clear)
- Amazon CDK creates a node-like project with abstractions to interact with their services in the cloud easier
- Use <lib> to define infrastructure selections like timeouts, runtimes, etc
- The image/src was created by us, and that's where you write your python and docker scripts
- this build was made using this video <https://www.youtube.com/watch?v=wbsbXfkv47A>

### Testing locally
* `cd image` 
* `docker build -t docker-image:<build_name> .` 
* `docker run -p 9000:8080 docker-image:<build_name>` 
> Open new terminal
* `curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'` 

### Deploying to lambda
* `aws sts get-caller-identity`   sanity check for aws cli setup, should give you a json 3 lines deep if configured right
* `cd ..`   return to cdk project directory
* `cdk bootstrap --region us-east-2`   return to cdk project directory
> click yes to deploy
* `cdk deploy.`   return to cdk project directory
> click link to test the function url
