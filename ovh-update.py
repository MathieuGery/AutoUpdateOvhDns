# -*- encoding: utf-8 -*-
'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
import json
import ovh
import subprocess

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='XXXXXXXXXXX',    # Application Key
    application_secret='XXXXXXXXXXXXX',
    consumer_key="XXXXXXXXXXXXX", # Application Secret    # Consumer Key
)

current_ip = ""
records_id = []
records_info = []

def check_ip_and_update():
    f = open("current_ip.txt", "w")
    process = subprocess.Popen(["dig", "TXT", "+short", "o-o.myaddr.l.google.com", "@ns1.google.com"], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output[:-1]
    ext_ip = output.decode('ascii')
    f.write(ext_ip)
    f.close()

def get_value(val, dic):
    for key, value in dic.items():
        if val == key:
             return value
    return "key doesn't exist"


def get_dns_records():
    records_id = client.get('/domain/zone/gideon.ovh/record/')

    for record in records_id:
        result = client.get('/domain/zone/gideon.ovh/record/' + str(record))
        if get_value('target', result) == current_ip:
            records_info.append(result)
    # Pretty print
    print (json.dumps(records_info, indent=4))

check_ip_and_update()
