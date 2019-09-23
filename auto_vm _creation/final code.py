#! /usr/bin/env python
import digitalocean
import paramiko

userdata_script="""
#cloud-config

runcmd:
  - apt-get update -y
  - apt-get install -y php-fpm nginx
"""

manager = digitalocean.Manager(token="")
keys = manager.get_all_sshkeys()
print("Enter Dropletr's name: ")
dname=input()

print("Press digit to select the image:")
print("""
         1. Ubuntu
         2. Fedora
         3. Centos
         4. Debian""" )

sno=input()

if sno=="1":
    sno="ubuntu-18-04-x64"
elif  sno=="2":
    sno="fedora-30-x64"
elif  sno=="3":
    sno="centos-7-x64"
elif  sno=="4":
    sno="debian-10-x64"
else:
    print("INAVLID IMAGE!!!")


print("Press digit to select the region:")
print("""
         1. Newyork1
         2. Newyork2
         3. Newyork3""" )
sno1=input()

if sno1=="1":
    sno1="nyc1"
elif  sno1=="2":
    sno1="nyc2"
elif  sno1=="3":
    sno1="nyc3"
else:
    print("INAVLID REGION!!!")

print ("Droplet is been created")
droplet = digitalocean.Droplet(token="",
                               name=dname,
                               region=sno1, # New York 2
                               image=sno, # Ubuntu 14.04 x64
                               size_slug='512mb',
                               user_data=userdata_script,
                               backups=False)
droplet.create()
actions = droplet.get_actions()
for action in actions:
    action.load()
    # Once it shows complete, droplet is up and running
    print(action.statusprint("Droplet is created")
    print("DONE !!!")
