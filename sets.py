val = {12, 56, 23, 45, 12, 48, 23}
print(val)
# items are not repeated and are printed in any random order
for i in val:
    print(i)
# print(val[2]) this will throw error
val1 = {}
print(val1)
print(type(val1))
# yahape output me class dict ayega, dictionary and set ka syntax same hai almost
# to make and empty set do this
val2 = set()
print(type(val2))
print(val2)

# ------------------Set methods-------------------------
# update and union method
city = {'Tokyo', 'Berlin', 'Mumbai', 'Pune'}
city2 = {'Tokyo', 'Berlin', 'Mumbai', 'Pune', 'blore', 'delhi'}
cityy = {'Tokyo'}
city3 = city.union(city2)
print(city3)
print(city.union(city2))
# isme sets me changes nai honge kuch
print(city)
print(city2)
print(cityy)
city4 = cityy.update(city)
# iska output None ayega
# print(city4)
print(cityy)
print(city4)

# intersection and intersection update
val={1,2,3,4,5}
val2={4,5,6,7,8}
print(val.intersection(val2))
# 4 and 5 print karega
print(val2)
val2.intersection_update(val)
print(val2)
# 4 and 5 values leke val2 ek naya set ban jayga

# symmetric difference and symmetric difference update method
val={1,2,3,4,5}
val2={4,5,6,7,8}
print(val2.symmetric_difference(val))
# 1 2 3 6 7 8 print hoga
print(val2)
val2.symmetric_difference_update(val)
print(val2)
# 1 2 3 6 7 8 values leke naya set banjayga

# difference and difference update method
val={1,2,3,4,5}
val2={4,5,6,7,8}
print(val.difference(val2))
# 1 2 3 print hoga
print(val2)
# val2.difference_update(val)
# print(val2)
# 6 7 8 values leke set banjayga
print(val)
val.difference_update(val2)
print(val)
# 1 2 3 values leke set banjayga

# Disjoint method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2)) #false

#superset
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

#subset
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

