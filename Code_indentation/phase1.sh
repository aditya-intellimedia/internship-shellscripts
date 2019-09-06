#! /bin/bash 
echo "Enter the file name :"
read file_name 
if [ -f $file_name ]
then 
index=0 
while IFS=read -r line  
do
    A[index]=$line 
    index= $(($index +1))
 done <$file_name 
 
 for[i=0;i<${#A[@]};i++]]
do 
  c="${A[i]//[^;]}"
       if (("${A[i]}">"1"))
      then
      IFS=";" read -a B <<<"${a[i]}"
      for element in "${B[@]}"
      do
      echo "$element ;">>intermediate_file.c
      done
      else
      echo "${A[i]}">>intermediate_file.c
      fi
      }
 else
  echo "No such file excist"
fi      
      
