class User:
    def __init__(self, userId: int, userLogin: str, userEmail: str):
        self._userId = userId
        self._userLogin = userLogin
        self._userEmail = userEmail
        self._isUserActive = True

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
