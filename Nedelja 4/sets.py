skup1 = {2}
skup1.add(4)
print(skup1)
skup2 = {2,4,6}

print(skup1.intersection(skup2))
print(skup1.union(skup2))
print(skup2.issuperset(skup1))

skup2.discard(2)