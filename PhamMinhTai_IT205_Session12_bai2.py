# -*- coding: utf-8 -*-
"""
He thong quan ly tai khoan tiet kiem TechBank
Su dung list va dict, xu ly edge cases, khong dung try-except
"""

# ==================== DU LIEU MAU ====================
saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyen Van An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Tran Thi Binh",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

# ==================== CAC HAM NHAP LIEU ====================
def get_nonempty_string(prompt):
    """Nhap chuoi khong duoc de trong"""
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Loi: Khong duoc de trong!")
        else:
            return s

def get_positive_int(prompt):
    """Nhap so nguyen duong"""
    while True:
        s = input(prompt).strip()
        if not s.isdigit():
            print("Loi: Vui long nhap so nguyen duong.")
            continue
        n = int(s)
        if n <= 0:
            print("Loi: Gia tri phai lon hon 0.")
            continue
        return n

def get_positive_float(prompt):
    """Nhap so thuc duong (co the co dau cham)"""
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Loi: Khong duoc de trong.")
            continue
        # Kiem tra dinh dang so thuc hop le: chu so va toi da 1 dau cham
        valid = True
        dot_count = 0
        for ch in s:
            if ch == '.':
                dot_count += 1
                if dot_count > 1:
                    valid = False
                    break
            elif not ch.isdigit():
                valid = False
                break
        if not valid:
            print("Loi: Vui long nhap so hop le (vi du: 6.5).")
            continue
        val = float(s)
        if val <= 0:
            print("Loi: Gia tri phai lon hon 0.")
            continue
        return val

# ==================== HAM TIM KIEM ====================
def find_account(account_id):
    """Tra ve dict cua so tiet kiem neu ton tai, nguoc lai None"""
    for acc in saving_accounts:
        if acc["account_id"] == account_id:
            return acc
    return None

# ==================== CHUC NANG ====================
def show_menu():
    print("\n====================================================")
    print("HE THONG QUAN LY TAI KHOAN TIET KIEM TECHBANK")
    print("====================================================")
    print("1. Xem danh sach so tiet kiem")
    print("2. Mo so tiet kiem moi")
    print("3. Cap nhat thong tin so tiet kiem")
    print("4. Tat toan so tiet kiem")
    print("5. Tinh lai du kien khi den han")
    print("6. Kiem tra dieu kien rut truoc han")
    print("7. Thoat chuong trinh")
    print("----------------------------------------------------")

def display_all():
    """Chuc nang 1: Xem danh sach"""
    print("\n--- DANH SACH SO TIET KIEM ---")
    if not saving_accounts:
        print("Danh sach so tiet kiem hien dang trong")
        return
    for i, acc in enumerate(saving_accounts, 1):
        print(f"{i}. Ma so: {acc['account_id']} | Khach hang: {acc['customer_name']} | "
              f"So tien gui: {acc['balance']:,} | Ky han: {acc['term_months']} thang | "
              f"Lai suat: {acc['interest_rate']}%/nam | Trang thai: {acc['status']}")

def open_account():
    """Chuc nang 2: Mo so tiet kiem moi"""
    print("\n--- MO SO TIET KIEM MOI ---")
    # Nhap ma so
    while True:
        acc_id = input("Nhap ma so tiet kiem: ").strip().upper()
        if acc_id == "":
            print("Ma so khong duoc de trong!")
            continue
        if find_account(acc_id) is not None:
            print("Ma so tiet kiem da ton tai!")
            continue
        break
    # Nhap ten khach hang
    name = get_nonempty_string("Nhap ten khach hang: ")
    # Nhap so tien gui
    balance = get_positive_int("Nhap so tien gui: ")
    # Nhap ky han
    term = get_positive_int("Nhap ky han gui theo thang: ")
    # Nhap lai suat
    rate = get_positive_float("Nhap lai suat nam (%): ")
    # Them moi
    saving_accounts.append({
        "account_id": acc_id,
        "customer_name": name,
        "balance": balance,
        "term_months": term,
        "interest_rate": rate,
        "status": "active"
    })
    print("Mo so tiet kiem thanh cong!")

