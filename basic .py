print("komal ji")
#varibels
a=6
print(type(a))
#string
kuku="radhe radhe"
print(kuku)
print(type(kuku))
#indexing
print(kuku[2])
print(kuku[-1])
print(kuku[::-1])
print(kuku[1::3])
#string method
k="    ram ram ji "
print(k.upper())
print(k.lower())
print(k.strip())#use for remove the blank space befor the string
print(k.split())
print(k.replace("ram","trip"))#use for replace word
print(k.find("ram"))#use to find any element and give the index
print(k+ kuku)#concatination of sting(add)
print(k+ " "+kuku)#this method use for add the space between two string
#also sting is imutable/not changeble 
#tupples
tupple=("rj","ten",45,67,True)#use"()"  this for create tupple
t=("tina")
print(tupple)
print(tupple[-1])
print(tupple[:2:])
print(tupple[::1])
#print(tupple.insert( -1,"tina"))# show's that tupple store not changeble data
print(t* 3)
print(tupple.count(2))
print(tupple.count("rj"))
#list
laj=["kan","ankh","67",89,90.8,True]
print(laj)
print(laj[::-1])#inverse
print(laj[-5])
print(laj[1:4])
print(laj.append(4))
laj.insert(2,3)#use for the insert the element in list( element knhi bhi insert ho sakte h)
print(laj)
laj.remove(3)#remove specific element
print(laj)
laj.pop()#pop last element
print(laj)
lal=[3.,566.6,34,67,98]
lal.sort()
print(lal)