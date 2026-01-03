# Advent of Code day 3
# -------------------Part 1-------------------
"""
find biggest digit from 0 to n-1
find biggest digit from position to n
"""
def max_in_range(seq, start, end):
    """
    Returns the largest digit in seq[start:end] and its position.
    """
    max_digit = -1
    max_pos = -1
    for i in range(start, end):
        digit = int(seq[i])
        if digit > max_digit:
            max_digit = digit
            max_pos = i
    return max_digit, max_pos


def part1(lines):
    total_joltage = 0

    for line in lines:
        # Step 1: tens digit (exclude last char)
        tens_digit, tens_pos = max_in_range(line, 0, len(line)-1)

        # Step 2: ones digit (everything after tens digit)
        ones_digit, _ = max_in_range(line, tens_pos+1, len(line))

        # Step 3: form two-digit number and add to total
        total_joltage += tens_digit * 10 + ones_digit

    return total_joltage

def read_input(filename):
    with open(filename, "r") as f:
        # Strip newline characters and ignore empty lines
        return [line.strip() for line in f if line.strip()]

line = read_input("inputs/input_day_3.txt")
print("-------------------Part 1-------------------")
print(part1(line))