alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_KG = 'АБВГДЕЁЖЗИЙКЛМНҢОӨПРСТУҮФХЦЧШЩЬЪЫЭЮЯАБВГДЕЁЖЗИЙКЛМНҢОӨПРСТУҮФХЦЧШЩЬЪЫЭЮЯ'
smeshenie = int(input('Шаг шифровки: '))
message = input("Сообщение для ДЕшифровки: ").upper()
itog = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i
if lang == 'EU':
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
if lang == 'KG':
    for i in message:
        mesto = alfavit_KG.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_KG:
            itog += alfavit_KG[new_mesto]
        else:
            itog += i
print (itog)
