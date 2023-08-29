class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = []
        self.following = []

    def follow(self, user):
        if user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def print_followers(self):
        print(self.name)
        for user in self.followers:
            print(user.name)
        print("")


first_user = User("001", "John")
second_user = User("002", "Jane")

first_user.follow(second_user)

first_user.print_followers()
second_user.print_followers()


# Class inheritance
class Animal:
    def __init__(self, name):
        self.num_eyes = 2
        self.name = name

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self, name, iscarnivore=False):
        super().__init__(name)
        self.eats_fish = iscarnivore

    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()
        print("doing this under water")


nemo = Fish("nemo")
nemo.swim()
print(nemo.num_eyes)
nemo.breathe()
