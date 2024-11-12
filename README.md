
### Docker Compose

```
docker compose up -d
```

![Grafana dashboard screenshot](https://github.com/adavarski/apps-prometehus-graphana-monitoring/blob/main/graphana.png)

### k8s 

#### Create k8s cluster (k3d)
```
k3d cluster create sre
```
#### Install Prometheus Operator
```
cd k8s-manigest
kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus-operator prometheus-community/kube-prometheus-stack --values prometheus.yaml -n monitoring

Note: serviceMonitorSelectorNilUsesHelmValues to false. So prometheus resource got updated and picked up serviceMonitors from other namespaces.

prometheus.yaml
===============
  serviceAccountName: monitoring-prometheus-oper-prometheus
  serviceMonitorNamespaceSelector: {}
  serviceMonitorSelector: {}
  version: v2.7.1

kubectl --namespace monitoring get pods

kubectl port-forward svc/prometheus-operator-kube-p-prometheus -n monitoring 9090:9090
kubectl port-forward svc/prometheus-operator-grafana -n monitoring 3000:80
kubectl get secret -n monitoring  prometheus-operator-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
prom-operator
````
#### Build & Push docker image
```
docker build -t davarski/go-mon:latest .
docker login 
docker push davarski/go-mon:latest
```
##### Deploy apps and apply Prometheus Service Monitors
```
cd k8s-manigest
kubectl apply -f deployment.yaml -f service.yaml 
kubectl apply -f -f servicemonitor.yaml -n monitoring
kubectl port-forward svc/go-mon 8080:8080
curl http://localhost:8080/metrics

kubectl get servicemonitors -n monitoring
```
![Prometheus monitoring target](./pictures/prometheus-go-mon-tearget.png)

![Prometheus monitoring graph](./pictures/prometheus-go-mon-graph.png)

Create Graphana dashboard:

![Graphana Dashboard](./pictures/graphana-dashboard-go-mon.png)

