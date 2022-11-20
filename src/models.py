from sqlalchemy import Date, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class BaseModel(Base):

    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id}"


class Reader(BaseModel):
    __tablename__ = "readers"

    name = Column(String)
    telephone = Column(String)
    address = Column(String)
    # books = relationship("Books", back_populates="readers")
    # givings = relationship("Givings", back_populates="readers")


class Book(BaseModel):
    __tablename__ = "books"

    name = Column(String)
    author = Column(String)
    year = Column(Integer)
    price = Column(Integer)
    quantity = Column(Integer)
    publishings_id = Column(Integer, ForeignKey("publishings.id"))
    # publishings = relationship("Publishings", back_populates="books")
    # readers = relationship("Readers", back_populates="books")

class Publishing(BaseModel):
    __tablename__ = "publishings"

    name = Column(String)
    city = Column(String)

    # books = relationship("Books", back_populates="publishings")


class Giving(BaseModel):
    __tablename__ = "givings"

    readers_id = Column(Integer, ForeignKey("readers.id"))
    books_id = Column(Integer, ForeignKey("books.id"))
    data = Column(Date)
    list = Column(String)

    # readers = relationship("Readers", back_populates="givings")

