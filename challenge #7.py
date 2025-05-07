def create_profile(name, profile={}):
    profile["username"] = name
    return profile

user1 = create_profile("mark")
user2 = create_profile("joe")
user3 = create_profile("matt")

print(user1)
print(user2)
print(user3)
