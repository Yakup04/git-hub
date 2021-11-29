sayi=float(input())
ars=str(sayi)
ars_list=[]
 if sayi>0 and type(sayi)== int:
    for i in ars:
        i=int(i)**len(ars)
        ars_list.append(i)
        ars_sayi=sum(ars_list)
        if ars_sayi == sayi :
             print("Bu sayi bir Armstrong sayisidir :",sayi)
        else:
             print("Bu sayi Armstrong sayisi degildir : ",sayi)    
    
 else :    
     print("Gecersiz sayi girisi")