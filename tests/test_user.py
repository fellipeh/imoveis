import unittest

from app import app, db


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_imoveis.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    def test_registration(self):
        info = dict(username='test', password='test')
        response = self.app.post('/user/register', data=info, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_login(self):
        self.test_registration()

        info = dict(username='test', password='test')
        response = self.app.post('/user/login', data=info, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_fail_login(self):
        info = dict(username='test2', password='test2')
        response = self.app.post('/user/login', data=info, follow_redirects=True)

        self.assertEqual(response.status_code, 500)

    def test_get_valid_jwt_auth(self):
        self.test_registration()

        info = dict(username='test', password='test')
        response = self.app.post('/user/login', data=info, follow_redirects=True)
        jwt_res = response.json['access_token']

        self.assertIsNotNone(jwt_res)

if __name__ == "__main__":
    unittest.main()