def update_account():
    """Chuc nang 3: Cap nhat thong tin so tiet kiem"""
    print("\n--- CAP NHAT SO TIET KIEM ---")
    acc_id = input("Nhap ma so can cap nhat: ").strip().upper()
    acc = find_account(acc_id)
    if acc is None:
        print("Khong tim thay ma so tiet kiem!")
        return
    if acc["status"] != "active":
        print("Khong the cap nhat so tiet kiem da tat toan!")
        return
    # Nhap thong tin moi
    new_name = get_nonempty_string("Nhap ten khach hang moi: ")
    new_balance = get_positive_int("Nhap so tien gui moi: ")
    new_term = get_positive_int("Nhap ky han moi theo thang: ")
    new_rate = get_positive_float("Nhap lai suat nam moi: ")
    # Cap nhat
    acc["customer_name"] = new_name
    acc["balance"] = new_balance
    acc["term_months"] = new_term
    acc["interest_rate"] = new_rate
    print("Cap nhat thong tin so tiet kiem thanh cong!")

def close_account():
    """Chuc nang 4: Tat toan so (chuyen trang thai thanh closed)"""
    print("\n--- TAT TOAN SO TIET KIEM ---")
    acc_id = input("Nhap ma so can tat toan: ").strip().upper()
    acc = find_account(acc_id)
    if acc is None:
        print("Khong tim thay ma so tiet kiem!")
        return
    acc["status"] = "closed"
    print("Da tat toan so tiet kiem. So duoc chuyen sang trang thai closed.")

def calculate_interest():
    """Chuc nang 5: Tinh lai du kien khi den han"""
    print("\n--- TINH LAI DU KIEN ---")
    acc_id = input("Nhap ma so tiet kiem: ").strip().upper()
    acc = find_account(acc_id)
    if acc is None:
        print("Khong tim thay ma so tiet kiem!")
        return
    if acc["status"] != "active":
        print("Khong the tinh lai cho so da tat toan!")
        return
    interest = acc["balance"] * (acc["interest_rate"] / 100) * (acc["term_months"] / 12)
    total = acc["balance"] + interest
    print(f"Tien lai du kien khi den han: {interest:,.0f}d")
    print(f"Tong tien nhan khi den han: {total:,.0f}d")

def early_withdrawal():
    """Chuc nang 6: Kiem tra rut truoc han"""
    print("\n--- KIEM TRA RUT TRUOC HAN ---")
    acc_id = input("Nhap ma so tiet kiem: ").strip().upper()
    acc = find_account(acc_id)
    if acc is None:
        print("Khong tim thay ma so tiet kiem!")
        return
    if acc["status"] != "active":
        print("Khong the thao tac voi so da tat toan!")
        return
    months = get_positive_int("Nhap so thang thuc gui: ")
    if months < acc["term_months"]:
        rate = 0.5
        loai = "lai suat khong ky han (0.5%/nam)"
    else:
        rate = acc["interest_rate"]
        loai = f"lai suat dung han ({rate}%/nam)"
    interest = acc["balance"] * (rate / 100) * (months / 12)
    total = acc["balance"] + interest
    print(f"\nKet qua: Rut {'truoc han' if months < acc['term_months'] else 'dung han'}")
    print(f"Ap dung: {loai}")
    print(f"Tien lai thuc nhan: {interest:,.0f}d")
    print(f"Tong tien thuc nhan: {total:,.0f}d")

# ==================== CHUONG TRINH CHINH ====================
def main():
    while True:
        show_menu()
        choice = input("Moi ban chon (1-7): ").strip()
        if not choice.isdigit():
            print("Lua chon khong hop le, vui long nhap lai!")
            continue
        choice = int(choice)
        if choice < 1 or choice > 7:
            print("Lua chon khong hop le, vui long nhap lai!")
            continue

        if choice == 1:
            display_all()
        elif choice == 2:
            open_account()
        elif choice == 3:
            update_account()
        elif choice == 4:
            close_account()
        elif choice == 5:
            calculate_interest()
        elif choice == 6:
            early_withdrawal()
        elif choice == 7:
            print("\nCam on ban da su dung he thong. Tam biet!")
            break

if __name__ == "__main__":
    main()
