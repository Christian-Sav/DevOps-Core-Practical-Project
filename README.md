# DevOps-Core-Practical-Project
This repository contains the total of my deliverables for the DevOps Core Practical Project

## Contents:  
*  [Project Brief](#Project-Brief)
*  [Project Planning](#Project-Planning)
*  [App Design](#App-Design)
*  [CI Pipeline](#CI-Pipeline)
*  [Known Issues](#Known-Issues)
*  [Future Work](#Future-Work)

## Project Brief:
The brief for this project required us to create a service-orientated architecture composed of at least 4 services that work together this was to be built and maintained using a fully automated CI/CD pipeline. The scope also set out a minimum set of requirements that follow:

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
* This could also provide a record of any issues or risks that you faced creating your project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
* If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
* The project must follow the Service-oriented architecture that has been asked for.
* The project must be deployed using containerisation and an orchestration tool.
* As part of the project, you need to create an Ansible Playbook that will provide the environment that your application needs to run.
* The project must make use of a reverse proxy to make your application accessible to the user.

As well as this there was also a constraint on the technologies that must be used as follows: 

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

## Project Planning:
During the planning phase for this project, I undertook a full risk assessment to possibly identify any hazards associated with this project, the resulting risk assessment is below:

![risk assessment](https://imgur.com/j0O9ee8.png)

As there is no data submitted by users to the app the risks presented are operational more associated with the deployment or the build of the app.

## App Design:
After considering the brief presented I chose to develop an app to generate a random build for Fallout: New Vegas. This not only meets but extends past the required microservice architecture which is shown below 

* Front-end (service 1): The service with which the user interacts. This service sends requests to the other services to generate random stats and then displays the generated build to the user.

* Special API (service 2): This service receives HTTP GET requests from service 1 and responds with a complete set of special stats generated using randint(1, 10).

* Tag API (service 3): This service receives HTTP GET requests from service 1, and responds with 3 randomly chosen tag skills chosen from a list by random.choice().

* Trait API (service 4): This service receives HTTP GET requests from service 1, and responds with 2 randomly traits chosen from a list, again by random.choice().

* Stats API (service 5): This service receives HTTP POST requests from service 1, which provides the randomly generated Special stats, tags and traits as JSON objects, service 5 has 4 if statements along with mathematical calculations that help to generate the stats using the values form service 2,3 and 4 and their effects. The special stats themselves affect their associated stats by stat=(2 + (2*{assossiated special) + ceil({luck special}/2)), the tags increase the associated stat by 15 and the traits have varying effects from +0 to +5 to all.

In addition to these main services, a reverse proxy using NGINX was implemented; the NGINX service listens to port 80 on the host machine and performs a proxy pass, directing traffic from port 80 on the host to port 5000 on the front-end container, where the app is accessible. The images below show the front-end in action:

![front-end](https://imgur.com/yyz1022.png)
![front-end](https://imgur.com/3xsR03p.png)

Currently, The only route available is the home page, I plan to add a history page so you would be able to see previous builds as well but due to the mass of information displayed this is currently only in theory. The events are however stored in a database (currently an SQLite file), the ERD entity relationship diagram for this is below:

![ERD](https://imgur.com/Uk6Nhbk.png)

The microservice architecture is below:

![Architecture](https://imgur.com/5CK03WZ.png)

## CI Pipeline:

As mentioned previously this project does use a complete CI/CI pipeline to test, build, deploy and maintain the application. The pipeline is made of the following main systems:

* Project Tracking
* Version Control
* Development Environment
* CI Server
* Deployment Environment

During this project, Jira was used for project tracking. Each task that was needed was assigned a story point, acceptance criteria and a MoSCoW prioritisation and then moved from Project Backlog to Sprint Backlog to To-Do then to In Progress and eventually to Done as the project was progressed. Below is a snippet of my Jira board mid-project:

![Jira Board](https://imgur.com/BfjpHCg.png)

For the version control, I used git with the project repository being hosted on GitHub, using git for version control allowed for easy access to the commit history for access to earlier versions whilst changes are being made and committed to the project. GitHub as a repository hosting service means that the actual repository for the project is stored far away from the development environment as well as providing webhooks that sends HTTP POST requests to the build server to automate building and testing made GitHub a valuable choice. A feature branch model was implemented in the project to separate the stable version of the application from the ongoing development on the feature branch.

![feature branch model](https://imgur.com/120tMRD.png)

The development environment used was a Ubuntu virtual machine hosted on GCP and accessed through VSCode.

For this project, Jenkins was used as a CI server. In response to the previously mentioned GitHub webhook Jenkins clones down the project repo and executes the pipeline script that is defined within the Jenkinsfile. There are 4 stages to the pipeline: There is Unit testing, Building and Pushing to Docker, Deploying on the Swarm Manager and worker using Docker Compose and finally the post-build actions. During the Unit testing a bash script (test.sh) cycles through each of the directories of the five services and runs their unit tests using pytest.

The front-end and all of the APIs all had unit tests written for them to test ALL areas of functionality. In order to test the HTTP requests that are being made by the front-end requests_mock was used to simulate responses from the APIs. In order to test the functionality of the APIs either random.choice or random.randint was patched with the unittest.mock to ensure reproducible test performance. The result of the tests is archived as a separate coverage report for each service as HTML file artefacts after the build is completed. These are the coverage reports for the separate services:

Shown below Is my Front-End coverage report, with 100% coverage everything related to the front-end has been tested on both the models.py and routes.py.
![Front-End](https://imgur.com/pJzAI3W.png)

Shown below Is my Special-API coverage report, with 70% coverage most of routes.py was tested however due to the addition of the test variable required for the while condition getting 100% coverage was significantly more difficult than the front-end.
![Special-API](https://imgur.com/31gzPJQ.png)

Shown below is my Stat-API coverage report with just over 50% coverage again most of routes.py was covered by the tests however the large number of conditional statements combined with the logic to generate the stats provided a significant challenge in writing the tests.
![Stat-API](https://https://imgur.com/nrQl4vw.png)

Below is the Tag-API Coverage report with barely under 80% coverage only an If conditional wasn't covered by the tests.
![Tag-API](https://imgur.com/t3po1FZ.png)

Finally is the Trait-API coverage report bringing it back with 100% everything in routes.py was tested.
![Trait-API](https://imgur.com/QnDFZCy.png)

As an average of my percentages, my total coverage for the project is just over 80%.

If all of the tests performed are successful then the next stage Build and Push will commence, during this docker-compose is used to build the images for all of the different services, docker is logged into using stored credentials configured on the Jenkins VM, the images are then pushed to Docker hub. Thankfully using a Jenkins pipeline makes optimisation of the project much easier instead of manually building and then pushing all of the required images. As well as this the requirements for testing and general operation have been split into separate files, which means only modules necessary for either tests or deployment are installed when they're required, making this change improved the speed at which the build and push stage is completed. 

Following the build and push, the deploy stage deploys the application.

Finally, in the post-build stage, the coverage reports are archived as artefacts and successful stages appear green, unstable builds are indicated by yellow stages, and failures are indicated via red stages. If a stage fails, later stages will be skipped, preventing failed versions from being deployed, this can be seen here:

![pipeline](https://imgur.com/XNj0Q2X.png)


## Known Issues:
During the final stages of my project my Jenkins VM developed an issue and became nonassessable, I was required to create an entirely new VM and go through the beginning steps of the project again, thankfully this was only a short process and I was back to work in under an hour.

Through the project, I have encountered some small issues, the most noticeable in code being the test variable in the special-API. This is as the maximum special total is 40 and to test the output by patching randint to a value I needed an even amount of variables, before resolution this greatly increased the Unit test stage of my CI pipeline as it would loop until timing out. 

## Future Work;
The first future implementation that I am striving for is to include a history page to display past builds so a build is not lost once a new one is generated.
As well this I would like to add more services to generate more options for the Build such as companions, alliances and play style.
