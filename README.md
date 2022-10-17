# RabbitMQ Example

This Repo is basic RabbitMQ example. This Repo help to understand how to work RabbitMQ.

### Requirements 
```sh
python 3.6
pika==1.2.0
docker
```

### Installation

We run RabbitMQ with Docker. We assume that Docker is installed

First of all we should run the RabbitMQ docker images

```sh
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
```

Then we run the report.py and notify.py files seperate consoles.

```sh
python report.py
python notify.py
```
We start the listen for publish port now. Then we publish the message 

```sh
python publish.py
```
Now we can see the message from publish. This message is in the notfiy.py console and report.py console.


