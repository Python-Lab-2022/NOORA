car={"brand":"ford","model":"mustang","year":1964}
print(type(car))
print(car)
x=car["model"]
print(x)
for x in car:
    print(x)
for x in car:
    print(car[x])
for x,y in car.items():
    print(x,y)
for x in car.values():
    print(x)

