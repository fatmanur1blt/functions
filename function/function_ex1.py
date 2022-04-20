sayilar=[1,2,3,4,5]

for index,sayi in enumerate (sayilar):
    print("{} sayisinin karesi: {}".format(index+1,sayi*sayi))

#fonksiyon örneği
def ilk_fonksiyon () :
    print("merhaba dünya")
ilk_fonksiyon ()

def bes_dondur():
    print(5)
bes_dondur()

liste1= [1,3,7,9,109,2]
liste2= ["f","a","t","m","a"]

def ilk_liste():
    print("İlk liste sıralanıyor...")
    print(sorted(liste1))
    print("ilk liste sıralandı...")
    print("------")

def ikinci_liste():
    print("ikinci liste sıralanıyor...")
    print(sorted(liste2))
    print("ikinci liste sıralandı...")
    print("------")

while True:
      print("1.liste:",liste1)
      print("2.liste:", liste2)

      secim= int(input("hangi listeyi sıralamak istersiniz (çıkmak için 3 ):"))
      if secim==1:
        ilk_liste()
      elif secim==2:
        ikinci_liste()
      elif secim==3:
        break
      else:
        print("hatalı tuşlama yaptınız")