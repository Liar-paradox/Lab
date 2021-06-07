from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
class Movies:
    def __init__(self,name):
        self.engine = create_engine('sqlite:///{}.db'.format(name), echo = True)
        self.meta = MetaData()
        self.table = Table(
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
        x = self.table.select()
        conn.execute(x).fetchall()

    def add_movie(self, tytul, rez, actorzy, platforma):
        conn = self.engine.connect()
        ins = self.table.insert().values(tytul=tytul, rezyser=rez, aktorzy= actorzy, platforma=platforma)
        conn.execute(ins)
    def show_film(self):
        conn = self.engine.connect()
        show = self.table.select
        res = conn.execute(show)
        for x in res:
            print(f'Film: {x[1]}, Reżyser: {x[2]}, Aktorzy: {x[3]}, platforma: {x[4]}')


t = Movies('filmy')

t.add_movie('title1','director1','actors1','vod1')
t.show_film()
t.delete_movie('title1')
t.show_film()