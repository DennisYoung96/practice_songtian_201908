#14.1csv2json.py
# import json
# fr = open("price2016.csv", "r")
# ls = []
# for line in fr:
#     line = line.replace("\n","")
#     ls.append(line.split(','))
# fr.close()
# print(ls)
# fw = open("price2016.json", "w")
# for i in range(2,len(ls)):
#     ls[i] = dict(zip(ls[1], ls[i]))
# json.dump(ls[2:],fw, sort_keys=True, indent=4, ensure_ascii=False)
# fw.close()


#14.2json2csv.py
import json
fr = open("price2016.json", "r")
ls = json.load(fr)
data = [ list(ls[0].keys()) ]
for item in ls:
    data.append(list(item.values()))
fr.close()
fw = open("price2016_from_json.csv", "w")
for item in data:
    fw.write(",".join(item) + "\n")
fw.close()





