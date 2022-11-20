s = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s == s2)
print(s != s2)

s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))
print(s3.issubset(s1))

print(s1.issuperset(s2))

print(s2.isdisjoint(s3))  # false
s4 = {100, 200, 300}
print(s2.isdisjoint(s4))  # true
