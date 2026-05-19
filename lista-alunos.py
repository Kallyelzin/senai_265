print("champions in top 5")
print("TOP 1 ItzRealMe, TOP 2 Marloww, TOP 3 ClownPierce, TOP 4 JudeLow, TOP 5 Ryo")
ps_champions = input("What this champion you search? ")
champions = ["Ryo", "Marloww", "Clownpierce", "Judelow", "TtzRealMe"]

for i in champions:
    if i == ps_champions:
        print("This champion is on!")
        break
else:
    print("This champion is of")