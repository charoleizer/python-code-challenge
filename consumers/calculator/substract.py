import sys
import os.path

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)
    )
)

import pika

from core import calculator

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="substract")


def callback(ch, method, properties, body):
    body_without_b = str(body)[1:]
    print("".join(["[x] Received: ", body_without_b]))
    x = calculator.substract_custom(body_without_b)
    print("".join(["Saving: ", "substract(", body_without_b, ") = ", str(x)]))


channel.basic_consume(queue="substract", on_message_callback=callback, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
