from os import write


def swapData():
    file1=input("enter first file: ")
    file2=input("enter second file: ")
    with open(file1,'r') as a:
        dataA=a.read()
    with open(file2,'r') as a:
        dataB=a.read()
    with open(file1,'w') as a:
        a.write(dataB)
    with open(file2,'w') as a:
        a.write(dataA)
    print(dataA)
    print(dataB)

swapData()
