#! /been/sh
echo"Enter the directory name: "
read $directory_name
if [ -d $directory_name ]
then
mv $directory_name/*.txt ~/temp
else
echo "This Directory doesn't exist"
fi
