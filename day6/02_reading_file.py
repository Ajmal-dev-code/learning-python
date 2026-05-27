file = open("notes.txt","r")
#this open file if it exist other wise error shows
content = file.read()# to read the content
print(content)
file.close()#necessory other wise file will open 