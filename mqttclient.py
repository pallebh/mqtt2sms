import paho.mqtt.client as mqttw


class MqttClient(object):
    """
    Mqtt client
    """

    def __init__(self,
                 address="localhost",
                 port=1883,
                 id_="mqtt2sms",
                 message=None,
                 subscribtions=None):
        self.address = address
        self.port = port
        self.message = message
        self.subscribtions = subscribtions
        self.client = mqttw.Client(client_id=id_)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(self.address, self.port)
        self.client.loop_forever()
        self.log = createLogger(__name__)

    def on_connect(self, client, userdata, flags, rc):
        """
        called when the connected to the mqtt broker
        """
        for subscribtion in self.subscribtions:
            self.client.subscribe(subscribtion)

    def on_message(self, client, userdata, msg):
        """
        callback funttion for message recieved over the mqqt protocol
        """
        self.log.debug('client:{0} userdata:{1} msg:{2}'.format(
            client, userdata, msg))

        if self.message is None:
            return

        self.message(client, userdata, msg)

    def publish(self, topic, payload=None, qos=0, retain=False):
        """
        function used to send messages tp the broker
        """
        self.log.debug('topic:{0} payload:{1} qos:{2} retain{3}'.format(
            topic, payload, qos, retain))
        self.client.publish(topic, payload, qos, retain)
