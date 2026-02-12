from datetime import date
import random 

class User:
    def __init__(self, id, name, surname, birthday):
        self.used_id = id
        self.name = name
        self.surname = surname  
        self.birthday = birthday

    def get_details(self):
        return f"""Name: {self.name}
Surname: {self.surname} 
Birthday: {self.birthday}"""
    
    def get_age(self):
        return f"{date.today().year - self.birthday.year} years"
    


class UserService:
    users = {}

    def add_user(self, user):
        self.users[user.used_id] = user

    def find_user(self, user_id):
        return self.users.get(user_id, "User not found")
    
    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
        else:
            print("User not found")

    def update_user(self, user_id, name=None, surname=None, birthday=None):
        user = self.users.get(user_id)
        if user:
            if name:
                user.name = name
            if surname:
                user.surname = surname
            if birthday:
                user.birthday = birthday
        else:
            print("User not found")

    def get_number(self):
        return len(self.users)



class UserUtil:
    def generate_user_id(self):
        random_generated = ""
        for i in range(7):
            random_generated += str(random.randint(0, 9))
        return str(date.today().year)[-2::] + random_generated

    def generate_password(self):
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
        upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lower = random.choice("abcdefghijklmnopqrstuvwxyz")
        digits = random.choice("0123456789")
        symbols = random.choice("!@#$%^&*()")
        password = list(upper + lower + digits + symbols + "".join(random.choice(characters) for _ in range(4)))
        random.shuffle(password)
        return "".join(password)
    
    def is_strong_password(self, password):
        if (len(password) >= 8 and 
            any(c.isupper() for c in password) and 
            any(c.islower() for c in password) and 
            any(c.isdigit() for c in password) and 
            any(c in "!@#$%^&*()" for c in password)):
            return True
        return False
    
    def generate_email(self, name, surname):
        domains = ["example.com", "mail.com", "test.com", "gmail.com", "outlook.com"]
        domain = random.choice(domains)
        return f"{name.lower()}.{surname.lower()}@{domain}"
    
    def is_valid_email(self, email):
        if "@" in email and "." in email.split("@")[-1]:
            return True
        return False
    
# Test Section 
class TestUser:
    def test_user_creation(self):
        user = User("2300001", "Bayel", "Askarbekov", date(2007, 4, 25))
        assert user.get_details() == """Name: Bayel
Surname: Askarbekov 
Birthday: 2007-04-25"""
        assert user.get_age() == f"{date.today().year - 2007} years"
        return "Успешно пройден тест TestUser"

class TestUserService: 
    def test_user_service(self):
        service = UserService()
        user1 = User("2300001", "Bayel", "Askarbekov", date(2007, 4, 25))
        user2 = User("2300002", "Adilkan", "Anarbekov", date(2007, 10, 11))
        service.add_user(user1)
        service.add_user(user2)
        assert service.find_user("2300001") == user1
        assert service.find_user("2300002") == user2
        assert service.find_user("2300003") == "User not found"
        service.delete_user("2300001")
        assert service.find_user("2300001") == "User not found"
        service.update_user("2300002", name="Azim")
        assert service.find_user("2300002").name == "Azim"
        assert service.get_number() == 1
        return "Успешно пройдет тест TestUserService"

class TestUserUtil:
    def test_user_util(self):
        util = UserUtil()
        user_id = util.generate_user_id()
        assert len(user_id) == 9
        assert user_id[:2] == str(date.today().year)[-2::]
        password = util.generate_password()
        assert util.is_strong_password(password)
        email = util.generate_email("Bayel", "Askarbekov")
        assert email.startswith("bayel.askarbekov@")
        assert util.is_valid_email(email)
        return "Успешно пройден тест TestUserUtil"
        
d = TestUser()
print(d.test_user_creation())

e = TestUserService()
print(e.test_user_service())

f = TestUserUtil()
print(f.test_user_util())