from collections import deque

class TransactionQueue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, transaction):
        self.queue.append(transaction)
        print("Transaksi ditambahkan ke dalam antrean.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean sudah kosong.")
        else:
            served_transaction = self.queue.popleft()
            print("Transaksi yang dilayani:", served_transaction)

    def peek(self):
        if self.is_empty():
            print("Antrean kosong.")
        else:
            next_transaction = self.queue[0]
            print("Transaksi berikutnya yang akan dilayani:", next_transaction)

    def display(self):
        if self.is_empty():
            print("Antrean kosong.")
        else:
            print("Transaksi dalam antrean:")
            for transaction in self.queue:
                print("- ", transaction)


queue = TransactionQueue()

while True:
    print("\nMenu:")
    print("1. Tambahkan transaksi ke dalam antrean")
    print("2. Hapus transaksi yang telah dilayani")
    print("3. Tampilkan transaksi berikutnya yang akan dilayani")
    print("4. Tampilkan semua transaksi dalam antrean")
    print("5. Keluar")

    choice = input("Masukkan pilihan (1-5): ")

    if choice == "1":
        customer_name = input("Masukkan nama pelanggan: ")
        transaction_type = input("Masukkan jenis transaksi: ")
        transaction_info = f"{customer_name} - {transaction_type}"
        queue.enqueue(transaction_info)
    elif choice == "2":
        queue.dequeue()
    elif choice == "3":
        queue.peek()
    elif choice == "4":
        queue.display()
    elif choice == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang valid.")