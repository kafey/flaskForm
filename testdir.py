import json
import httplib




# mylist = [{"name":"fname1","value":"ardian"},{"name":"frm2","value":"febri"},{"name":"frm3","value":"jalan ciwaruga"}]
# jsonlist = json.dumps(mylist)
# # print jsonlist
# mylist = json.loads(jsonlist)
# mydict = {}
# MyKey = ["nama depan", "nama belakang", "alamat"]
# for item in MyKey:
# 	for i in range(len(mylist)):
# 		mydict.update( {item:mylist[i]})
# # for item in mylist:
# # 	mydict[item["name"]] = item["value"]

# # print mylist 
# # for item in mylist:
# # 	dest = mydict.update(item)




# print mydict



conn = httplib.HTTPConnection("rajaongkir.com")

headers = { 'key': "b327026a9dcef0e90b7d796078b1340a" }

conn.request("GET", "/api/starter/city?id=&province=5", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


# mydict = {"fname1":"ardian","frm2":"febri", "frm3":"jalanciwaruga"}
