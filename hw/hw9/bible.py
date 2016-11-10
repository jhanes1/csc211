
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///bible.sqlite')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Verse(Base):
    __tablename__ = 'verses'
    id = Column(Integer, primary_key=True)
    book = Column(String)
    chapter = Column(Integer)
    verse = Column(Integer)
    text = Column(String)
    def __repr__(self):
        return "<Verse(book='{}',chapter='{}',verse='{}',text='{}')>".\
        format(self.book,self.chapter,self.verse,self.text)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

from functools import lru_cache
import gzip, csv
memoize = lru_cache(1)
@memoize
def read_bible():
    cols = ['book','chapter','verse','text']
    with open('bible.tsv','rt') as rfp:
        reader = csv.DictReader(rfp,cols,delimiter='\t')
        verses = list(reader)
    return verses

bibHolder = read_bible()
#{'chapter': '0',
#'text': 'And the earth was without form, and void; and darkness [was] upon the face of the deep. And the Spirit of God moved upon the face of the waters. @',
#'book': 'genesis',
#'verse': '1'}
index = 0
for item in bibHolder:
    iHold = index
    cHold = int(item['chapter'])
    tHold = item['text']
    bHold = item['book']
    vHold = int(item['verse'])

    tempH = Verse(id = iHold, book = bHold, chapter = cHold, verse = vHold, text = tHold)
    session.add(tempH)

    index += 1

session.commit()
