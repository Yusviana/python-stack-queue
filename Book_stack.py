class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print("Buku ditambahkan ke dalam tumpukan.")

    def pop(self):
        if self.is_empty():
            print("Tumpukan sudah kosong.")
        else:
            removed_book = self.stack.pop()
            print("Buku terakhir dihapus:", removed_book)

    def peek(self):
        if self.is_empty():
            print("Tumpukan kosong.")
        else:
            top_book = self.stack[-1]
            print("Buku teratas:", top_book)

    def display(self):
        if self.is_empty():
            print("Tumpukan kosong.")
        else:
            print("Buku dalam tumpukan:")
            for book in reversed(self.stack):
                print("- ", book)


stack = Stack()

while True:
    print("\nMenu:")
    print("1. Tambahkan buku")
    print("2. Hapus buku terakhir")
    print("3. Tampilkan buku teratas")
    print("4. Tampilkan semua buku dalam tumpukan")
    print("5. Keluar")

    choice = input("Masukkan pilihan (1-5): ")

    if choice == "1":
        book_title = input("Masukkan judul buku: ")
        book_author = input("Masukkan penulis buku: ")
        book_info = f"{book_title} oleh {book_author}"
        stack.push(book_info)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        stack.peek()
    elif choice == "4":
        stack.display()
    elif choice == "5":
        print("BUKU ADALAH JENDELA DUNIA. TERIMAKASIH!")
        break
    else:
        print("Pilihan tidak valid")