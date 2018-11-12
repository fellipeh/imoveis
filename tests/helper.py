from app import app, db


def register(self, username, password):
    return self.app.post(
        '/user/register',
        data=dict(username=username, password=password),
        follow_redirects=True
    )


def login(self, email, password):
    return self.app.post(
        '/user/login',
        data=dict(email=email, password=password),
        follow_redirects=True
    )


def logout(self):
    return self.app.get(
        '/user/logout/access',
        follow_redirects=True
    )
