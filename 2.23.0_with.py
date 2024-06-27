file_name = 'file_3.txt'
data = 'Meow!'

#выполнение различных действий с файлом, чтобы он сам не закрылся
# fw = open(file_name, 'w')
# fw.write(data)
# fw.close()

#используется для того, чтобы отредактировать файл и сразу закрыть его
with open(file_name, 'a') as files:
    files.write(data)