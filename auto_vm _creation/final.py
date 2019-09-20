#! /usr/bin/env python
import digitalocean
#import SSHClient
import paramiko

#import subprocess
#import os
manager = digitalocean.Manager(token="")
#my_droplets = manager.get_all_droplets()
#print(my_droplets)
keys = manager.get_all_sshkeys()


Droplet is been created
droplet = digitalocean.Droplet(token="",
                               name='het',
                               region='nyc1', # Amster
                               image='ubuntu-14-04-x64', # Ubuntu 14.04 x64
                               size_slug='512mb',  # 512MB
                               ssh_keys=keys, #Automatic conversion
                               backups=False)
droplet.create()

actions = droplet.get_actions()
for action in actions:
    action.load()
    # Once it shows complete, droplet is up and running
    print(action.status)

sh = paramiko.SSHClient()
sh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

k = paramiko.RSAKey.from_private_key_file(authorized_keys)

sh.connect(hostname=host, username=username, pkey=k)
sh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sudo apt update")
#subprocess.call(["doctl compute droplet create het --region nyc1 --image ubuntu-18-04-x64 --size 1gb --ssh-keys 25336801 --wait"," "])
#cmd="doctl compute droplet create het --region nyc1 --image ubuntu-18-04-x64 --size 1gb --ssh-keys 25336801 --wait"
#os.system("doctl compute droplet create het --region nyc1 --image ubuntu-18-04-x64 --size 1gb --ssh-keys 25336801 --wait")
print("Droplet is created")
#ccmd="doctl compute ssh het"
#os.system(ccmd)
print("DONE !!!")
#os.system("sudo apt update")
#sudo apt install nginx

#sudo apt install php-fpm
                            
