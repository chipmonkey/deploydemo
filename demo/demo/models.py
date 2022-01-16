from demo import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    first = db.Column(db.String())
    last = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    @classmethod
    def init_v2(cls, first, last):
        result = cls(first + ' ' + last)
        result.first = first
        result.last = last
        return result
        

    def __repr__(self):
        return f"<id: {self.id}, name: {self.name}>"

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'name'       : self.name,
           'first'      : self.first,
           'last'       : self.last
       }
