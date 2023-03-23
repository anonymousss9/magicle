from datetime import datetime
import datetime
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.dialects.postgresql import insert
import sqlalchemy
from sqlalchemy import desc



class DatabaseData:
    schema = 'data'

    def __init__(self):
        self.init_database()

    def init_database(self):
        self.engine = create_engine('postgresql://postgres:password1@localhost:5432/data')
        meta = MetaData()
        meta.reflect(bind=self.engine)
        self.linkedin = meta.tables['linkedin_data']
        self.test = meta.tables['test']


    def insert_data(self, data):
        ins_stmt = insert(self.linkedin).values(data)
        do_nothing_stmt = ins_stmt.on_conflict_do_nothing(index_elements=['linkedin_url'])
        result = self.engine.execute(do_nothing_stmt)

