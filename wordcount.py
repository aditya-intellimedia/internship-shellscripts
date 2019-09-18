import sys
s=0
f=open("abc.txt","r")
for line in f:
    a=line.split(" ")
    s = s+len(a)
    
print (" Total no. of words : " + str(s) )

==========================================================================================

abc.txt :

Hello Het
Leave the esk at 4 and go to tution
echo "Droplet is been created"
doctl compute droplet create het --region nyc1 --image ubuntu-18-04-x64 --size 1gb --ssh-keys 25336801 --wait
