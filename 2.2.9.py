from time import sleep

headers_stor = {}

sources = ["bing.com",
           "google.ru",
           "yahoo.com",
           "mail.ru",
           "ya.ru"]


def get_request_header(url: str):
    # моделируем различное время ответа от ресурсов
    if url == "yahoo.com":
        sleep(10)
    elif url == "mail.ru":
        sleep(1.8)
    elif url == "google.ru":
        sleep(0.2)
    else:
        sleep(1.4)
    headers_stor[url] = "ok"


import threading

threads=[]
for source in sources:
    headers_stor[source]='no_response'
    thread=threading.Thread(target=get_request_header, args=(source,), daemon=True)
    threads.append(thread)
    thread.start()

sleep(1.5)



# Работа тестирующей системы:
for url, headers in sorted(headers_stor.items()):
    print(f"{url}: {headers}")