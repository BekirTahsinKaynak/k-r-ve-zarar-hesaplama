
gelirler = []

giderler = []



def gelir_girme():

    a = True

    print('Lütfen Gelirlerinizi Tek Tek Giriniz. \nDeğerlerinizi Girmeyi Bitirdiğinizde 00 Girerek Çıkabilirsiniz.')

    while (a):

        gelir_degeri = int(input('Gelir: '))

        if(gelir_degeri == 00):

            a = False

        else:

            gelirler.append(gelir_degeri)

            pass

    print('-'*60)



def gider_girme():

    b = True

    print('Lütfen Giderlerinizi Tek Tek Giriniz. \nDeğerlerinizi Girmeyi Bitirdiğinizde 00 Girerek Çıkabilirsiniz.')

    while (b):

        gider_degeri = int(input('Harcamalar: '))

        if(gider_degeri == 00):

            b = False

        else:

            giderler.append(gider_degeri)

            pass

    print('-'*60)



def kar_hesaplama():

    toplam_gelir = sum(gelirler)

    toplam_gider = sum(giderler)

    toplam_gider *= -1



    kar = toplam_gelir + toplam_gider

    if(kar>0):

        print('Toplam Geliriniz ${}, Toplam Gideriniz ${}, Yaptığınız Kâr ${}'.format(toplam_gelir, toplam_gider, kar))

    elif(kar == 0):

        print('Toplam Geliriniz ${}, Toplam Gideriniz ${}, Kâr Veya Zarar Yapmadınız.'.format(toplam_gelir, toplam_gider))

    else:

        print('Toplam Geliriniz ${}, Toplam Harcamalarınız ${}, Yaptığınız Zarar ${}'.format(toplam_gelir, toplam_gider, kar))

    

gelir_girme()

gider_girme()

kar_hesaplama()