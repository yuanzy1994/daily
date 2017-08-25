from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://root:passwd@172.16.80.210:3306/zabbix",)


result = engine.execute("select * from users")
print result.fetchall()