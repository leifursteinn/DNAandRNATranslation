spulla = str(input("ertu að nota DNA eða RNA: "))
if spulla == "DNA":
    y = "T"
elif spulla == "RNA": 
    y = "U"
else:
    print("neitun yrðingar")

if spulla == "RNA" or "DNA":
    txt = str(input("Óþýdd Kirni: "))
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
        
    print("Þýdd Kirni:", ''.join(txt1))
