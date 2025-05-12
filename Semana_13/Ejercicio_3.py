from datetime import date

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def verify_age(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user.age < 18:
            raise ValueError("User is underage")
        return func(*args, **kwargs)
    return wrapper
    

@verify_age
def register_user(user: User):
    print(f"User {user} registered successfully!")
    return True

user_adult = User(date(2000, 1, 1))
user_under_age = User(date(2010, 1, 1))

register_user(user_adult) 
register_user(user_under_age)  


