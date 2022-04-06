# DevOps-Core-Practical-Project
This repository containts the total of my deliverables for the DevOps Core Practical Project

## Contents:  
*  [Project Brief](#Project-Brief)
*  [Project Planning](#Project-Planning)
*  [App Design](#App-Design)
*  [CI Pipeline](#CI-Pipeline)
*  [Known Issues](#Known-Issues)
*  [Future Work](#Future-Work)

## Project Brief:
The brief for this project required us to create a service-orientated architecure composing of at least 4 services that work together this was to be built and maintained using a fully automated CI/CD pipeline. The scope also set out a minimum set of requirements that follow:

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
* This could also provide a record of any issues or risks that you faced creating your project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
* If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
* The project must follow the Service-oriented architecture that has been asked for.
* The project must be deployed using containerisation and an orchestration tool.
* As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
* The project must make use of a reverse proxy to make your application accessible to the user.

As well as this there was also a constraint on the technologies that must be used that follows: 

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

## Project Planning:
During the planning phase for this project I undertook a full risk assessment in order to possibly identify any hazards assossiated with this project, the resulting risk assessment is below:

{risk assessment}

As there is no data submitted by users to the app the risks presented are operational risk more assossiated with the deployment or the build of the app.

## App Design:
After considering the brief presented I chose to develop an app to generate a random build for Fallout: New Vegas. This not only meets but extends past the required microservice architecture which is shown below 

* Front-end (service 1): The service with which the user interacts. This service sends requests to the other services to generate random stats and then displays the generated build to the user.

* Special API (service 2): This service receives HTTP GET requests from service 1 and responds with a complete set of special stats generated using randint(1, 10).

* Tag API (service 3): This service receives HTTP GET requests from service 1, and responds with 3 randomly chosen tag skills chosen from a list by random.choice().

* Trait API (service 4): This service receives HTTP GET requests from service 1, and responds with 2 randomly traits chosen from a list, again by random.choice().

* Stats API (service 5): This service receives HTTP POST requests from service 1, which provides the randomly generated Special stats, tags and traitsas JSON objects, service 5 has 4 if statments along with mathmatical calulations that help to generate the stats using the values form service 2,3 and 4 and their affects. The special stats themselves affect thir assosiated stats by stat=(2 + (2*{assossiated special) + ceil({luck special}/2)), the tags increase the assossiated stat by 15 and the traits have varying affects from +0 to +5 to all.

In addition to these main services, a reverse proxy using NGINX was implemented; the NGINX service listens to port 80 on the host machine and performs a proxy pass, directing traffic from port 80 on the host to port 5000 on the front-end container, where the app is accessible. The images below show the front-end in action:

{front-end}
S
Currently The only route availiable is the home page, I plan to add a history page so you would be able to see previous builds as well but due to the mass of information displayed this is currently only in theory. The events are however stored in a database (currently an sqlite file), the ERD entity relationship diagram for this is below:

{ERD}

The microservice architecture is below:


## CI Pipeline:

As mentioned previously this project does use a complete CI/CI pipeline in order to test, build, deploy and maintain the application. The pipeline is made of the following main systems:

* Project Tracking
* Version Control
* Development Enviroment
* CI Server
* Deloyment Enviroment

During this project Jira was used for project tracking. Each task that was needed was assigned a story point, acceptance criteria and a MoSCoW prioritisation and then moved from Project Backlog to Sprint Backlog to To Do then to In Progress and eventually to done as the project was progressed. Below is a snippet of my jira board mid project:

{jira board}

For the version control I used git with the project repository being hosted on github, using git for version control allowed for easy access to the commit history for access to earlier versions whilst changes are being made and committed to the project. GitHub as a repository hosting service means that the actual repositoy for the project is sotred far away from the development environment this as well as providing webhooks which send http POST requests to the build server to automate building and testing made GitHub a valuable choice. A feature branch model was implemented in the project as to seperate the stable version of the application from the ongoing development on the feature branch.

{feature branch model}

The development enviroment used was a Ubuntu virtual machine hosted on GCP and accessed through VSCode.

For this project Jenkins was used as a CI server. In response to the previously mentioned github webhook Jenkins clones down the project repo and executes the pipeline script that is defined within the Jenkinsfile. There are 4 stages to the pipeline: There is Unit testing, Building and Pushing to Docker, Deploying on the Swarm Manager and worker using Docker Compose and finally the post-build actions. During the Unit testing a bash script (test.sh) cycles through each of the dirctories of the five services and runs their unit tests using pytest.

The front-end and all of the API;s all had unit tests written for them to test ALL areas of functionality. In order to test the HTTP requests that are being made by the front-end requests_mock was used to simulate responses from the APIs. In order to test the functionality of the APIs either random.choice or random.randint was patched with the unittest.mock to ensure reproducable test performance. The result of the tests are archived as a serperate coverage report for each service as HTML file artifacts after the build is completed. These are the coverage reports for the seperate services:

{front-end test}
{special test}
{tag test}
{trait test}
{stat test}
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the tests are successful, the build/push stage uses docker-compose to build the images for the different services, logs into docker using credentials configured on the Jenkins VM, and then pushes the images to Dockerhub. The use of a Jenkins pipeline, with this stage-by-stage breakdown, makes optimisation of the project easier. For example, initially all pip installs, for tests and deployment, were done using one requirements file, which meant that testing modules were being installed when building the images; since this was not necessary and since the build/push stage was the longest stage in the pipeline the requirements were separated into a requirements.txt file, containing only the pip installs needed to run the app, and a test_requirements.txt file, which contained all requirements including testing modules. This eliminated unnecessary pip installs during the build stage

As can be seen here, 100% coverage was achieved for all services; this ensured that all of the functions of the app worked exactly as intended.

Following the build and push, the deploy stage deploys the application. First the docker-compose.yaml and nginx.conf files are copied to the manager node by secure copy (scp). Then, an ansible playbook is used to run three roles: the first installs docker on the swarm machines if it is not present already and adds jenkins to the docker group, the second initialises a swarm on the manager node and uses the Ansible docker stack module to deploy the application, and the third adds the worker node to the swarm. This creates an overlay network as follows:

{overlay network}

Finally, in the post-build stage, the j-unit and cobertura test reports are published. The result of this pipeline is shown below:

{stage view}

Successful stages appear green, unstable builds are indicated by yellow stages, and failures are indicated via red stages. If a stage fails, later stages will be skipped, preventing failed versions from being deployed, this can be seen here:
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
{pipeline}

The overall structure of the CI/CD pipeline is:

{structure}

## Known Issues:

## Future Work;
THe first future implementation that I am striving for is to include a history page to display past builds so a build is not lost once a new one is genrated.
