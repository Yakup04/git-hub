sayi=int(input(""))
if sayi > 2 :
     for i in range(2,sayi) :
         if (sayi%i)==0 :
             print(f"{sayi} is not prime number")
             break
         else:
             print(f"{sayi} is prime number")    
             break