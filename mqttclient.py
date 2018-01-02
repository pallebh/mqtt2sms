import paho.mqtt.client as mqttw
import logger

class MqttClient :

    def __init__( self , address = "localhost", port = 1883 , id = "mqtt2sms" ,  message = None , subscribtions = None ) :
        self.address = address
        self.port = port
        self.message = message
        self.subscribtions = subscribtions
        self.client = mqttw.Client( client_id = id )

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(self.address, self.port)
        self.client.loop_forever()
        self.log = createLogger( __name__ ) 
        

    def on_connect( self , client , userdata , flags , rc ) :
        for subscribtion in self.subscribtions :
            self.client.subscribe( subscribtion )

    def on_message( self , client , userdata , msg ) :
        self.log.info( "client:{0} userdata:{1} msg:{2}".format( client , userdata , msg ) 
        
        if self.message is None :
            return
        self.message( client , userdata , msg )

    def publish( self , topic, payload=None, qos=0, retain=False ) :
        self.log.info( "client:{0} userdata:{1} msg:{2}".format( client , userdata , msg ) 
        self.client.publish( topic  , payload , qos , retain )

