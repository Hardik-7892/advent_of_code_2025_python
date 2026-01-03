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


def part2(lines, k=12):
    """
    Creating that helper function payed off, reusing it in part 2
    Generalized Part 2: pick k digits per bank to form the largest number.
    """
    total_joltage = 0

    for line in lines:
        n = len(line)
        start = 0
        selected_digits = []

        for remaining in range(k, 0, -1):
            # End index: last position we can pick this digit so enough remain
            end = n - remaining + 1
            max_digit, pos = max_in_range(line, start, end)
            selected_digits.append(str(max_digit))
            start = pos + 1  # next search starts after the picked digit

        # Combine selected digits to form the number
        total_joltage += int("".join(selected_digits))

    return total_joltage

print("-------------------Part 2-------------------")
print(part2(line))


# -------------------Part 2 optimized using stack-------------------
def part2_optimized(lines, k=12):
    total = 0

    for line in lines:
        n = len(line)
        stack = []
        for i, digit_char in enumerate(line):
            digit = int(digit_char)
            # While stack not empty, current digit bigger, and enough digits left
            while stack and digit > stack[-1] and len(stack) + (n - i) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(digit)
        # Form number
        total += int("".join(map(str, stack[:k])))
    return total

print("-------------------Part 2 optimized-------------------")
print(part2_optimized(line))