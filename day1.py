# Advent of Code Day 1
# -------------------Part 1-------------------
"""
map L and R with + and -
variable sum = 50 (initial condition), count = 0
while input in inputs:
  split input into L/R and number
  sum + or - = number (depending on L or R)
  if sum == 0: count +=1
  if sum <0: sum = 100 + sum
  if sum >=100: sum = sum -100
return count
"""
def find_password(inputs):
    total = 50   # starting position
    count = 0    # number of times dial points at 0

    for instruction in inputs:
        direction = instruction[0]
        number = int(instruction[1:])

        if direction == 'L':
            total -= number
        elif direction == 'R':
            total += number

        total = total % 100

        if total == 0:
            count += 1
        # print(f"Total : {total}, Count : {count}")

    return count

def read_input_from_file(filename):
    with open(filename, "r") as file:
        # strip whitespace and ignore empty lines
        return [line.strip() for line in file if line.strip()]

inputs = read_input_from_file("inputs/input_day_1.txt")
password = find_password(inputs)
print("-------------------Part 1-------------------")
print(password)

# -------------------Part 2-------------------
def find_password_part2(inputs):
    total = 50
    count = 0
    for instruction in inputs:
        direction = instruction[0]
        steps = int(instruction[1:])

        # count full revolutions
        count += steps // 100
        remaining = steps % 100
        
        if direction == 'R':
            total += remaining
            if total > 99:
                total -= 100
                count += 1
        elif direction == 'L':
            total -= remaining
            if total == 0 and remaining != 0:
                # landed exactly on zero
                count += 1
            elif total < 0:
                # wrapped around
                if total + remaining != 0:
                    # did not start on zero
                    count += 1
                total += 100

    return count

password = find_password_part2(inputs)
print("-------------------Part 2-------------------")
print(password)