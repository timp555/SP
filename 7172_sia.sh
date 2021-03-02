#!/bin/bash

echo "Программа для блокировки/разблокировки пользователей"
echo "Программа позволяет заблокировать или разблокировать пользователя по его имени"
echo -e "Разработчик: Салова Ирина, гр. 717-2\n\n"
while true; do
	err=0 
	read -p "Введите имя пользователя: " uname
	if ! $(grep -w $uname /etc/passwd &>/dev/null) 
	then
	echo "Такой пользователь отсутствует"
	continue	
	else
		# do stuff
		echo "Выберите действие:"
		select action in "заблокировать" "разблокировать"
		do
			case $action in
				заблокировать)
					passwd -l $uname > /dev/null && echo -e "Пользователь $uname успешно заблокирован\n" || err=$?
					break;;
				разблокировать)
					passwd -u $uname > /dev/null && echo -e "Пользователь $uname успешно разблокирован\n" || err=$?
					break;;
				*) echo "Такой вариант отсутствует, попробуйте ещё раз."; continue;;
			esac
		done

	fi

	echo "Желаете повторить?"
	select again in "да" "нет" 
	do
		case $again in
			да) break ;; 
			нет) exit $err;; 
			*) echo "Такой вариант отсутствует, попробуйте ещё раз."; continue;;
		esac
	done
        echo -e "\n\n"

done
