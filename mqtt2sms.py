"""
Mqtt2sms brigde between a mqtt broker and the service smstools.

Usage:
  mqtt2sms [-i IP ] [-p PORT ] [-f LOGFILEPATH ]		

Options:
    -i IP --ip IP  Hostname or ip address of the mqtt broker 
    [default: 127.0.0.1]     
    -p PORT --port PORT Port where the mqtt broker is listning 
    [default: 1883]
    -f --logfile LOGFILEPATH path of the logfile used by the program 
    [default: /var/log/mqtt2sms.log]
"""
import logging
import logging.handlers

from docopt import docopt
import paho.mqtt.client


#logger
def createlogger():
    """
    creates logger for screen and file
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logfilepath = "mqtt2sms.log"
    log_file = logging.handlers.RotatingFileHandler(
        logfilepath, mode="a", maxBytes=1024 * 1024, backupCount=5)
    log_file.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s:%(file)s:%(lineno)d:%(message)s',
        datefmt='%m/%d/%Y %H:%M:%S')
    log_file.setFormatter(formatter)
    logger.addHandler(log_file)

    log_console = logging.StreamHandler()
    log_console.setLevel(logging.DEBUG)
    log_console.setFormatter(formatter)
    logger.addHandler(log_console)
    return logger

def sms(msg):
    msg = json.loads(msg.payload.decode("utf-8"))
    writetodisk(smstoolformatfile(msg["to"], msg["msg"]))

def sms_toolformatfile(to, content):
    return "To:{0}\n\n{1}\n".format(to, content)

def sms_writetodisk(textmessage, dir_='/var/spool/sms/outgoing'):
    with stempfile.NamedTemporaryFile( mode="at", dir=dir_, delete=False) as file_:
        file_.write(textmessage)

def mqttclient_on_connect(client, userdata, flags, rc):
    pass

def mqttclient_on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload
    sms(msg)

def mqttclient_publish(topic, payload=None, qos=0, retain=False):
    pass

if __name__ == '__main__':
    logger = createlogger()
    arguments = docopt(__doc__, version="0.9.0")
    ipaddress = arguments["--ip"]
    port = int( arguments["--port"] )

    id_ = 'mqtt2sms'
    mqttclient = paho.mqtt.client.Client(client_id=id_)
    mqttclient.enable_logger(logger)

    mqttclient.on_connect = mqttclient_on_connect
    mqttclient.on_message = mqttclient_on_message


    mqttclient.connect(host = ipaddress, port = port , keepalive = 60, bind_address='')
    mqttclient.subscribe('mqtt2sms')
    
    try:
        mqttclient.loop_forever()
    except KeyboardInterrupt:
        mqttclient.disconnect()



