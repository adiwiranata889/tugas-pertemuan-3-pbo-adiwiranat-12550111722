# =====================================
# CLASS RESTAURANT
# =====================================

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0   # atribut jumlah pelanggan (default = 0)

    # menampilkan deskripsi restoran
    def describe_restaurant(self):
        print(f"{self.restaurant_name} adalah restoran yang menyajikan {self.cuisine_type}.")

    # menampilkan restoran buka
    def open_restaurant(self):
        print(f"{self.restaurant_name} sekarang sudah buka!\n")

    # mengatur jumlah pelanggan
    def set_number_served(self, number):
        self.number_served = number

    # menambah jumlah pelanggan
    def increment_number_served(self, additional):
        self.number_served += additional


# =====================================
# MEMBUAT OBJEK RESTAURANT
# =====================================

restaurant = Restaurant("Rasa Nusantara", "Masakan Indonesia")

# =====================================
# MENAMPILKAN DATA RESTORAN
# =====================================

restaurant.describe_restaurant()
restaurant.open_restaurant()

# menampilkan jumlah pelanggan awal
print("Jumlah pelanggan yang telah dilayani:", restaurant.number_served)

# =====================================
# MENGUBAH NILAI JUMLAH PELANGGAN
# =====================================

restaurant.number_served = 20
print("Jumlah pelanggan setelah diubah langsung:", restaurant.number_served)

# =====================================
# MENGGUNAKAN METHOD set_number_served()
# =====================================

restaurant.set_number_served(35)
print("Jumlah pelanggan setelah menggunakan set_number_served():", restaurant.number_served)

# =====================================
# MENAMBAH JUMLAH PELANGGAN
# =====================================

restaurant.increment_number_served(15)
print("Jumlah pelanggan setelah penambahan pelanggan:", restaurant.number_served)