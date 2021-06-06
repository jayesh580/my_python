jay = {
    "jay": "softy",
    "amol": "sweety",
    "list": [1,2,3,4,5],
    "tuple": (1,2,3,4),
    "andic" : {'a':'A', 'b':'B', 'c':'C'}
}
newjay = {
    "softy": "abhishek",
    "amol": "sana"
}
#print(tuple(jay.items()))
#print(list(jay.keys()))
jay.update(newjay)
print(jay)
print(jay.get("softy"))