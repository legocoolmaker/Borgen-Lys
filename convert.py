l = input("Skriv in de 4 verdiene: ").split(",")
l = [int(x)/2000 if int(x)>2 else int(x)/1200 for nr,x in enumerate(l)]
print([[l[0],l[1]],[l[2],l[3]]])

