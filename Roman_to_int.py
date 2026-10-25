def roman_to_int(roman_numeral):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    integer_value = 0
    i = 0
    while i < len(roman_numeral):
        current_char = roman_numeral[i]
        current_value = roman_map[current_char]

        # Check for subtractive cases
        if i + 1 < len(roman_numeral):
            next_char = roman_numeral[i+1]
            next_value = roman_map[next_char]
            if current_value < next_value:
                integer_value += (next_value - current_value)
                i += 2 
                continue

        # Otherwise, add the current value
        integer_value += current_value
        i += 1
    return integer_value

# Example usage:
print(roman_to_int("MCMXCIV"))  # Output: 1994  
print(roman_to_int("CC"))   # Output: 58