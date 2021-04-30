from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
class Movies:
    def __init__(self,name):
        self.engine = create_engine('sqlite:///{}.db'.format(name), echo = True)
        self.meta = MetaData()
        self.filmy = Table(
           '{}'.format(name), self.meta,
           Column('id', Integer, primary_key = True),
           Column('tytul', String),
           Column('rezyser', String),
           Column('actorzy',String),
           Column('Platforma',String),
        )
        self.meta.create_all(self.engine)

    def delete_movie(self,tytul):
        conn = self.engine.connect()
        stmt = self.table.delete().where(self.table.c.tytul == tytul)
        conn.execute(stmt)

    def add_movie(self, tytul, rez, actorzy, platforma):
        ins = self.table.insert().values(tytul=tytul, rezyser=rez, aktorzy= actorzy, platforma=platforma)
        conn = self.engine.connect()

t = Movies('filmy')