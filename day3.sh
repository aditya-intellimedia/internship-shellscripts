#! /been/sh
echo"Enter the directory name: "
read $directory_name
if [ -d $directory_name ]
then
type=('txt' 'py' 'jpeg')
for((i=0;i<${#type[@]};i++))
{
mv $directory_name/*.${#type[@]} ~/temp/temp.${#type[i]}
}
else
echo "This Directory doesn't exist"
fi
