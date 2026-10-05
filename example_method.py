list_score = [8.5, 9.0, 6.0, 7.5]

# for score in list_score:
#     if score >=8 and score < 9:
#         print(f"Hoc sinh gioi trong list la: {score}")
#         break
#     else:
#         print("Khong co hoc sinh gioi nao trong list")


def is_rank_in_89(score):
    if score >= 8 and score < 9:
        return True
    else:
        return False


for score in list_score:
    if is_rank_in_89(score):
        print(f"Hoc sinh gioi trong list la: {score}")
        break
    else:
        print("Khong co hoc sinh gioi nao trong list")
