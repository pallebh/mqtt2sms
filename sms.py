import json
import logger

logger.createLogger( __name__ )


def sms(client,userdata,msg):
    msg = json.loads( msg.payload.decode( "utf-8" ) )
    writetodisk( smstoolformatfile( msg["to"] , msg["msg"] ) )
    
def smstoolformatfile(to,content):
    return "To:{0}\n\n{1}\n".format(to,content)
    
def writetodisk(textmessage): 
    with tempfile.NamedTemporaryFile(mode="at",dir=dir,delete=False) as file_:
        logger.info( textmessage )         
        file_.write(textmessage)
        
