import redis
conn = redis.Redis()
print(conn.delete('test'))
print(conn.hmset('test', {'count':1, 'name':'Fester Beatertester'}))
print(conn.hgetall('test'))