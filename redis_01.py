import redis
r = redis.Redis(host='172.16.80.210',port=6379)

# r.set('name','yuanzy')
# print r.get('name')


# import redis
#
# pool = redis.ConnectionPool(host='172.16.80.210',port=6379)
# r = redis.Redis(connection_pool=pool)
# r.set('name',123)
# print r.get('name')


# import redis
# r = redis.Redis('172.16.80.210',6379)
# r.mset({'k1':'v1','k2':'v2'})
# print r.mget('k1','k2')

# import redis
# r = redis.Redis('172.16.80.210',6379)
# r.incr('age',1)    #decr
# print r.get('age')

# import redis
# r = redis.Redis('172.16.80.210',6379)
# r.append('name','1994')
# print r.get('name')

# r.hset('xb','sex','M')
# r.hset('xb','age',19)  #hmset
# print r.hget('xb','sex')
# print r.hget('xb','age')   #hmget

#from: http://www.cnblogs.com/wupeiqi/articles/5132791.html

while True:
    pub = r.pubsub()
    pub.subscribe('ccav')
    pub.parse_response()
    print pub.parse_response()


