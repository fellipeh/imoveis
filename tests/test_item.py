import os
import unittest

from app import app, db


class ItemTests(unittest.TestCase):
    info_new_item = dict(title="House 1",
                         description="Description of House 1",
                         price=100600
                         )

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_imoveis.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    def test_insert_item_without_auth(self):
        response = self.app.put('/items', data=self.info_new_item, follow_redirects=True)

        self.assertEqual(response.status_code, 401)

    def test_insert_item_with_auth(self):

        # register the user and get the auth key.
        info = dict(username='test', password='test')
        response = self.app.post('/user/register', data=info, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        if 'access_token' in response.json:
            jwt_res = response.json['access_token']
        else:
            self.assertRaises('no jwt auth key')

        hd = {'Authorization': 'Bearer ' + jwt_res}

        response = self.app.put('/items', headers=hd, data=self.info_new_item, follow_redirects=True)

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
