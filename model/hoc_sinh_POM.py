[
    {"ID": "SV001", "Họ tên": "Nguyễn Văn An", "Điểm": 8.5, "Xếp loại": "Giỏi"},
    {"ID": "SV002", "Họ tên": "Trần Thị Bình", "Điểm": 9.0, "Xếp loại": "Xuất sắc"},
    {"ID": "SV003", "Họ tên": "Lê Văn Cường", "Điểm": 6.0, "Xếp loại": "Trung bình"},
    {"ID": "SV004", "Họ tên": "Phạm Thị Mai", "Điểm": 7.5, "Xếp loại": "Khá"},
]
class HocSinh:
    def __init__(self, id: str, ho_ten: str, diem: float):
        self.id = id
        self.ho_ten = ho_ten
        self.diem = diem
        self.xep_loai = None

    def xep_loai_hoc_sinh(self):
        if self.diem > 9:
            self.xep_loai = "Xuat sac"
        elif self.diem >= 8 and self.diem <= 9:
            self.xep_loai = "Gioi"
        elif self.diem >= 7 and self.diem < 8:
            self.xep_loai = "Kha"
        else:
            self.xep_loai = "Trung binh"

    def display_info(self):
        print(f"Hoc sinh {self.ho_ten} co diem {self.diem} va xep loai {self.xep_loai}")

