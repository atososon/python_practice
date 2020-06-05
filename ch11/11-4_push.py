import redis
conn = redis.Redis()
print('Pusher is starting')
chocoes = ['choco1', 'choco2', 'choco3', 'choco4']
for choco in chocoes:
   msg = choco.encode('utf-8')
   conn.rpush('chocoes', msg)
   print('Pushed',choco)
conn.rpush('chocoes', 'quit')
print('Pusher is done')