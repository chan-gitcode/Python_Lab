[
    {"ID": "SV001", "Họ tên": "Nguyễn Văn An", "Điểm": 8.5, "Xếp loại": "Giỏi"},
    {"ID": "SV002", "Họ tên": "Trần Thị Bình", "Điểm": 9.0, "Xếp loại": "Xuất sắc"},
    {"ID": "SV003", "Họ tên": "Lê Văn Cường", "Điểm": 6.0, "Xếp loại": "Trung bình"},
    {"ID": "SV004", "Họ tên": "Phạm Thị Mai", "Điểm": 7.5, "Xếp loại": "Khá"},
]
lop_hoc ="I'm a variable"

class HocSinh:
    def __init__(self, id: str, ho_ten: str, diem: float):
        self.id = id
        self.ho_ten = ho_ten
        self.diem = diem
        self.xep_loai = None

    # def nhap_thong_tin(self, id, ho_ten, diem):
    #     self.id = id
    #     self.ho_ten = ho_ten
    #     self.diem = diem

    def xep_loai_hoc_sinh(self):
        print(f"{lop_hoc} 1")
        if self.diem > 9:
            self.xep_loai = "Xuat sac"
        elif self.diem >= 8 and self.diem <= 9:
            self.xep_loai = "Gioi"
        elif self.diem >= 7 and self.diem < 8:
            self.xep_loai = "Kha"
        else:
            self.xep_loai = "Trung binh"


hoc_sinh_1 = HocSinh(id="SV001", ho_ten="Nguyễn Văn An", diem=8.5)
hoc_sinh_1.xep_loai_hoc_sinh()
def hello():
    print(f"{lop_hoc} 2")

print(f"{lop_hoc} 3")
print(f"Hoc sinh {hoc_sinh_1.ho_ten} co diem {hoc_sinh_1.diem} va xep loai {hoc_sinh_1.xep_loai}")
