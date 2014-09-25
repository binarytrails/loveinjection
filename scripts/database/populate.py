from sqlite3app.models import User

user = User(
    username = "admin",
    password = "god"
)
user.save()
user = User(
    username = "sys",
    password = "letmein",
)
user.save()
user = User(
    username = "peterparker",
    password = "spiderman"
)
user.save()
