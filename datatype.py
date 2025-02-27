#dictionary
dic={"name":"komal","age":19}
print(dic,type(dic))
dic.values()
dic.keys()
print(dic.get("name"))
print(print("hello"))
print(True+True+False)
#print="komal"
#print(print)=give the error
#print="komal"\normal   print karvane pr run ho jayega (in juypter)
print(dic["name"])
print(dic.items())
dic["city"]="jaipur"
dic.update({"name":"preeto"})
print(dic)
a,b,c,d=(1,2,3,4) #this is an int. data type
print(b,type(b))
b=1,2,3 #this is an iupple data type
print(b,type(b))


#arithmatic operations
k=9
p=4
n=5
print(p+n+k)
print(p*n)
print(k-p)
print(k/n)
print(k**n)
print(k//n)

#cOMPARISION OPERATERES
print(k==n)
print(k!=n)
print(k>n)
print(k<n)
print(k>=n)
print(k<=n)

#assignment opertors
k=3
k+=5
print(k)
k*=9
print(k)
k/=n
print(k)
k%=n
print(k)
print(k//n)

#logical operators
#and ,or,not
print(k<n and k>n)
print( p&n)
print(p^n)
#identiy operators
print(k is n)
print(k  is not n)

#membership operators
f=[1,2,3]
print(2 in f)
print(2 not in f)

#conditional satetments
#keywords:if,else,elif

# age=90
# if (age>78):
#     print("hello")
# elif(age==60):
#      print("you are ready to enter in old stage")
# else:
#      print("world")
# marks=input(print("plese enter your marks"))
# if(marks=>85):
#      print("you get a+ grade")
# elif(marks=<50):
#      print("you get c grade")
# elif(marks=>50):
#      print("you get b grade")
# elif(marks=>90):
#       print("you get a++ grade")



#for 
print(dic)
for i in dic.items():
    print(i)
for j in dic.keys():
    print(j)

# l=[1,2,3,4,]
# for h in l:
#     print(h)
#     if(h==3):
#         break
    
l=[1,2,3,4,]
for h in l:
    
    if(h==2):
        continue
    print(h)


#while loop
count=0
while (count<=6):
    print(count)
    count+=1