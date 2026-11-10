import subprocess

def cls():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

list1 = []
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            print("{}.{}.{}".format(x, y, z))
            list1.append("{}.{}.{}".format(x, y, z))
cls()
print(list1)
