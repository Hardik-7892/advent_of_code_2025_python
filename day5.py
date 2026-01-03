# Advent of Code day 5
# -------------------Part 1-------------------
"""
Freshness mapping approach
array to mark which ingredient IDs are fresh, based on a direct lookup
"""
def read_input(filename):
    # reader function to get input and segregate ranges and ids
    with open(filename, "r") as f:
        lines = f.read().strip().split("\n")
    
    fresh_ranges = []
    available_ids = []
    is_ranges = True

    for line in lines:
        if line == "":
            is_ranges = False
            continue
        
        if is_ranges:
            parts = line.split("-")
            start = int(parts[0])
            end = int(parts[1])
            fresh_ranges.append((start, end))
        else:
            available_ids.append(int(line))

    return fresh_ranges, available_ids

def freshness_map_approach(fresh_ranges, available_ids):
    fresh_count = 0
    
    for ingredient_id in available_ids:
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break  # Once found, stop checking other ranges for this ID

    return fresh_count

print("-------------------Part 1 approach 1-------------------")
fresh_ranges, available_ids = read_input("inputs/input_day_5.txt")

print("Freshness mapping approach count:", freshness_map_approach(fresh_ranges, available_ids))


"""
Range Sorting Approach
relies on sorting the fresh ranges and checking each available ingredient ID against these sorted ranges
time-optimized for handling smaller ranges or fewer IDs, where sorting is quick.
"""
def range_sorting_approach(fresh_ranges, available_ids):
    fresh_ranges.sort()

    # Check each available ID against ranges
    fresh_count = 0
    for id_val in available_ids:
        for start, end in fresh_ranges:
            if start <= id_val <= end:
                fresh_count += 1
                break  # stop at first matching range

    return fresh_count

print("-------------------Part 1 approach 2-------------------")
print("Rage sorting approach count:", range_sorting_approach(fresh_ranges, available_ids))


# -------------------Part 2-------------------