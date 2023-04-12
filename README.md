# ING final project
Our final project consists of a very minimalistic Flask app that makes a request to an API (https://rapidapi.com/gox-ai-gox-ai-default/api/ott-details/) that return a list of movies released between the years 2015 and 2020.
The project is composed of three parts: Application development, CI/CD on local and CI/CD on cloud

# Application development
Our app makes a REST request to a public API and retrieves the response in a JSON format, in order for the changed data to remain persisted. Everytime the user starts the application, the script checks whether a json file exists with the data, and if not it creates it. We implemented this approach in order to cut down the times we made calls to the API.  

<img width="710" alt="image" src="https://user-images.githubusercontent.com/76562302/231350387-49d0e178-3cdd-4c27-973a-c44ac9fcadbb.png">

For the user to acces the data, we implemented an endpoint called liveness, in which it returns the data in a JSON format (no cute user interface i m afraid)

<img width="503" alt="image" src="https://user-images.githubusercontent.com/76562302/231350617-ae5728f0-6abf-46b9-9234-54369f80c870.png">

In order for the app to be later deployed in a local registry in Docker and on the cloud (with Azure), we wrote a `Dockerfile` script that:
<ul>
  <li>uses a python:3-alpine image</li>
  <li>passes the variables needed for the application to start</li>
  <li>uses a command that installs all the packets used in python</li>
  <li>exposes the app both locally and with the outside</li>
</ul>

<img width="485" alt="image" src="https://user-images.githubusercontent.com/76562302/231351379-470d723a-bde3-4f71-aac8-244106325cd3.png">

# CI/CD on local
Now that we created the image of our application, through the `Dockerfile`, we made a script that contains all the necessary command that help us:
<ul>
  <li>build and push the image to a local registry</li>
  <li>deploy the application into a docker container</li>
  <li>send a curl request to the app's URL to check whether the connection returns a status code of 200 or not</li>
</ul>

Builds the Docker image with the Flask application:<br>
`python3 script.py build --dockerFilePath . --imageName flask-app --imageTag latest`

Pushes the created Docker image into a container registry:<br>
`python3 script.py push --username maraxd --imageName flask-app --imageTag latest`

Deploys a container with the Flask application on your local machine using Docker:<br>
`python3 script.py deploy --imageName maraxd/flask-app --imageTag latest`

Send a curl request to the films endpoint:<br>
`python3 script.py test --endpoint http://localhost:80/films`

As a bonus, we've also wrote a command that creates a Kubernetes deployment with the Flask application in a Kubernetes cluster, deployed on out local machine:
<br>
`python3 script.py deployK --deploymentFile deployment.yaml --serviceName flask-service`




