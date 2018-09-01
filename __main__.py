"""
Mqtt2sms brigde between a mqtt broker and the service smstools.


Usage:
  mqtt2sms [-i IP ] [-p PORT ] -s SUBSCRITIONS... [-f LOGFILEPATH ] [-l LOGLEVEL ]		

Options:
    -i IP --ip IP  Hostname or ip address of the mqtt broker [default: 127.0.0.1]     
    -p PORT --port PORT  Port of the mqtt broker [default: 1883]
    -s SUBSCRITIONS --subscribtions SUBSCRIBTIONS  Subscribtions to messages from the mqtt broker
    -f --logfile LOGFILEPATH path of the logfile used by the program [default: /var/log/mqtt2sms.log]
"""

import mqttclient
import sms
import logger
from docopt import docopt

if __name__ == '__main__' :
    arguments = docopt (__doc__, version="0.0.1")
    mc = mqttclient.MqttClient( address = arguments["--ip"] , 
    port = int( arguments["--port"] ) ,  
    message = sms.sms , 
    subscribtions = arguments["--subscribtions"] 
    )
     
    
