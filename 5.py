
LUOTI_GRAMMOINA = 13.3
NAULA_LUOTEINA = 32
LEIVISKA_NAULOINA = 20

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

kokonaisluodit = (leiviskat * LEIVISKA_NAULOINA * NAULA_LUOTEINA) + (naulat * NAULA_LUOTEINA) + luodit
kokonaisgrammat = kokonaisluodit * LUOTI_GRAMMOINA

kilogrammat = int(kokonaisgrammat // 1000)
grammat = kokonaisgrammat % 10

print(f"Massa nykymittojen mukaan:\n{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")



