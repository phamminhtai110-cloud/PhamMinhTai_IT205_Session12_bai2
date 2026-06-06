break_line = "===================================================="
menu_title_text = "TECHBANK SAVINGS MANAGEMENT"
menu_title = f"{break_line}\n{' ' * ((len(break_line) - len(menu_title_text)) // 2)}{menu_title_text}\n{break_line}"

saving_accounts = [
    {"account_id": "STK001", "customer_name": "Nguyễn Văn An", "balance": 50000000,
     "term_months": 6, "interest_rate": 6.5, "status": "active"},
    {"account_id": "STK002", "customer_name": "Trần Thị Bình", "balance": 120000000,
     "term_months": 12, "interest_rate": 7.2, "status": "active"}
]

while True:
    print(menu_title)
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    print("-" * 50)
    chon = input("Mời bạn chọn (1-7): ").strip()
    if chon not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    chon = int(chon)

    # 1. Xem danh sách
    if chon == 1:
        if not saving_accounts:
            print("\nDanh sách sổ tiết kiệm hiện đang trống")
        else:
            print("\n+------+----------------------+--------------+--------+-----------+--------+")
            print("| STT  | Mã sổ                | Khách hàng   | Số tiền| Kỳ hạn   | Lãi suất| Trạng thái |")
            print("+------+----------------------+--------------+--------+-----------+--------+")
            for i, a in enumerate(saving_accounts, 1):
                print(f"| {i:<4} | {a['account_id']:<6} | {a['customer_name']:<20} | {a['balance']:>10,} | {a['term_months']:>5} tháng | {a['interest_rate']:>5}% | {a['status']:<10} |")
            print("+------+----------------------+--------------+--------+-----------+--------+")

    # 2. Mở sổ mới
    elif chon == 2:
        print("\n--- MỞ SỔ TIẾT KIỆM MỚI ---")
        ma = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        if ma == "":
            print("Mã sổ không được để trống!")
            continue
        trung = False
        for a in saving_accounts:
            if a["account_id"] == ma:
                trung = True
                break
        if trung:
            print("Mã sổ tiết kiệm đã tồn tại!")
            continue
        ten = input("Nhập tên khách hàng: ").strip()
        if ten == "":
            print("Tên khách hàng không được để trống!")
            continue
        tien_str = input("Nhập số tiền gửi: ").strip()
        if not tien_str.isdigit():
            print("Số tiền gửi không hợp lệ!")
            continue
        tien = int(tien_str)
        if tien <= 0:
            print("Số tiền gửi phải lớn hơn 0!")
            continue
        kyhan_str = input("Nhập kỳ hạn gửi theo tháng: ").strip()
        if not kyhan_str.isdigit():
            print("Kỳ hạn không hợp lệ!")
            continue
        kyhan = int(kyhan_str)
        if kyhan <= 0:
            print("Kỳ hạn phải lớn hơn 0!")
            continue
        lai_str = input("Nhập lãi suất năm (%): ").strip()
        valid = True
        dot_count = 0
        for ch in lai_str:
            if ch == '.':
                dot_count += 1
                if dot_count > 1:
                    valid = False
                    break
            elif not ch.isdigit():
                valid = False
                break
        if not valid or lai_str == "":
            print("Lãi suất không hợp lệ!")
            continue
        lai = float(lai_str)
        if lai <= 0:
            print("Lãi suất phải lớn hơn 0!")
            continue
        saving_accounts.append({
            "account_id": ma,
            "customer_name": ten,
            "balance": tien,
            "term_months": kyhan,
            "interest_rate": lai,
            "status": "active"
        })
        print("Mở sổ tiết kiệm thành công!")

    # 3. Cập nhật
    elif chon == 3:
        print("\n--- CẬP NHẬT THÔNG TIN SỔ TIẾT KIỆM ---")
        ma = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
        tim = None
        for a in saving_accounts:
            if a["account_id"] == ma:
                tim = a
                break
        if tim is None:
            print("Không tìm thấy mã sổ tiết kiệm!")
            continue
        if tim["status"] != "active":
            print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
            continue
        ten = input("Nhập tên khách hàng mới: ").strip()
        if ten == "":
            print("Tên không được để trống!")
            continue
        tien_str = input("Nhập số tiền gửi mới: ").strip()
        if not tien_str.isdigit():
            print("Số tiền không hợp lệ!")
            continue
        tien = int(tien_str)
        if tien <= 0:
            print("Số tiền phải lớn hơn 0!")
            continue
        kyhan_str = input("Nhập kỳ hạn mới: ").strip()
        if not kyhan_str.isdigit():
            print("Kỳ hạn không hợp lệ!")
            continue
        kyhan = int(kyhan_str)
        if kyhan <= 0:
            print("Kỳ hạn phải lớn hơn 0!")
            continue
        lai_str = input("Nhập lãi suất mới: ").strip()
        valid = True
        dot_count = 0
        for ch in lai_str:
            if ch == '.':
                dot_count += 1
                if dot_count > 1:
                    valid = False
                    break
            elif not ch.isdigit():
                valid = False
                break
        if not valid or lai_str == "":
            print("Lãi suất không hợp lệ!")
            continue
        lai = float(lai_str)
        if lai <= 0:
            print("Lãi suất phải lớn hơn 0!")
            continue
        tim["customer_name"] = ten
        tim["balance"] = tien
        tim["term_months"] = kyhan
        tim["interest_rate"] = lai
        print("Cập nhật thông tin sổ tiết kiệm thành công!")

    # 4. Tất toán
    elif chon == 4:
        print("\n--- TẤT TOÁN SỔ TIẾT KIỆM ---")
        ma = input("Nhập mã sổ tiết kiệm cần tất toán: ").strip().upper()
        tim = None
        for a in saving_accounts:
            if a["account_id"] == ma:
                tim = a
                break
        if tim is None:
            print("Không tìm thấy mã sổ tiết kiệm!")
        else:
            tim["status"] = "closed"
            print("Đã tất toán sổ tiết kiệm. Sổ được chuyển sang trạng thái closed.")

    # 5. Tính lãi dự kiến
    elif chon == 5:
        print("\n--- TÍNH LÃI DỰ KIẾN KHI ĐẾN HẠN ---")
        ma = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        tim = None
        for a in saving_accounts:
            if a["account_id"] == ma:
                tim = a
                break
        if tim is None:
            print("Không tìm thấy mã sổ tiết kiệm!")
        elif tim["status"] != "active":
            print("Không thể tính lãi cho sổ đã tất toán!")
        else:
            lai = tim["balance"] * (tim["interest_rate"] / 100) * (tim["term_months"] / 12)
            tong = tim["balance"] + lai
            print(f"Tiền lãi dự kiến: {lai:,.0f}đ")
            print(f"Tổng tiền nhận khi đến hạn: {tong:,.0f}đ")

    # 6. Rút trước hạn
    elif chon == 6:
        print("\n--- KIỂM TRA ĐIỀU KIỆN RÚT TRƯỚC HẠN ---")
        ma = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        tim = None
        for a in saving_accounts:
            if a["account_id"] == ma:
                tim = a
                break
        if tim is None:
            print("Không tìm thấy mã sổ tiết kiệm!")
            continue
        if tim["status"] != "active":
            print("Không thể thao tác với sổ đã tất toán!")
            continue
        thang_str = input("Nhập số tháng thực gửi: ").strip()
        if not thang_str.isdigit():
            print("Số tháng thực gửi không hợp lệ!")
            continue
        thang = int(thang_str)
        if thang <= 0:
            print("Số tháng phải lớn hơn 0!")
            continue
        if thang < tim["term_months"]:
            ls = 0.5
            loai = "lãi suất không kỳ hạn (0.5%/năm)"
        else:
            ls = tim["interest_rate"]
            loai = f"lãi suất đúng hạn ({ls}%/năm)"
        lai = tim["balance"] * (ls / 100) * (thang / 12)
        tong = tim["balance"] + lai
        print(f"\nKết quả: Rút {'trước hạn' if thang < tim['term_months'] else 'đúng hạn'}")
        print(f"Áp dụng: {loai}")
        print(f"Tiền lãi thực nhận: {lai:,.0f}đ")
        print(f"Tổng tiền thực nhận: {tong:,.0f}đ")

    # 7. Thoát
    elif chon == 7:
        print("Cảm ơn bạn đã sử dụng hệ thống! Tạm biệt.")
        break
