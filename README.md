#Introduction

This is an python programm that allow you to automaticly update your dns records refered to your machine when your external ip adresse change. This is verry handy for home hosted application if you don't have the budget to get an static ip adress or you don't want to use DyDns.

#Installation
This python script use the [python-ovh](https://github.com/ovh/python-ovh) package.
The python wrapper works with Python 2.7 and Python 3.4+.

The easiest way to get the latest stable release is to grab it from pypi using pip.
```bash
pip install ovh
```

Alternatively, you may get latest development version directly from Git.

```bash
pip install -e git+https://github.com/ovh/python-ovh.git#egg=ovh
```
#Configuration

You will need to have and application_key, application_secret & consumer_key, for that you can read the OVH documentation [here](https://docs.ovh.com/gb/en/customer/first-steps-with-ovh-api/). Don't forget to add the GET and PUT to your application, if not you won't be able to edit dns records.

```python
# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='XXXXXXXX', # Application Key
    application_secret='XXXXXXXX', # Application Secret
    consumer_key="XXXXXXXX", # Consumer Key
)

domain_name = "XXXXXXXX" # Enter your OVH domain name here
```

#Automate with cron
You can create cron to automate the update.
<ins>Simply run:</ins>

```bash
sudo crontab -e
```

And add this line:
```bash
*/30 * * * * /usr/bin/python3 /path/to/your/script/ovh-autoupdate.py
```

This will execute the sript every 30mins. You can easely create your own crontab with this [link](https://crontab.guru)
