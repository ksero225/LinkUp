import requests
from config import contact_link

class ContactService:
    @staticmethod
    def add_contact(user, contact_login):
        api_link = contact_link(user.get_user_login(), contact_login, 'ADD')
        try:
            response = requests.patch(api_link, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return True, data[-1] if isinstance(data, list) and data else data, None
            return False, None, "Error adding new contact!"
        except requests.exceptions.Timeout:
            return False, None, "Request timed out. Please try again later."
        except requests.exceptions.RequestException as e:
            return False, None, f"Error: {e}"

    @staticmethod
    def remove_contact(user, contact_login):
        api_link = contact_link(user.get_user_login(), contact_login, 'DELETE')
        try:
            response = requests.patch(api_link, timeout=5)
            if response.status_code == 200:
                return True, None, None
            return False, None, "Error removing contact!"
        except requests.exceptions.Timeout:
            return False, None, "Request timed out. Please try again later."
        except requests.exceptions.RequestException as e:
            return False, None, f"Error: {e}"
