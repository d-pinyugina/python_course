str = "world"
for i in str:
    if 'r' == i:
        continue
    print(i)
l = len(str)
Remove_last = str[:l - 1]
print("String : ", Remove_last)


