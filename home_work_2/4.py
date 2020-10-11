import json

fl = open('1.json','r')

d1 = json.loads(fl.read())
d1["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["week"] = "3"

fl.close()


f1 = open('1_way_for_dumps.json','w')
arr = json.dumps(d1)
for i in range(len(arr)):
    f1.write(arr[i])
f1.close()


f2 = open('2_way_for_dump.json','w')
json.dump(d1, f2)
f2.close()
