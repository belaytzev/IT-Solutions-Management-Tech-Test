# IT-Solutions-Management-Tech-Test

1. Run Hello app in Local with Docker-Composer
```
docker-compose up
```
2. [Hello World Link](http://127.0.0.1:8080)
3. [Prometheus Metrics Link](http://127.0.0.1:8080/metrics)
4. [Liveness Probe Link](http://127.0.0.1:8080/health/liveness)
5. [Readiness Probe Link](http://127.0.0.1:8080/health/readiness)
6. [Grafana Link](http://127.0.0.1:3000)
* User: admin
* Pass: admin
7. Run Hello app in Kubernetes with Helm
```
helm install hello ./helm -n hello --create-namespace -f helm/values.yaml
```
