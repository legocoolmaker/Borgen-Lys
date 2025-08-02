while True:
  l = input("Skriv in de 4 verdiene: ").split(",")
  l = [int(x) for x in l]

  

  print(f"[[{(l[0]/2000):.4f},{(l[1]/2000):.4f}],[{(l[2]/1120):.4f},{(l[3]/1120):.4f}]]")