class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User({self.user_id})'


users = [User(1), User(5), User(3)]
print(users)

users2 = sorted(users, key=lambda u: u.user_id)
print(users2)

from operator import attrgetter
users3 = sorted(users, key=attrgetter('user_id'))
print(users3)
