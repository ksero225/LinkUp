class User:
    def __init__(self):
        self._userId = None
        self._userLogin = None
        self._userEmail = None
        self._isUserActive = None

    def get_user_id(self):
        return self._userId

    def get_user_login(self):
        return self._userLogin

    def get_user_email(self):
        return self._userEmail

    def get_is_user_active(self):
        return self._isUserActive

    def set_user_id(self, user_id):
        self._userId = user_id

    def set_user_login(self, user_login):
        self._userLogin = user_login

    def set_user_email(self, user_email):
        self._userEmail = user_email

    def set_is_user_active(self, is_user_active):
        self._isUserActive = is_user_active
