# LogFilter Challenge
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

LogFilter is a Python script that uses the tail function to continually check the changes in the logs generated by OurApp. It checks for new lines and filters log lines based on the specified log level. It reads the LOG_LEVEL variable to determine which log  messages to display and continuously outputs matching log lines to the standard output.

ConfigMap is created as a volume attached to the container because that way, the Log_LEVEL variable can be changed without restarting the pod.

## Installation

Use the manifests to create the ConfigMap and the Pod. The logfilter container will run as a sidecar container to ourapp, in that way it can share networking and volumes.

```bash
kubectl create -f log-config-cm.yaml
kubectl create -f logfilter.yaml
```

## Improvements

A better way to deal with changes in LOG_LEVEL: I could have used the [inotify](https://pypi.org/project/inotify/) library to watch for changes to the variable while the script is running. 
