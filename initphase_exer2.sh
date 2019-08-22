#! /bin/bash
echo "Enter the file name :"
read file_name

if [ -f $file_name ]
then
  extension +${$file_name##.}
  touch ind_file.$extension
  while IFS= read -r line
  do
    if[]
    then
      echo "/n $line">>ind_file.$extension
    else
       echo "/n $line">>ind_file.$extension
     fi
   done <"$file_name"
else 
	echo "no such file is found"
fi
