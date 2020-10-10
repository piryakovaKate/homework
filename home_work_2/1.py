f = open("1_text_for_reading.txt", "r")

x = f.readlines()
print(x[0].strip())


f.close()
