import redis
conn = redis.Redis()
print(conn.hincrby('test','count',3))
print(conn.hget('test','count'))