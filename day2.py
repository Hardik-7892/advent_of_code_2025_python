# Advent of Code Day 2
# -------------------Part 1-------------------
""" go through all ranges, 
# ignore odd number of digits"""
def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)

    # Must have even number of digits
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]

def sum_invalid_ids(input_line: str) -> int:
    total = 0
    ranges = input_line.strip().split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total

def read_input_from_file_comma(filename):
    with open(filename, "r") as file:
        # return file.read().strip().split(",")
        # I thought i had to strip the commas but there was no such need
        return file.read()

input = read_input_from_file_comma("input_day_2.txt")
print("-------------------Part 1-------------------")
print(sum_invalid_ids(input))
