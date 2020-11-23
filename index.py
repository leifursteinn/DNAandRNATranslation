spulla = str(input("ertu að nota DNA eða RNA: "))
if spulla == "DNA":
    y = "T"
else: 
    y = "U"
txt = str(input(""))
x = 0
txt1 = []

for i in range(len(txt)):
    if txt[x] == "A":
        txt1.insert(x, y)
        x+=1
    elif txt[x] == y:
        txt1.insert(x, "A")
        x+=1
    elif txt[x] == "G":
        txt1.insert(x, "C")
        x+=1
    elif txt[x] == "C":
        txt1.insert(x, "G")
        x+=1
    
print(''.join(txt1))
