import os

array = []    # в этом массиве будет хранить список из строк, содержащих директории(в которых есть .py)

f = open('text_for_dir.txt', 'w')
os.chdir('архив')

for current_dir, dirs, files in os.walk("."):
    for j in range(len(dirs)): # берем одну папку и просмотриваем все файлы, если находим с нужным расширение, то кидаем имя папки в массив 

        for i in range(len(files)):   # просматриваем все файлы
           filename, file_extension = os.path.splitext(files[i])
           if file_extension == '.py' : # смотрим на расширение
               print(os.getcwd())

               needs_dir = dirs[j]
               if needs_dir not in array:    # чтоб не было повторяющихся папок
                    array.append(needs_dir)

array.sort()
for i in range(len(array)):
    f.write(array[i])
    f.write('\n')


f.close()


