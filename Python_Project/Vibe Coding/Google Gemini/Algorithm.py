
# --- 1. Algoritma Konsolidasi --- #
def consolidate_data(data_list, group_key, sum_key):
    """
    Mengonsolidasikan daftar dictionary.
    Menggabungkan dictionary berdasarkan `group_key` dan menjumlahkan nilai pada `sum_key`.

    Args:
        data_list (list): Daftar dictionary yang akan dikonsolidasikan.
        group_key (str): Kunci untuk mengelompokkan item.
        sum_key (str): Kunci yang nilainya akan dijumlahkan.

    Returns:
        list: Daftar dictionary yang sudah dikonsolidasikan.
    """
    consolidated = {}

    for item in data_list:
        key_value = item.get(group_key)
        sum_value = item.get(sum_key, 0)

        if key_value is not None:
            if key_value not in consolidated:
                new_item = item.copy()
                consolidated[key_value] = new_item
            else:
                current_sum = consolidated[key_value].get(sum_key, 0)
                consolidated[key_value][sum_key] = current_sum + sum_value

    return list(consolidated.values())

# --- 2. Algoritma Menggabungkan (Merging) --- #
def merge_data(list1, list2, merge_key):
    """
    Menggabungkan dua daftar dictionary berdasarkan merge_key.
    Ini seperti 'full outer merge', mencakup semua item dari kedua daftar
    dan menggabungkan atribut item yang cocok berdasarkan merge_key.

    Args:
        list1 (list): Daftar dictionary pertama.
        list2 (list): Daftar dictionary kedua.
        merge_key (str): Kunci untuk mencocokkan item antar daftar.

    Returns:
        list: Daftar dictionary hasil gabungan.
    """
    merged = {}

    for item in list1:
        key_value = item.get(merge_key)
        if key_value is not None:
            merged[key_value] = item.copy()

    for item in list2:
        key_value = item.get(merge_key)
        if key_value is not None:
            if key_value in merged:
                merged[key_value].update(item)
            else:
                merged[key_value] = item.copy()

    return list(merged.values())

# --- 3. Algoritma Memperbarui (Updating) --- #
def update_data(target_list, update_list, match_key):
    """
    Memperbarui item dalam target_list menggunakan informasi dari update_list
    berdasarkan match_key. Hanya item di target_list yang akan diubah.

    Args:
        target_list (list): Daftar dictionary yang akan diperbarui.
        update_list (list): Daftar dictionary yang berisi data pembaruan.
        match_key (str): Kunci untuk mencocokkan item antar daftar.

    Returns:
        list: target_list setelah diperbarui (list yang sama yang dimodifikasi).
    """
    update_dict = {}
    for item in update_list:
        key_value = item.get(match_key)
        if key_value is not None:
            update_dict[key_value] = item

    for item in target_list:
        key_value = item.get(match_key)
        if key_value is not None and key_value in update_dict:
            update_info = update_dict[key_value]
            for key, value in update_info.items():
                 # Opsi: if key != match_key: # Hindari menimpa match_key itu sendiri
                item[key] = value

    return target_list

# --- 4. Algoritma Memisah (Splitting) --- #
def split_data(data_list, split_key):
    """
    Memisahkan daftar dictionary menjadi beberapa grup berdasarkan split_key.

    Args:
        data_list (list): Daftar dictionary yang akan dipisah.
        split_key (str): Kunci untuk memisahkan item.

    Returns:
        dict: Dictionary di mana kunci adalah nilai dari split_key
              dan nilai adalah list dari dictionary yang sesuai.
    """
    split_groups = {}

    for item in data_list:
        key_value = item.get(split_key)

        if key_value is not None:
            if key_value not in split_groups:
                split_groups[key_value] = []

            split_groups[key_value].append(item)

    return split_groups

# --- Contoh Penggunaan Semua Algoritma --- #

print("--- Contoh Penggunaan Konsolidasi ---")
inventory = [
    {'item': 'Apple', 'qty': 5, 'price': 0.5},
    {'item': 'Banana', 'qty': 2, 'price': 0.3},
    {'item': 'Apple', 'qty': 3, 'price': 0.5},
    {'item': 'Orange', 'qty': 1, 'price': 0.7},
    {'item': 'Banana', 'qty': 4, 'price': 0.3},
]
print("Data asli inventory:")
for item in inventory: print(item)
consolidated_inventory = consolidate_data(inventory, group_key='item', sum_key='qty')
print("\nData setelah konsolidasi (item, qty):")
for item in consolidated_inventory: print(item)
print("-" * 30)

print("\n--- Contoh Penggunaan Menggabungkan (Merging) ---")
products = [
    {'id': 'P001', 'name': 'Laptop', 'category': 'Electronics'},
    {'id': 'P002', 'name': 'Desk Chair', 'category': 'Furniture'},
    {'id': 'P003', 'name': 'Keyboard', 'category': 'Accessories'},
]
prices = [
    {'id': 'P001', 'price': 1200.00, 'currency': 'USD'},
    {'id': 'P003', 'price': 75.00, 'currency': 'USD'},
    {'id': 'P004', 'price': 25.00, 'currency': 'USD'},
]
print("Daftar Produk:")
for item in products: print(item)
print("\nDaftar Harga:")
for item in prices: print(item)
merged_data = merge_data(products, prices, merge_key='id')
print("\nData setelah digabungkan (id):")
for item in merged_data: print(item)
print("-" * 30)


print("\n--- Contoh Penggunaan Memperbarui (Updating) ---")
current_stock = [
    {'product_id': 'A101', 'name': 'Gadget X', 'price': 500, 'stock': 100},
    {'product_id': 'A102', 'name': 'Widget Y', 'price': 150, 'stock': 50},
    {'product_id': 'A103', 'name': 'Thing Z', 'price': 250, 'stock': 200},
]
price_updates = [
    {'product_id': 'A101', 'price': 520},
    {'product_id': 'A103', 'price': 245, 'stock': 180},
    {'product_id': 'A104', 'price': 99},
]
print("Stok saat ini:")
for item in current_stock: print(item)
print("\nPembaruan:")
for item in price_updates: print(item)
# Perhatikan: update_data memodifikasi current_stock secara langsung
updated_stock = update_data(current_stock, price_updates, match_key='product_id')
print("\nStok setelah diperbarui (product_id):")
for item in updated_stock: print(item)
print("-" * 30)


print("\n--- Contoh Penggunaan Memisah (Splitting) ---")
transactions = [
    {'transaction_id': 101, 'customer_id': 'CustA', 'amount': 50.0},
    {'transaction_id': 102, 'customer_id': 'CustB', 'amount': 120.0},
    {'transaction_id': 103, 'customer_id': 'CustA', 'amount': 30.0},
    {'transaction_id': 104, 'customer_id': 'CustC', 'amount': 200.0},
    {'transaction_id': 105, 'customer_id': 'CustB', 'amount': 75.0},
]
print("Daftar Transaksi:")
for item in transactions: print(item)
split_transactions = split_data(transactions, split_key='customer_id')
print("\nTransaksi setelah dipisah (customer_id):")
for customer_id, transactions_list in split_transactions.items():
    print(f"Customer ID: {customer_id}")
    for transaction in transactions_list:
        print(f"  {transaction}")
print("-" * 30)
