row1 = ["T", "T", "T"]
row2 = ["T", "T", "T"]
row3 = ["T", "T", "T"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

mappoint = int(input("enter map point "))

map[round(mappoint/10)-1][round(mappoint % 10)-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
