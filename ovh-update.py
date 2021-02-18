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
    application_key='XXXXXXXXX', # Application Key
    application_secret='XXXXXXXXX', # Application Secret
    consumer_key="XXXXXXXXX", # Consumer Key
)

domain_name = "XXXXXXXXX" # Enter your OVH domain name here

current_ip = ""


def check_ip_and_update():
    process = subprocess.Popen(["dig", "TXT", "+short", "o-o.myaddr.l.google.com", "@ns1.google.com"], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output[:-1]
    ext_ip = output.decode('ascii')
    check_if_file_exist()
    f = open("current_ip.txt", "r+")
    if (f.read() != ext_ip):
        f.close()
        f = open("current_ip.txt", "w")
        f.write(ext_ip)
        f.close()
    else:
        print("Nothing to do")

def check_if_file_exist():
    try:
        f = open("current_ip.txt", "r+")
    except:
        f = open("current_ip.txt", "w+")
        f.close()

def get_value(val, dic):
    for key, value in dic.items():
        if val == key:
             return value
    return "key doesn't exist"


def get_dns_records():
    records_id = []
    records_info = []
    records_id = client.get("/domain/zone/" + domain_name + "/record/")

    for record in records_id:
        result = client.get("/domain/zone/" + domaine_name + "/record/" + str(record))
        if get_value("target", result) == current_ip:
            records_info.append(result)
    # Pretty print
    print (json.dumps(records_info, indent=4))

check_ip_and_update()
