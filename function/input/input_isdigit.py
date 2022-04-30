
sayi = input("bir sayi giriniz:")

while not sayi.isdigit():
    print("üzgünüm bu bir sayi değildir.")
    sayi = input("bir sayi giriniz:")

else :
    print("tebrikler bir sayi girdiniz ve bir sonraki aşamaya geçmeye hak kazandınız!")

    girdi= input("bir sonraki aşamaya geçmek istiyorsanız 1' e basınız, istemiyorsanız 2'ye basınız.")
    if girdi== "1" :
        print("ödülü almak için geçerli bir sayi daha girmeniz gerekmekte")
        odul_sayisi= input("ödül almak için geçerli bir sayi giriniz:")
        while not odul_sayisi.isdigit():
            print("üzgünüm bu bir sayi değildir.")
            odul_sayisi = input("bir sayi giriniz:")
        else :
            print("Tebrikler geçerli bir sayi daha girdiniz ve ödülü aldınız.")

    else:
            print("çıkış yaptınız:")
