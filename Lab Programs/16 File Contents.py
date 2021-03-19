sfilename=input("source filename:")
dfilename=input("Destination filename:")
f1=open(sfilename,'r')
f2=open(dfilename,'w')
for line in f1.readline():
    f2.write(line)
print("file copied successful")
f1.close()
f2.close()