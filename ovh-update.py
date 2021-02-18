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
    application_key='XXXXXXXXXX', # Application Key
    application_secret='XXXXXXXXXX', # Application Secret
    consumer_key="XXXXXXXXXX", # Consumer Key
)

domain_name = "XXXXXXXXXX" # Enter your OVH domain name here

def check_if_file_exist():
    try:
        f = open("current_ip.txt", "r")
        f.close()
    except:
        f = open("current_ip.txt", "w+")
        f.close()

def get_value(val, dic):
    for key, value in dic.items():
        if val == key:
             return value
    return "key doesn't exist"

def get_dns_records(previous_ip):
    records_id = []
    records_info = []
    records_id = client.get("/domain/zone/" + domain_name + "/record/")

    for record in records_id:
        result = client.get("/domain/zone/" + domain_name + "/record/" + str(record))
        if get_value("target", result) == previous_ip:
            records_info.append(result)
    return (records_info)

def update_dns(previous_ip, new_ip):
    print("previous", previous_ip)
    print("newip", new_ip)
    # Pretty print
    print (json.dumps(get_dns_records(previous_ip), indent=4))
    dns_records = get_dns_records(previous_ip)
    print(dns_records[1]["id"])
    for record in dns_records:
        print(record["id"])

def check_ip_and_update():
    process = subprocess.Popen(["dig", "TXT", "+short", "o-o.myaddr.l.google.com", "@ns1.google.com"], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output[1:-2]
    ext_ip = output.decode('ascii')
    check_if_file_exist()
    f = open("current_ip.txt", "r+")
    previous_ip = f.read()
    if (previous_ip != ext_ip):
        f.close()
        f = open("current_ip.txt", "w")
        f.write(ext_ip)
        f.close()
        update_dns(previous_ip, ext_ip)
    else:
        print("Nothing to do")

check_ip_and_update()
