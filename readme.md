#this is python-flask-redis-webapp

1.  buil docker image
    docker-compose build

2.  push to docker-hub
    docker-compose push

3.  deploy to k8s
    kubectl apply -f ./k8sfile/

4.  get url and port
    kubectl get service hello-flask -o wide

5.  open url

    url1:
    EXTERNAL-IP:nodeport

    url2:
    EXTERNAL-IP:nodeport/home
