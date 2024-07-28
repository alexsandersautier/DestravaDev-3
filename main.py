import schedule
from scrapy import execute
from worksheet import generate

def init():
    product, price, date, link = execute()
    generate([product, price, date, link])

schedule.every(30).minutes.do(init)
print(f'próxima consulta às {schedule.next_run()}')
while True:
    schedule.run_pending()