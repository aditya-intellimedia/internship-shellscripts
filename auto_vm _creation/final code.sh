#! /bin/bash

#doctl auth init

echo "Droplet is being created"
doctl compute droplet create het --region nyc1 --image ubuntu-18-04-x64 --size 1gb --ssh-keys 25336801 --wait

echo "Droplet is created"
doctl compute ssh het --ssh-command "sudo apt update"
doctl compute ssh het --ssh-command "sudo apt install nginx"
doctl compute ssh het --ssh-command "sudo apt install php-fpm"

