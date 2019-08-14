#! /bin/bash
echo "Enter the directory name :"
read directory_name

if [ -d $directory_name ]
then

	mkdir temp
	cd $directory_name
	numfiles=(*)
	for((i=0;i<${#numfiles[@]};i++))
	{	
		extension=${numfiles[i]##*.}
		cd ~/temp
	if [ -d all.$extension ]
	 	then	
		mv ~/$directory_name/${numfiles[i]}  ~/temp/all.$extension
	else
		mkdir all.$extension
		mv ~/$directory_name/${numfiles[i]} ~/temp/all.$extension
	fi
	}
	cd ~/
	rm -r $directory_name
	
	mv temp $directory_name 
else 
	echo "no such directory is found"
fi
