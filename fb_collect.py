import requests as req
import urllib3
import xml.etree.ElementTree as ET
import hashlib
import json
import sqlite3
from time import sleep
    
#   Loads the Configuration Data
def load_config():
    with open('fb_config.json', 'r') as file:
        return json.load(file)

#   Getting the SID
def fb_get_sid(fritzbox, fritz_user, fritz_pw):
    session = req.Session()
    http = urllib3.PoolManager()
    data = http.request("get", fritzbox + "/login_sid.lua").data
    tree = ET.fromstring(data)
    fb_sid = tree.findtext("SID")
    if fb_sid == "0000000000000000":
        challenge = tree.findtext("Challenge")
        hash_me = (challenge + "-" + fritz_pw).encode("UTF-16LE")
        hashed = hashlib.md5(hash_me).hexdigest()
        response = challenge + "-" + hashed
        ret = session.get(fritzbox + "/login_sid.lua", params={
            "username": fritz_user,
            "response": response
        }, verify=False, timeout=5)
        tree = ET.fromstring(ret.text)
        fb_sid = tree.findtext("SID")
        if fb_sid == "0000000000000000":
            print("fb_get_sid: Could not get SID, check your User Data")
            exit()
    return fb_sid

#   Creating the Sqlite Database if not already done
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messwerte 
              (zeit TIMESTAMP DEFAULT CURRENT_TIMESTAMP, wert TEXT)''')
    conn.commit()
    conn.close()

def save_to_db(raw_value):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO messwerte (wert) VALUES (?)', (raw_value,))
    conn.commit()
    conn.close()

#   Call for the sensor data. 
#   More calls can be added but this requires to add more variables to 
#   the config.json file
def main():
    config = load_config()
    init_db()  

    while True:
        fb_sid = fb_get_sid(config['routerurl'], 
                            config['username'], config['password'])
        params = {
            "ain": config['device_ain'],
            "switchcmd": config['command_cmd'],
            "sid": fb_sid
        }

        resp = req.get(config['ahaurl'], params=params)

        if resp.status_code == 200:
            raw_value = resp.text
            save_to_db(raw_value) 
        else:
            print("Value Error")
            
#   Sets the Intervall between calls in seconds   
        sleep(config.get('interval', 60))
if __name__ == '__main__':
    main()
