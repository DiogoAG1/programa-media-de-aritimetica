bm1 =float(input("Digite o primeiro bimestre:"))
bm2 =float(input("Digite o segundo bimestre:"))
bm3 =float(input("Digite o terceiro bimestre:"))
bm4 =float(input("Digite o quarto bimestre:"))
media = bm1 + bm2 + bm3 + bm4
print (f"Sua nota final é : {media/4}")
media2 = (media/4)
if media2 >= 9:
    print ("Aprovado com louvor!")
elif media2 >= 7:
     print ("Aprovado")
elif media2 < 7:
     print ("Reprovado")
