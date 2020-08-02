import pika


def sendSum(x):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="sum")
    channel.basic_publish(exchange="", routing_key="sum", body=x)

    connection.close()


def sendSubstract(x):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="substract")
    channel.basic_publish(exchange="", routing_key="substract", body=x)

    connection.close()
