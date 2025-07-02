print("Eslatma agar ism kiritishni hohlamsangiz 'chiqish' deb yozing")
c=str
lst=[]
while c!="chiqish":
    c=input("  ")
    if c!="chiqish":
        lst.append(c)
else:
    print(lst)
    print(f"Shuncha ism bor: {len(lst)}")