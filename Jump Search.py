from prettytable import PrettyTable

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def tambah_di_antara(self, posisi, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        for _ in range(posisi - 1):
            if temp.next is None:
                raise ValueError("Posisi melebihi panjang linked list")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def hapus_di_awal(self):
        if not self.head:
            print("Linked list sudah kosong")
            return
        self.head = self.head.next

    def hapus_di_akhir(self):
        if not self.head:
            print("Linked list sudah kosong")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def hapus_di_antara(self, posisi):
        if not self.head:
            print("Linked list sudah kosong")
            return
        temp = self.head
        if posisi == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(posisi - 1):
            if temp is None or temp.next is None:
                raise ValueError("Posisi melebihi panjang linked list")
            temp = temp.next
        if temp.next is None:
            raise ValueError("Posisi melebihi panjang linked list")
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def merge_sort(self, key='harga', descending=False):
        if not self.head or not self.head.next:
            return self.head
        
        # Fungsi pembantu untuk membagi linked list menjadi dua bagian
        def split_linked_list(head):
            slow = head
            fast = head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None
            return head, mid
        
        # Fungsi pembantu untuk menggabungkan dua linked list yang terurut
        def merge(left, right):
            dummy = Node(0)
            current = dummy
            
            while left and right:
                if not descending:
                    if getattr(left.data, key) < getattr(right.data, key):
                        current.next = left
                        left = left.next
                    else:
                        current.next = right
                        right = right.next
                else:
                    if getattr(left.data, key) > getattr(right.data, key):
                        current.next = left
                        left = left.next
                    else:
                        current.next = right
                        right = right.next
                current = current.next
            
            current.next = left or right
            return dummy.next
        
        # Fungsi rekursif untuk merge sort
        def merge_sort_recursive(head):
            if not head or not head.next:
                return head
            
            left, right = split_linked_list(head)
            left_sorted = merge_sort_recursive(left)
            right_sorted = merge_sort_recursive(right)
            
            return merge(left_sorted, right_sorted)
        
        self.head = merge_sort_recursive(self.head)

    def jump_search(self, nama):
        if not self.head:
            print("Linked list kosong")
            return None

        if nama is None:
            print("Nama barang tidak boleh kosong")
            return None
        
        # Pointer untuk pencarian
        prev = None
        current = self.head
        
        # Melakukan pencarian
        while current and current.data.nama < nama:
            prev = current
            current = current.next
        
        # Jika barang ditemukan dan data barang tidak kosong, kembalikan data barang
        if current and current.data and current.data.nama == nama:
            return current.data
        else:
            print("Barang tidak ditemukan.")
            return None

class Barang:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def __str__(self):
        return f"Nama: {self.nama}, Jumlah: {self.jumlah}, Harga: {self.harga}"

class ManajemenInventaris:
    def __init__(self):
        self.inventaris = {
            'Kanvas': LinkedList(),
            'Kuas': LinkedList(),
            'Cat': LinkedList(),
            'Palet': LinkedList(),
            'Dudukan Kanvas': LinkedList(),
            'Koper': LinkedList(),
        }

    def tambah_item_di_awal(self, jenis, item):
        if jenis not in self.inventaris:
            self.inventaris[jenis] = LinkedList()
        self.inventaris[jenis].tambah_di_awal(item)

    def tambah_item_di_akhir(self, jenis, item):
        if jenis not in self.inventaris:
            self.inventaris[jenis] = LinkedList()
        self.inventaris[jenis].tambah_di_akhir(item)

    def tambah_item_di_antara(self, jenis, posisi, item):
        if jenis not in self.inventaris:
            self.inventaris[jenis] = LinkedList()
        self.inventaris[jenis].tambah_di_antara(posisi, item)

    def hapus_item_di_awal(self, jenis):
        if jenis in self.inventaris:
            self.inventaris[jenis].hapus_di_awal()
        else:
            print("Inventaris untuk jenis", jenis, "kosong.")

    def hapus_item_di_akhir(self, jenis):
        if jenis in self.inventaris:
            self.inventaris[jenis].hapus_di_akhir()
        else:
            print("Inventaris untuk jenis", jenis, "kosong.")

    def hapus_item_di_antara(self, jenis, posisi):
        if jenis in self.inventaris:
            self.inventaris[jenis].hapus_di_antara(posisi)
        else:
            print("Inventaris untuk jenis", jenis, "kosong.")

    def tampilkan_inventaris(self, jenis, urutkan=False, key='harga', descending=False):
        if jenis in self.inventaris:
            print(f"Inventaris {jenis} Saat Ini:")
            if urutkan:
                self.inventaris[jenis].merge_sort(key=key, descending=descending)
            inventaris_table = PrettyTable(["Nama", "Jumlah", "Harga"])
            current_node = self.inventaris[jenis].head
            while current_node:
                inventaris_table.add_row([current_node.data.nama, current_node.data.jumlah, current_node.data.harga])
                current_node = current_node.next
            print(inventaris_table)
        else:
            print("Inventaris untuk jenis", jenis, "kosong.")

    def perbarui_item(self, jenis, nama_item, jumlah_baru):
        if jenis in self.inventaris:
            temp = self.inventaris[jenis].head
            while temp:
                if temp.data.nama == nama_item:
                    temp.data.jumlah = jumlah_baru
                    print("Item berhasil diperbarui.")
                    return
                temp = temp.next
            print("Item tidak ditemukan dalam inventaris.")
        else:
            print("Inventaris untuk jenis", jenis, "kosong.")

    def hapus_item(self, jenis, nama_item):
        if jenis in self.inventaris:
            temp = self.inventaris[jenis].head
            prev = None
            while temp:
                if temp.data.nama == nama_item:
                    if prev:
                        prev.next = temp.next
                    else:
                        self.inventaris[jenis].head = temp.next
                    print("Item berhasil dihapus.")
                    return
                prev = temp
                temp = temp.next
            print("Item tidak ditemukan dalam inventaris.")
        else:
            print("Inventaris untuk jenis", jenis, "kosong.")

    def cari_barang_berdasarkan_jenis(self, jenis, nama):
        if jenis in self.inventaris:
            result = self.inventaris[jenis].jump_search(nama)
            if result:
                return [(jenis, result)]
        print("Barang tidak ditemukan.")
        return None
    
    def tampilkan_inventaris(self):
        for jenis, linked_list in self.inventaris.items():
            print(f"Inventaris {jenis} Saat Ini:")
            linked_list.merge_sort()
            inventaris_table = PrettyTable(["Nama", "Jumlah", "Harga"])
            current_node = linked_list.head
            while current_node:
                inventaris_table.add_row([current_node.data.nama, current_node.data.jumlah, current_node.data.harga])
                current_node = current_node.next
            print(inventaris_table)

    def cari_barang_berdasarkan_nama(self, nama):
        results = []
        for jenis, linked_list in self.inventaris.items():
            current_node = linked_list.head
            while current_node:
                if current_node.data.nama == nama:
                    results.append((jenis, current_node.data))
                current_node = current_node.next
        return results

    def cari_barang(self, jenis, nama=None):
        if jenis == 'jenis':
            nama_barang = input("Masukkan jenis barang yang ingin dicari: ")
            self.tampilkan_hasil_pencarian_jenis(nama_barang)
        elif jenis == 'nama':
            nama_barang = input("Masukkan nama barang yang ingin dicari: ")
            results = self.cari_barang_berdasarkan_nama(nama_barang)
            if results:
                self.tampilkan_hasil_pencarian(nama_barang, results)
            else:
                print("Barang tidak ditemukan")
        else:
            print("Pilihan pencarian tidak valid.")




    def tampilkan_hasil_pencarian(self, nama_barang, results):
        if results:
            print(f"Hasil pencarian untuk barang dengan nama '{nama_barang}':")
            table = PrettyTable(["Jenis", "Nama", "Jumlah", "Harga"])
            for jenis, barang in results:
                table.add_row([jenis, barang.nama, barang.jumlah, barang.harga])
            print(table)
        else:
            print(f"Tidak ditemukan barang dengan nama '{nama_barang}'.")


    def tampilkan_hasil_pencarian_jenis(self, jenis):
        if jenis in self.inventaris:
            print(f"Inventaris {jenis} Saat Ini:")
            linked_list = self.inventaris[jenis]
            inventaris_table = PrettyTable(["Nama", "Jumlah", "Harga"])
            current_node = linked_list.head
            while current_node:
                inventaris_table.add_row([current_node.data.nama, current_node.data.jumlah, current_node.data.harga])
                current_node = current_node.next
            print(inventaris_table)
        else:
            print("Inventaris untuk jenis", jenis, "kosong.")


def main():
    manajemen_inventaris = ManajemenInventaris()
    # Menambahkan barang Marsoto ke jenis Kanvas dari awal
    manajemen_inventaris.tambah_item_di_awal('Kanvas', Barang('Marsoto', 12, 20000))
    manajemen_inventaris.tambah_item_di_awal('Kanvas', Barang('Blacu', 98, 16000))
    manajemen_inventaris.tambah_item_di_awal('Kanvas', Barang('Tesla Paints', 2, 49000))
    manajemen_inventaris.tambah_item_di_awal('Kanvas', Barang('Phoenix', 44, 50000))
    manajemen_inventaris.tambah_item_di_awal('Kanvas', Barang('Royal Talens', 60, 85000))

    manajemen_inventaris.tambah_item_di_awal('Kuas', Barang('Joyko', 23, 11500))
    manajemen_inventaris.tambah_item_di_awal('Kuas', Barang('Montana', 9, 20000))
    manajemen_inventaris.tambah_item_di_awal('Kuas', Barang('Deli', 11, 10323))
    manajemen_inventaris.tambah_item_di_awal('Kuas', Barang('Lyra', 5, 99900))
    manajemen_inventaris.tambah_item_di_awal('Kuas', Barang('Giorgione', 88, 3000)) 

    manajemen_inventaris.tambah_item_di_awal('Cat', Barang('Winsor', 41, 19825))
    manajemen_inventaris.tambah_item_di_awal('Cat', Barang('Faber-Castell', 89, 23132))
    manajemen_inventaris.tambah_item_di_awal('Cat', Barang('Van Gogh', 82, 10179))
    manajemen_inventaris.tambah_item_di_awal('Cat', Barang('Sakura Koi', 94, 28125))
    manajemen_inventaris.tambah_item_di_awal('Cat', Barang('Deli Solid', 22, 24904))

    manajemen_inventaris.tambah_item_di_awal('Palet', Barang('Amando Caruso', 58, 25449))
    manajemen_inventaris.tambah_item_di_awal('Palet', Barang('Graha', 97, 25876))
    manajemen_inventaris.tambah_item_di_awal('Palet', Barang('V-Tec', 67, 29383))
    manajemen_inventaris.tambah_item_di_awal('Palet', Barang('Etchr Lab', 50, 24840))
    manajemen_inventaris.tambah_item_di_awal('Palet', Barang('Deli', 19, 14715))

    while True:
        print("\nSistem Manajemen Inventaris")
        print("1. Tambah Barang")
        print("2. Tampilkan Inventaris")
        print("3. Perbarui Jumlah Item")
        print("4. Hapus Item")
        print("5. Cari Barang (Berdasarkan Jenis/Nama)")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            jenis = input("Masukkan jenis barang: ")
            nama = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            harga = float(input("Masukkan harga barang: "))
            item = Barang(nama, jumlah, harga)
            posisi = input("Pilih posisi tambah (awal/antara/akhir): ").lower()
            if posisi == 'awal':
                manajemen_inventaris.tambah_item_di_awal(jenis, item)
            elif posisi == 'antara':
                posisi = int(input("Masukkan posisi tambah: "))
                manajemen_inventaris.tambah_item_di_antara(jenis, posisi, item)
            elif posisi == 'akhir':
                manajemen_inventaris.tambah_item_di_akhir(jenis, item)
            else:
                print("Posisi tidak valid.")

        elif pilihan == '2':
            # manajemen_inventaris.tampilkan_inventaris()
            urutkan = input("Urutkan berdasarkan harga atau jumlah? (harga/jumlah): ").lower()
            if urutkan == 'harga' or urutkan == 'jumlah':
                descending_input = input("Pilih urutan (ascending/descending): ").lower()
                descending = True if descending_input == 'descending' else False
                for jenis in manajemen_inventaris.inventaris:
                    manajemen_inventaris.inventaris[jenis].merge_sort(key=urutkan, descending=descending)
                manajemen_inventaris.tampilkan_inventaris()
            elif urutkan == '':
                manajemen_inventaris.tampilkan_inventaris()
            else:
                print("Pilihan pengurutan tidak valid.")

        elif pilihan == '3':
            jenis = input("Masukkan jenis barang: ")
            nama = input("Masukkan nama item untuk memperbarui jumlah: ")
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            manajemen_inventaris.perbarui_item(jenis, nama, jumlah_baru)

        elif pilihan == '4':
            jenis = input("Masukkan jenis barang: ")
            nama = input("Masukkan nama item untuk dihapus: ")
            manajemen_inventaris.hapus_item(jenis, nama)

        elif pilihan == '5':
            jenis_pencarian = input("Pilih jenis pencarian (jenis/nama): ")
            manajemen_inventaris.cari_barang(jenis_pencarian)

        elif pilihan == '0':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan opsi yang benar.")

if __name__ == "__main__":
    main()
