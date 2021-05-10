import requests
import json
import time
from datetime import datetime


url = 'http://api.nbp.pl/api/exchangerates/rates/a/usd/'

# funkcja pobierająca aktualny kurs dolara
def readCurrency(adres):
    print("---------------------------------------")
    try:
        r = requests.get(adres)
        data = r.json()
        cur = data['rates'][0]['mid']
        print("Kurs dolara: ", cur)
    except TimeoutException:
        print('Blad pozyskania danych')

# funkcja mierząca czas wykonania fukcji readCurrency wraz z podaniem aktualnej daty
def timeMeasure():
    start = time.time()
    readCurrency(url)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Data i godzina: ", dt_string)
    print ('Czas wykonania zapytania: %.2f sekund' % (time.time() - start))

#funckja wywolująca timeMeasure 5 razy co 12 sekund
def InterLoop():
    for i in range(0,5):
        timeMeasure()
        time.sleep(15.0)

InterLoop()