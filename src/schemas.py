from pydantic import BaseModel
from datetime import date


class BookBase(BaseModel):

    name: str
    author: str
    year: int
    price: int
    quantity: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    publishings_id: int

    class Config:
        orm_mode = True


class ReaderBase(BaseModel):

    name: str
    telephone: int
    address: str


class ReaderCreate(ReaderBase):

    pass


class Reader(ReaderBase):

    id: int
    #book: list[Book]=[]

    class Config:

        orm_mode = True


class PublishingBase(BaseModel):


    name: str
    city: str


class PublishingCreate(PublishingBase):

    pass


class Publishing(PublishingBase):

    id: int


    class Config:

        orm_mode = True


class GivingBase(BaseModel):

    readers_id: int
    books_id: int
    data: date



class GivingCreate(GivingBase):
    pass


class Giving(GivingBase):
    id: int
    list: str

    class Config:
        orm_mode = True

