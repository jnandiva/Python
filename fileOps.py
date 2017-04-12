
fo = open("mytext.txt",'r')
'''
fo.write("this is line1: ")
fo.write("this is line2: ")
'''
'''
s=fo.readlines(1)
print(s)


for i in range(3):
 x = input("enter no:")
 y = input("enter name:")
 z = input("enter age:")
 str = (x + "," + y + "," + z +"\n")
 fo.write(str)
'''
fo = open("mytext.txt",'r')
for line in fo.readlines():
    if i % 2 == 0 :
        print(line)
    i += 1

fo.close()
