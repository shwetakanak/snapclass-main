"""f=open("module_5/sample.txt","r") #returns  file object
#data=f.read()
data=f.readline() #reads line by line
#print(type(data))
print(data)
f.close()"""

#search if python exist or not and line number
data=True
line=1
word="Python"
with open("module_5/sample.txt","r") as f:
    while data:
        data=f.readline()
        if(word in data):
            print(f"{word} Word found at line {line}")
            break
   # print(data)
        line+=1