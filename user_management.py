from datetime import datetime
import random
import string
import re

class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return (f"User ID: {self.user_id}, Name: {self.name} {self.surname}, "
                f"Email: {self.email}, Birthday: {self.birthday.strftime('%Y-%m-%d')}")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            user = cls.users[user_id]
            user.name = user_update.name if user_update.name else user.name
            user.surname = user_update.surname if user_update.surname else user.surname
            user.email = user_update.email if user_update.email else user.email
            user.password = user_update.password if user_update.password else user.password
            user.birthday = user_update.birthday if user_update.birthday else user.birthday

    @classmethod
    def get_number(cls):
        return len(cls.users)

class UserUtil:
    @staticmethod
    def generate_user_id():
        current_year = str(datetime.now().year)[2:]
        random_digits = ''.join(random.choices(string.digits, k=7))
        return int(current_year + random_digits)

    @staticmethod
    def generate_password():
        uppercase = random.choice(string.ascii_uppercase)
        lowercase = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special = random.choice(string.punctuation)
        remaining = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=4))
        password = ''.join(random.sample(uppercase + lowercase + digit + special + remaining, 8))
        return password

@staticmethod
def is_strong_password(password):
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":;{}\\|<>\-=\+\[\]\\']", password):
            return False
        return True

@staticmethod
def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

@staticmethod
def validate_email(email):
        pattern = r"^[a-zA-Z]+\.[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$"
        return re.match(pattern, email) is not None