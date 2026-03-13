# =====================================
# CLASS USER
# =====================================

class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        self.login_attempts = 0   # atribut jumlah percobaan login

    # metode untuk menampilkan informasi user
    def describe_user(self):
        print("=== Informasi User ===")
        print(f"Nama Depan : {self.first_name}")
        print(f"Nama Belakang : {self.last_name}")
        print(f"Umur : {self.age}")
        print(f"Email : {self.email}")
        print(f"Kota : {self.city}")
        print()

    # metode untuk menyapa user
    def greet_user(self):
        print(f"Halo {self.first_name} {self.last_name}, selamat datang!\n")

    # menambah percobaan login
    def increment_login_attempts(self):
        self.login_attempts += 1

    # mereset percobaan login
    def reset_login_attempts(self):
        self.login_attempts = 0


# =====================================
# MEMBUAT INSTANCE USER
# =====================================

user1 = User("Andi", "Saputra", 20, "andi@gmail.com", "Pekanbaru")

# =====================================
# MENAMPILKAN DATA USER
# =====================================

user1.describe_user()
user1.greet_user()

# =====================================
# MENAMBAH LOGIN ATTEMPTS
# =====================================

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Jumlah percobaan login:", user1.login_attempts)

# =====================================
# RESET LOGIN ATTEMPTS
# =====================================

user1.reset_login_attempts()

print("Jumlah percobaan login setelah reset:", user1.login_attempts)