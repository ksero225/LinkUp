class User:
    def __init__(self, userId: int, userLogin: str, userEmail: str, userFriendList: list):
        self._userId = userId
        self._userLogin = userLogin
        self._userEmail = userEmail
        self._isUserActive = True
        self._userContacts = userFriendList

    def get_user_id(self):
        return self._userId

    def get_user_login(self):
        return self._userLogin

    def get_user_email(self):
        return self._userEmail

    def get_is_user_active(self):
        return self._isUserActive

    def get_user_contacts(self):
        return self._userContacts

    def set_user_id(self, user_id):
        self._userId = user_id

    def set_user_login(self, user_login):
        self._userLogin = user_login

    def set_user_email(self, user_email):
        self._userEmail = user_email

    def set_is_user_active(self, is_user_active):
        self._isUserActive = is_user_active

    def set_user_contacts(self, user_contacts):
        self._userContacts = user_contacts
