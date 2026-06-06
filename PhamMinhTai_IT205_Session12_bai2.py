# Dữ liệu mẫu
saving_accounts = [
    {"account_id": "STK001", "customer_name": "Nguyễn Văn An", "balance": 50000000,
     "term_months": 6, "interest_rate": 6.5, "status": "active"},
    {"account_id": "STK002", "customer_name": "Trần Thị Bình", "balance": 120000000,
     "term_months": 12, "interest_rate": 7.2, "status": "active"}
]

# Dùng tuple để lưu menu
MENU = ("1.Xem", "2.Mở", "3.Cập nhật", "4.Tất toán", "5.Tính lãi", "6.Rút trước hạn", "7.Thoát")

while True:
    print("\n===== TECHBANK =====")
    for item in MENU:
        print(item)
    chon = input("Chọn (1-7): ").strip()

    # Kiểm tra lựa chọn có phải 1-7 không
    if chon not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Lựa chọn không hợp lệ!")
        continue

    # 1. Xem danh sách
    if chon == "1":
        if not saving_accounts:
            print("Danh sách trống")
        else:
            for i, a in enumerate(saving_accounts, 1):
                print(f"{i}. {a['account_id']} | {a['customer_name']} | {a['balance']:,}đ | "
                      f"{a['term_months']} tháng | {a['interest_rate']}% | {a['status']}")

    # 2. Mở sổ mới
    elif chon == "2":
        ma = input("Mã sổ: ").strip().upper()
        # Kiểm tra trùng
        trung = False
        for a in saving_accounts:
            if a["account_id"] == ma:
                trung = True
                break
        if trung:
            print("Mã sổ đã tồn tại!")
            continue

        ten = input("Tên KH: ").strip()
        if ten == "":
            print("Tên không được trống!")
            continue

        # Nhập số tiền
        tien_str = input("Số tiền gửi: ").strip()
        if not tien_str.isdigit():
            print("Số tiền phải là số nguyên dương!")
            continue
        tien = int(tien_str)
        if tien <= 0:
            print("Số tiền phải lớn hơn 0!")
            continue

        # Nhập kỳ hạn
        kyhan_str = input("Kỳ hạn (tháng): ").strip()
        if not kyhan_str.isdigit():
            print("Kỳ hạn phải là số nguyên dương!")
            continue
        kyhan = int(kyhan_str)
        if kyhan <= 0:
            print("Kỳ hạn phải lớn hơn 0!")
            continue

        # Nhập lãi suất (cho phép số thập phân, kiểm tra bằng cách thử chuyển float)
        lai_str = input("Lãi suất năm (%): ").strip()
        # Kiểm tra lãi suất có định dạng số thực hợp lệ (không dùng try-except)
        # Cách thủ công: cho phép dấu chấm và chữ số
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

        saving_accounts.append({"account_id": ma, "customer_name": ten, "balance": tien,
                                "term_months": kyhan, "interest_rate": lai, "status": "active"})
        print("Mở sổ thành công!")

    # 3. Cập nhật
    elif chon == "3":
        ma = input("Mã cần cập nhật: ").strip().upper()
        tim = None
        for a in saving_accounts:
            if a["account_id"] == ma:
                tim = a
                break
        if tim is None:
            print("Không tìm thấy mã!")
        elif tim["status"] != "active":
            print("Sổ đã tất toán, không thể cập nhật!")
        else:
            ten = input("Tên mới: ").strip()
            if ten == "":
                print("Tên không được trống!")
                continue
            tien_str = input("Số tiền mới: ").strip()
            if not tien_str.isdigit():
                print("Số tiền phải là số nguyên dương!")
                continue
            tien = int(tien_str)
            if tien <= 0:
                print("Số tiền phải lớn hơn 0!")
                continue
            kyhan_str = input("Kỳ hạn mới: ").strip()
            if not kyhan_str.isdigit():
                print("Kỳ hạn phải là số nguyên dương!")
                continue
            kyhan = int(kyhan_str)
            if kyhan <= 0:
                print("Kỳ hạn phải lớn hơn 0!")
                continue
            lai_str = input("Lãi suất mới: ").strip()
            # Kiểm tra số thực đơn giản
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
            print("Cập nhật thành công!")

    # 4. Tất toán
    elif chon == "4":
        ma = input("Mã cần tất toán: ").strip().upper()
        tim = None
        for a in saving_accounts:
            if a["account_id"] == ma:
                tim = a
                break
        if tim is None:
            print("Không tìm thấy mã!")
        else:
            tim["status"] = "closed"
            print("Đã tất toán sổ!")

    # 5. Tính lãi dự kiến
    elif chon == "5":
        ma = input("Mã tính lãi: ").strip().upper()
        tim = None
        for a in saving_accounts:
            if a["account_id"] == ma:
                tim = a
                break
        if tim is None:
            print("Không tìm thấy mã!")
        elif tim["status"] != "active":
            print("Sổ đã tất toán!")
        else:
            lai = tim["balance"] * (tim["interest_rate"] / 100) * (tim["term_months"] / 12)
            print(f"Tiền lãi dự kiến: {lai:,.0f}đ | Tổng: {tim['balance'] + lai:,.0f}đ")

    # 6. Rút trước hạn
    elif chon == "6":
        ma = input("Mã kiểm tra: ").strip().upper()
        tim = None
        for a in saving_accounts:
            if a["account_id"] == ma:
                tim = a
                break
        if tim is None:
            print("Không tìm thấy mã!")
        elif tim["status"] != "active":
            print("Sổ đã tất toán!")
        else:
            thang_str = input("Số tháng thực gửi: ").strip()
            if not thang_str.isdigit():
                print("Số tháng phải là số nguyên dương!")
                continue
            thang = int(thang_str)
            if thang <= 0:
                print("Số tháng phải lớn hơn 0!")
                continue
            if thang < tim["term_months"]:
                ls = 0.5
            else:
                ls = tim["interest_rate"]
            lai = tim["balance"] * (ls / 100) * (thang / 12)
            print(f"Lãi thực nhận: {lai:,.0f}đ | Tổng: {tim['balance'] + lai:,.0f}đ")

    # 7. Thoát
    elif chon == "7":
        print("Tạm biệt!")
        break