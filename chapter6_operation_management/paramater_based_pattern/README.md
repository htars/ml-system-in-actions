# parameter based prediction pattern

## 目的

パラメータによってリクエストする推論器を変えるパターンです。

## 前提

- Python 3.8以上
- Docker
- Kubernetesクラスターまたはminikube

## 使い方

1. Dockerイメージをビルド

```sh
$ make build_all
docker build \
		-t shibui/ml-system-in-actions:parameter_based_pattern_setosa_0.0.1 \
		-f ./Dockerfile.service.setosa \
		.
docker build \
		-t shibui/ml-system-in-actions:parameter_based_pattern_versicolor_0.0.1 \
		-f ./Dockerfile.service.versicolor \
		.
docker build \
		-t shibui/ml-system-in-actions:parameter_based_pattern_virginica_0.0.1 \
		-f ./Dockerfile.service.virginica \
		.
docker build \
		-t shibui/ml-system-in-actions:parameter_based_pattern_proxy_0.0.1 \
		-f ./Dockerfile.proxy \
		.
docker build \
		-t shibui/ml-system-in-actions:parameter_based_pattern_client_0.0.1 \
		-f ./Dockerfile.client \
		.
```

2. Kubernetesでサービスを起動

```sh
$ make deploy
kubectl apply -f manifests/namespace.yml
kubectl apply -f manifests/

# 稼働確認
$ kubectl -n parameter-based get all
NAME                                   READY   STATUS    RESTARTS   AGE
pod/client                             1/1     Running   0          37s
pod/iris-setosa-65ff969788-ck4fj       1/1     Running   0          36s
pod/iris-setosa-65ff969788-krvtb       1/1     Running   0          36s
pod/iris-setosa-65ff969788-n8jl7       1/1     Running   0          36s
pod/iris-versicolor-6859488d66-5jpz7   1/1     Running   0          36s
pod/iris-versicolor-6859488d66-lxpn5   1/1     Running   0          36s
pod/iris-versicolor-6859488d66-r6tds   1/1     Running   0          36s
pod/iris-virginica-56cd8c569d-f29f5    1/1     Running   0          35s
pod/iris-virginica-56cd8c569d-n8ljk    1/1     Running   0          35s
pod/iris-virginica-56cd8c569d-z5ts2    1/1     Running   0          35s
pod/proxy-78d645844d-dz2ld             1/1     Running   0          37s
pod/proxy-78d645844d-qrgbv             1/1     Running   0          37s
pod/proxy-78d645844d-zn4mt             1/1     Running   0          37s

NAME                      TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
service/iris-setosa       ClusterIP   10.4.9.6      <none>        8000/TCP   36s
service/iris-versicolor   ClusterIP   10.4.7.226    <none>        8001/TCP   36s
service/iris-virginica    ClusterIP   10.4.10.166   <none>        8002/TCP   35s
service/proxy             ClusterIP   10.4.13.181   <none>        9000/TCP   37s

NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/iris-setosa       3/3     3            3           36s
deployment.apps/iris-versicolor   3/3     3            3           36s
deployment.apps/iris-virginica    3/3     3            3           35s
deployment.apps/proxy             3/3     3            3           37s

NAME                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/iris-setosa-65ff969788       3         3         3       36s
replicaset.apps/iris-versicolor-6859488d66   3         3         3       36s
replicaset.apps/iris-virginica-56cd8c569d    3         3         3       35s
replicaset.apps/proxy-78d645844d             3         3         3       37s
```

3. 起動したAPIにリクエスト

```sh
# クライアントに接続
$ kubectl -n parameter-based exec -it pod/client bash

# 同じエンドポイントに異なるデータをリクエストします。
$ curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"data": [[5.1, 3.5, 1.4, 0.2]]}' \
    proxy.parameter-based.svc.cluster.local:9000/predict
{
  "setosa": 1,
  "versicolor": 0
}

$ curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"data": [[50.0, 30.1, 111.4, 110.2]]}' \
    proxy.parameter-based.svc.cluster.local:9000/predict 
{
  "setosa": 0,
  "versicolor": 0
}
```

4. Kubernetesからサービスを削除

```sh
$ kubectl delete ns parameter-based
```