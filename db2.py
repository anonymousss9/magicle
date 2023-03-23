from datetime import datetime
import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.dialects.postgresql import insert
import sqlalchemy
from sqlalchemy import desc
from sqlalchemy import create_engine,update


class JuggleDatabase:
    schema = 'data'

    def __init__(self):
        self.init_database()

    def init_database(self):
        self.engine = create_engine('postgresql://postgres:password1@localhost:5432/data')
        meta = MetaData()
        meta.reflect(bind=self.engine)
        self.test = meta.tables['test']


    #def insert_test(self, test):
    #    ins_stmt = self.coins_prices.insert().values(test)
    #    self.engine.execute(ins_stmt)

    def insert_test(self, name):
        ins = self.test_table.insert().values(name)
        with self.engine.connect() as conn:
            conn.execute(ins)
