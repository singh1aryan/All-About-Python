def rv(str):
    l = ['a','e','i','o','u']
    b=set(l)
    a=""
    for i in str:
        if i not in b:
            a+=i
    return a


print(rv("leetcodearyan"))
print(rv("aeieieoe"))

#  making a set is less expensive than using contains in a list
