# kubernetes-final-project
Basic Python Flask app deployed using Kubernetes which saves the name, last_name and role of the employee

### Project structure
```
final-project/
├── src
│   ├── __init__.py
│   └──app.py
├── Dockerfile
├── final-app-deployment.yml
├── final-app-service.yml
├── final-ingress.yml
├── final-mysql-configmap.yml
├── final-mysql-deployment.yml
├── final-mysql-secret.yml
├── final-mysql-service.yml
└── requirements.txt
```

### Download application
Download the project by cloning the Git repo.
```
$ git clone https://github.com/ximegasub/kubernetes-final-project.git
```

### Create image for the final-app-deployment.yml
The existing image is in [DockerHub](https://hub.docker.com/repository/docker/ximegasub/python-flask-kb8).
```
$ docker build -t ximegasub/python-flask-kb8:0.5 .
$ docker push ximegasub/python-flask-kb8:0.5
```

### Prerequisites
Run this command, then grab the result and set this IP address in ```final-mysql-configmap.yml``` in ```mysql-host```
```
$ kubectl get pod <final-mysql-deployment-....> -o template --template={{.status.podIP}}
```

### Run the manifests
```
$ kubectl apply -f final-mysql-configmap.yml
$ kubectl apply -f final-mysql-secret.yml
$ kubectl apply -f final-mysql-deployment.yml
$ kubectl apply -f final-mysql-service.yml
$ kubectl apply -f final-app-deployment.yml
$ kubectl apply -f final-app-service.yml
$ kubectl apply -f final-ingress.yml
```

### Test the project
Use curl command to save employee's data:
```
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"<name>", "last_name": "<last_name>", "role": "<role>"}' http://<IP node>/add-employee 
```
Also, visit to see the home page:
```
http://<IP node>:8000/ 
```

### Verify the running app by checking the result:
```
$ The employee with name: <name>, last name: <last_name>, role: <role> was created succesfully.
```

### Verify the running app by checking the result in case the employee's name was already created:
```
$ Employee already exists.
```

#### Additional note:
Check this working on my assigned instance: ```k8s-instance-6```

