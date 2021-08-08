import pika, json

params = pika.URLParameters('amqps://iojxyujl:EyPOy4uIHvGbbjEmwW-a3u_4Bl7Wasoj@elk.rmq2.cloudamqp.com/iojxyujl')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)