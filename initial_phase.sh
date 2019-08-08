#! /been/sh
echo"Enter the directory name: "
read $directory_name
if [ -d $directory_name ]
then
echo "Here will be the link to the further code"
else
echo "This Directory doesn't exist"
fi
