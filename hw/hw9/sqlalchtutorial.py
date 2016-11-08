%logstart -ot sqlalchemy.log

import sqlalchemy
sqlalchemy.__version__

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:',echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='{}',fullname='{}',password='{}')>".format(self.name,self.fullname,self.password)

User.__table__
Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
ed_user.name
ed_user.password
str(ed_user.id)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
our_user

ed_user is our_user

session.add_all([
User(name='wendy',fullname='Wendy Williams',password='foobar')
User(name='mary',fullname='Mary Contrary',password='xxg527')
User(name='fred',fullname='Fred Flinstone',password='blah')
])

ed_user.password = 'f8s7ccs'

session.dirty
session.new
session.commit()
ed_user.id

ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser',fullname='Invalid',password='12345')
session.add(fake_user)
session.query(User).filter(User.name.in_(['Edwardo','fakeuser'])).add()
session.rollback()
ed_user.name
fake_user in session
session.query(User).filter(User.name.in_(['ed','fakeuser'])).all()
