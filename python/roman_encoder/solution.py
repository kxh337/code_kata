# link to problem https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

roman_dict = {
    1:'I',
    5:'V',
    10:'X',
    50:'L',
    100:'C',
    500:'D',
    1000:'M',
}

def get_roman_char(val, power):
    power = power + 1
    # Get characters
    roman_chars = []
    if power == 1:
       roman_chars.append(roman_dict[1])
       roman_chars.append(roman_dict[5])
       roman_chars.append(roman_dict[10])
    elif power == 2:
       roman_chars.append(roman_dict[10])
       roman_chars.append(roman_dict[50])
       roman_chars.append(roman_dict[100])
    elif power == 3:
       roman_chars.append(roman_dict[100])
       roman_chars.append(roman_dict[500])
       roman_chars.append(roman_dict[1000])
    elif power == 4:
       roman_chars.append(roman_dict[1000])

    roman_str = ''
    if val < 4:
        # just add char1
        while val > 0:
            roman_str = roman_str + roman_chars[0]
            val = val - 1
    elif val == 4:
        # add char1  then char5
        roman_str = roman_str + roman_chars[0]
        roman_str = roman_str + roman_chars[1]
    elif val > 4 and val < 9:
        # add  char5 then char1's
        roman_str = roman_str + roman_chars[1]
        val = val - 5
        while val > 0:
            roman_str = roman_str + roman_chars[0]
            val = val - 1
    elif val == 9:
        # val is 9
        roman_str = roman_str + roman_chars[0]
        roman_str = roman_str + roman_chars[2]
    else:
        # just add char 3 # number of times
        while val > 0:
            roman_str = roman_str + roman_chars[2]
            val = val - 1
    return roman_str


def solution(n):
    # generate list for each decimal value
    dec_val = []
    while n >= 1:
        val = int(n % 10)
        dec_val.append(val)
        n = n / 10

    roman_str_list = []
    # iterate through the decimal list and
    for power, val in enumerate(dec_val):
        roman_str = get_roman_char(val, power)
        roman_str_list.append(roman_str)

    return ''.join(roman_str_list[::-1])

print(solution(1000))
