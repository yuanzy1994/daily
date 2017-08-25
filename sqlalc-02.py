from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(20)),
             )

color = Table('color', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(20)),
              )

engine = create_engine("mysql+mysqldb://root:root@172.16.80.210:3306/duiba",)
metadata.create_all(engine)