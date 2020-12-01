import threading
import requests

def func1(link):
    r = requests.get(link)
    if (r.text)== str({}):
        print(link, "доступен")
    else:
        print(link, "не доступен")

hosts = ['https://api.binance.com/api/v1/ping', 'https://ru.wikipedia.org/wiki/Ping', 'http://cs.mipt.ru', 'https://translate.yandex.ru/?lang=ru-en&text=ссылка', 'https://yandex.ru/search/?text=ping()%20в%20питоне&lr=213&clid=2270455&win=348']

threads = [threading.Thread(target = func1, args = (hosts[i], )) for i in range(len(hosts))]
for thread in threads:
    thread.start()


