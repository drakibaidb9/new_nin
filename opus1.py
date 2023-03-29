import random
import sys
import websocket
import threading
import time
import json
import logging
import socket
import ssl
import rel
from logging.handlers import SysLogHandler
class ContextFilter(logging.Filter):
    hostname = socket.gethostname()
    def filter(self, record):
        record.hostname = "opus-2"
        return True
syslog = SysLogHandler(address=('logs6.papertrailapp.com', 10066))
syslog.addFilter(ContextFilter())
format = '%(asctime)s %(hostname)s Earnify Bot: %(message)s'
formatter = logging.Formatter(format, datefmt='%b %d %H:%M:%S')
syslog.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(syslog)
logger.setLevel(logging.INFO)
username = "lum-customer-c_5c6306ff-zone-ci_shopee_crawler_1-country-us"
password = "8nb63oxoi7ok"
"""
username = "naxmkqry-rotate"
password = "cn6ro7dfjt4i"
"""
channels = ["0x90B10109840FCEC8A890B786A0986B3304EA9492","0xA69B7A3092ADF3A598ABD48E939F1B4AA4B3ADB8"]
proxys = [
"188.74.210.21:6100",
"45.155.68.129:8133",
"154.95.36.199:6893",
"45.94.47.66:8110",
"144.168.217.88:8780"]



msg3 = {"type":"rate","value":100000000000000000000000}
jsonmsg3 = json.dumps(msg3)
class ws_eat():

    def on_message(this,ws, message):
        
        
        logger.info(message)
        print(message)
        ws.send(jsonmsg3)

    def on_error(this,ws, error):
        print(error)
        logger.error(error)

    def on_close(this,ws, close_status_code, close_msg):
        print("### closed ###")
        logger.warning(close_msg)
        

    def on_open(this,ws):
        ws.send(jsonmsg1)
        ws.send(jsonmsg2)
        ws.send(jsonmsg3)
        

    def ws_thread(this,addr,c,proxy):
        
        hostname = "zproxy.lum-superproxy.io"
        port  = "22225"
        """
        hostname = "p.webshare.io"
        port = "80"
        """
        msg1 = {"type":"channel","value":c}
        jsonmsg1 = json.dumps(msg1)
        msg2= {"type":"wallet","value":addr,"version":"1"}
        
        jsonmsg2 = json.dumps(msg2)
        
        websocket.enableTrace(False)
        
        ws = websocket.WebSocketApp("wss://faices-api.edgevideo.com",
                                on_open=this.on_open,
                                on_message=this.on_message,
                                on_error=this.on_error,
                                on_close=this.on_close)
        print(addr)
        ws.keep_running =True 
        ws.run_forever(  http_proxy_host=hostname, http_proxy_port=port,
        proxy_type="http", http_proxy_auth=(username,password))
    

addresses = []


def read_adr():
    with open("./accounts.txt", 'r') as f:
        ad = f.read()
        ad = ad.split("\n")
        for i in ad:
            addresses.append(i.split(":")[0])


read_adr()

ch = [0,1]


script_name = "eat_exp.py"



    


if __name__ == "__main__":
    for addr in addresses:
        ind = 0
        for c in ch:
            
            socket_cl = ws_eat()
            msg1 = {"type":"channel","value":f"{channels[c]}"}
            jsonmsg1 = json.dumps(msg1)
            msg2= {"type":"wallet","value":addr,"version":"1"}
            
            jsonmsg2 = json.dumps(msg2)    
            daemon_thread = threading.Thread(target=socket_cl.ws_thread,args=(addr,f"{channels[c]}",proxys[0]))
            # or
            # daemon_thread.daemon = True
            # or
            # daemon_thread.setDaemon(True)
            daemon_thread.start()
            time.sleep(10)
        ind = ind + 1
        