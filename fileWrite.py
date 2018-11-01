# https://www.guru99.com/reading-and-writing-files-in-python.html

f= open("guru99.txt","w+")
for i in range(20):
     f.write("This is line %d\r\n" % (i+1))
f.close()
