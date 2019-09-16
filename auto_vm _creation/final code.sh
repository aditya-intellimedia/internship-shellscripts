#! /bin/bash

#doctl auth init
echo "Droplet Name:"
read droplet_name

echo echo "Image Name:"
echo " 1.Ubuntu    2.CentOS    3.Debian "
echo "Press coresponding no."
read no
if [[ $no == "1" ]]
then imag="ubuntu-18-04-x64"
elif [[ $no == "2" ]]
then imag="centos-6-5-x64"
elif [[ $no == "3" ]]
then imag="debian-9-x64"
else
echo "Invalid entry"
fi
echo "Region :"
echo " 1.Newyork1   2.Newyork2   3.Newyork3 "
echo "Press coresponding no."
read nom
if [[ $nom == "1" ]]
then reg="nyc1"
elif [[ $nom == "2" ]]
then reg="nyc2"
elif [[ $nom == "3" ]]
then reg="nyc3"
else echo "Invalid entry"
fi
echo "Droplet is being created"
doctl compute droplet create $droplet_name --region $reg --image $imag --size 1gb --ssh-keys 25336801 --wait

echo "Droplet is created"
doctl compute ssh $droplet_name --ssh-command "sudo apt update"
doctl compute ssh $droplet_name --ssh-command "sudo apt install nginx"
doctl compute ssh $droplet_name --ssh-command "sudo apt install php-fpm"

