
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('bible.sqlite')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Verse(Base):
    id = Column(Integer, primary_key=True)
    book = Column(String)
    chapter = Column(Integer)
    verse = Column(Integer)
    text = Column(String)
    def __repr__(self):
        return "<Verse(book='{}',chapter='{}',verse='{}',text='{}')>".\
        format(self.book,self.chapter,self.verse,self.text)

from functools import lru_cache
import gzip, csv
memoize = lru_cache(1)
@memoize
def read_bible():
    cols = ['book','chapter','verse','text']
    with gzip.open('/home/jhanes/csc211/hw/hw2/bible.tsv.gz','rt') as rfp:
        reader = csv.DictReader(rfp,cols,delimiter='\t')
        verses = list(reader)
    return verses

print(read_bible())
