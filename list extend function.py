order1=["paneer chilli","green pise","dal tadka"]
order2=["roti","chapati","'bhakari"]
print(order1)
order2.insert(4,"naan")
print(order2)
order1.append("soyabn chilli")
print(order1)
order1.extend(order2)
print(order1)
order2.extend("mashroom")
order2.remove("naan")
print(order2)
order2.pop(4)
print(order2)