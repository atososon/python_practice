import redis
from time import sleep
from datetime import datetime

conn = redis.Redis()
print('Poper is starting')
while True:
   sleep(0.5)
   msg = conn.blpop('chocoes')
   if not msg:
       break
   val = msg[1].decode('utf-8')
   if val == 'quit':
       break
   print('Poped', val, 'at', datetime.now(), 'remaining amount:', max(0,conn.llen('chocoes')-1))

print('Chocoes are poped')