def merge_age_and_height(ages, heights):
    return reversed(list(zip(ages,heights)))
    
def print_age_and_height(ages_and_heights):
    for pair in ages_and_heights:
        print(f"Idade {pair[0]}, altura {pair[1]}")
    

ages = [34, 25, 26]
heights = [176, 165, 190]
print_age_and_height(merge_age_and_height(ages, heights))



