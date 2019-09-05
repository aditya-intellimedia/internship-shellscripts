#! /bin/bash 
echo "Enter the file name :"
read file_name 
if [ -f $file_name ]
then 
extension=${file_name##*.}
touch ind_file.$extension 
index=0 
while read line 
do
    A[index]=$line 
    index= $(($index +1))
    done <$file_name 
    echo " ${A[@]} " 
    space=" " 
    func()
    {
      if [[${A[i]} = *'{']]
      then
      echo "$space ${A[i]}">>ind_file.$extension
      i=$(($i+1))
      while [[${A[i]} != }* ]]
      do 
        echo"$space $space ${A[i]} ">>ind_file.$extension
        i=$(($i+1))
     done
     fi
     }
for[i=0;i<${#A[@]};i++]]
do 
       if [[${A[i]} = *'{']]
      then
      echo "${A[i]}">>ind_file.$extension
      i=$(($i+1))
      while [[${A[i]} != }* ]]
      do 
        func
        echo" $space ${A[i]} ">>ind_file.$extension
        i=$(($i+1))
     done
      i=$(($i-1))
      else
       echo "${A[i]}">>ind_file.$extension
       fi
       done
       else
       echo "No such directory excist"
fi     
