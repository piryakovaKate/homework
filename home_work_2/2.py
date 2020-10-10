def write_array(array, file_name):
    N = len(array)
    if N == 0:
        return 
    x = array[N-1]

    # записываю в файл
    f.write(x + '\n')
    array.pop()

    write_array(array, file_name)


array = ['fist_str', 'second_str', 'third_str', 'fourth_str', 'fifth_str']
f = open('file_for_writing.txt', 'a')
write_array(array, f) 

f.close()
