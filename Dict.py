#creating a dictionery
Data = {"name":"Humera", "age":26, "degree":"Ai", "gender":"female"}
#print(Data)

#creating dictinery with different data type
info = {"name":"Humera", "age":26, "height":5.2}
#print(info)

#Adding elements in dictionery
info = {"name":"Humera", "age":26, "height":5.2}
info["degree"] = "m.com"
#print(info)

#updating dictionery
info = {"name":"Humera", "age":26, "height":5.2}
info["age"] = 28
#print(info)

#Deleting element in a dictionery
info = {"name":"Humera", "age":26, "height":5.2}
del info["height"] 
#print(info)

#Deleting element by using pop function 
info = {"name":"Humera", "age":26, "height":5.2}
info.pop("name") 
#print(info)

#Built in dictionery functions
#Find the length of dict
info = {"name":"Humera", "age":26, "height":5.2}
#print(len(info))

#compare the elements of dict
#print(cmp(Data,info))


#convert dict into text form
#print(str(info))
 
#del dictionery
#print(info.clear())

#del entire dict
del info
print(info)

