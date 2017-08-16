import redis

r = redis.Redis(host='172.16.80.210',port=6379)
while True:
    messages = raw_input(">>:")
    r.publish("ccav",messages)