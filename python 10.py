classes=50
atd=int(input("attended class"))
atten=(atd/classes)*100
if(atten>75):
    print("the percentage of attendance is",atten)
    print("allowed to attend examination")
else:
    print("the percentage of attendance is",atten)
    print("not allowed to attend examination")
