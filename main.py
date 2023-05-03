liczba_elemntów = int(input('Podaj ilość elementów: '))
WAGA_PACZKI = 20
liczka_paczek = 0
waga_paczki = 0
waga_elemtow = 0
suma_elemetów_w_paczce = 0

for element in range(liczba_elemntów):
    waga = int(input('Podaj wage elemntu: '))
    if waga < 1 or waga > 10:
        print('Zła waga elementu!')
        break
    waga_paczki += waga
    waga_elemtow += waga
    suma_elemetów_w_paczce += 1
    # print(f'waga paczki: {waga_paczki}')
    # print(f'waga paczki: {waga_paczki}, waga łączna: {waga_elemtow}, ilosc elen: {suma_elemetów_w_paczce}')
    if waga_paczki == 20:
        liczka_paczek += 1
        print(f'waga paczki : {waga_paczki}, ile elementów: {suma_elemetów_w_paczce}, nr: {liczka_paczek}')
        waga_paczki = 0
        suma_elemetów_w_paczce = 0
    if waga_paczki > 20:
        liczka_paczek += 1
        waga_paczki = waga_paczki - waga
        suma_elemetów_w_paczce -= 1
        print(f'waga paczki : {waga_paczki}, ile elementów: {suma_elemetów_w_paczce}, nr: {liczka_paczek}')
        # print(f'waga paccki: {waga_paczki}')
        waga_paczki = waga
        suma_elemetów_w_paczce = 1
        # print(f'dodano paczke: {liczka_paczek}')
        # print(f'waga paczki: {waga_paczki}')
if waga_paczki < 20:
    liczka_paczek += 1
    print(f'ile elementów: {suma_elemetów_w_paczce}, nr: {liczka_paczek}')

print(f' waga łączna: {waga_elemtow}, wysłano paczek : {liczka_paczek}/'
      f'liczba pustych kilogramów: {liczka_paczek* 20 - waga_elemtow}')
