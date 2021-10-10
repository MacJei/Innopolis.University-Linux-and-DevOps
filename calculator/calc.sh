FILE_1="$1"
FILE_2="$2"

if [[ -z $FILE_1 ]]; then
	echo "Параметры не указаны"
	echo "Пожалуйста, передайте один или два файла с арифметическим выражением, например:"
	echo " sh ./calc.sh file1.txt file2.txt"
else
	result_1=$(($(cat "$FILE_1")))
	if [[ ! -z "$FILE_2" ]]; then
		result_2=$(($(cat "$FILE_2")))
		if [ $result_2 -eq $result_1 ] || [ $result_2 -gt $result_1 ]; then
			echo $result_2
		else
			echo $result_1
		fi
	else
		echo $result_1
	fi
fi
