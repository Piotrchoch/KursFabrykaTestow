import requests
import json
import time
from datetime import datetime
import csv

file = open('OdczytWaluty.csv', 'w', newline='')
writer = csv.writer(file, delimiter=';')
writer.writerow(["Kurs USD", "Data odczytu", "Godzina odczytu", "Czas wykonania zapytania"])
newline = []

url = 'http://api.nbp.pl/api/exchangerates/rates/a/usd/'

# funkcja pobierająca aktualny kurs dolara
def readCurrency(adres):
    print("---------------------------------------")
    newline.clear()
    try:
        r = requests.get(adres)
        data = r.json()
        cur = data['rates'][0]['mid']
        print("Kurs dolara: ", cur)
        newline.append(cur)
        return newline

    except TimeoutException:
        print('Blad pozyskania danych')
        newline.append('Blad')
        print(newline)


# funkcja mierząca czas wykonania fukcji readCurrency wraz z podaniem aktualnej daty
def timeMeasure():
    start = time.time()
    readCurrency(url)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")
    hr_string = now.strftime("%H:%M:%S")
    print("Data i godzina: ", dt_string, " ", hr_string)
    newline.append(dt_string)
    newline.append(hr_string)
    zapCzas = time.time() - start
    print ('Czas wykonania zapytania: %.2f sekund' % zapCzas)
    newline.append(zapCzas)
    print(newline)
    writer.writerow(newline)

#funckja wywolująca timeMeasure 5 razy co 2 sekund
def InterLoop():
    for i in range(0,5):
        timeMeasure()
        time.sleep(2.0)

InterLoop()

