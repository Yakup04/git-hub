def fibonacci(sinir) :
    sinir = int(input("Lütfen bir sayi giriniz :"))
    sinir=sinir+1
    list=[]
    n=0
    for i in range(sinir) :
        sonuc = ((((1+5**0.5)/2)**n) - (((1-5**0.5)/2)**n))/(5**0.5)
        if sonuc <= sinir:
                n = n + 1
                list.append(int(sonuc))     
    print(list)

fibonacci(55)