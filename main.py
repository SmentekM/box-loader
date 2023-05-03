liczba_elemntów = int(input('Podaj ilość elementów: '))
WAGA_PACZKI = 20
liczka_paczek = 0
waga_paczki = 0
waga_elemtow = 0
suma_elemetów_w_paczce = 0
najwieksza_liczba_pustych_kg = 1
najwiecej_pustych_kg_w_paczce = 1

for element in range(liczba_elemntów):
    waga = int(input('Podaj wage elemntu: '))
    if waga < 1 or waga > 10:
        print('Zła waga elementu!')
        break
    waga_paczki += waga
    waga_elemtow += waga
    suma_elemetów_w_paczce += 1
    if waga_paczki == 20:
        liczka_paczek += 1
        puste_kg_w_paczce = 20 - waga_paczki
        print(f'waga paczki : {waga_paczki}, ile elementów: {suma_elemetów_w_paczce}, nr: {liczka_paczek}/'
              f'puste kg: {puste_kg_w_paczce}')
        waga_paczki = 0
        suma_elemetów_w_paczce = 0
    if waga_paczki > 20:
        liczka_paczek += 1
        waga_paczki = waga_paczki - waga
        puste_kg_w_paczce = 20 - waga_paczki
        suma_elemetów_w_paczce -= 1
        if puste_kg_w_paczce > najwieksza_liczba_pustych_kg:
            najwieksza_liczba_pustych_kg = puste_kg_w_paczce
            najwiecej_pustych_kg_w_paczce = liczka_paczek


        print(f'waga paczki : {waga_paczki}, ile elementów: {suma_elemetów_w_paczce}, nr: {liczka_paczek}/'
              f'puste kg:{puste_kg_w_paczce}')
        waga_paczki = waga
        suma_elemetów_w_paczce = 1

if waga_paczki < 20:
    liczka_paczek += 1
    puste_kg_w_paczce = 20 - waga_paczki
    if puste_kg_w_paczce > najwieksza_liczba_pustych_kg:
        najwieksza_liczba_pustych_kg = puste_kg_w_paczce
        najwiecej_pustych_kg_w_paczce = liczka_paczek

    print(f'ile elementów: {suma_elemetów_w_paczce}, nr: {liczka_paczek}/'
          f'puste kg: {puste_kg_w_paczce}')

print(f' PODSUMOWANIE: \n > Łącznie wysłano paczek: {liczka_paczek:}\n '
      f'> Wysłano łącznie elementów o wadze: {waga_elemtow} kg\n '
      f'> Suma pustych wysłanych kilogramów: {liczka_paczek* 20 - waga_elemtow} kg\n'
      f'> Najwiecej pustych kilogramów jest w paczce nr: {(najwiecej_pustych_kg_w_paczce)}[{najwieksza_liczba_pustych_kg}kg]')
