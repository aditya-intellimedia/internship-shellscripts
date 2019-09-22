#! /usr/bin/env python
import digitalocean
import paramiko
manager = digitalocean.Manager(token="")
keys = manager.get_all_sshkeys()
print ("Droplet is been created")
droplet = digitalocean.Droplet(token="",
                               name='Het',
                               region='nyc1', # New York 2
                               image='ubuntu-14-04-x64', # Ubuntu 14.04 x64
                               size_slug='512mb',  # 512MB
                               backups=False)
droplet.create()
actions = droplet.get_actions()
for action in actions:
    action.load()
    # Once it shows complete, droplet is up and running
    print(action.status)
print("Enter your password : ")
g=input()

print("Enter your ip : ")
i=input()
ssh = paramiko.SSHClient()ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(i, username="root", password=g)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sudo apt update")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sudo install ngix")
print("Droplet is created")
#ccmd="doctl compute ssh het"
#os.system(ccmd)
print("DONE !!!")
#os.system("sudo apt update")
#sudo apt install nginx
