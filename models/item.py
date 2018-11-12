# -*- coding: utf-8 -*-

from app import db


class ItemModel(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text(120), nullable=True)
    price = db.Column(db.Float, nullable=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'title': x.title,
                'description': x.description,
                'price': x.price
            }

        return {'items': list(map(lambda x: to_json(x), ItemModel.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except Exception as e:
            return {'message': str(e)}
