import re
import pandas as pd

input_file = 'input.txt'
digits = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
            'eight', 'nine')

def get_digit(text: str) -> str:
    '''Returns the corresponding digit to a string number'''
    if text.isnumeric():
        return text
    else:
        return str(digits.index(text))

def first_last_num(text: str) -> int:
    '''Selects the first and last number in a string and
    returns the combined number.

    regex explained:

        \d  looks for any digits

        |   or operator

        $=  look-ahead operator
    '''

    regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
    # regex = r'(\d)' # solution for part 1
    nums = re.findall(regex, text)

    if nums:
        return int(get_digit(nums[0]) + get_digit(nums[-1]))
    else:
        return 0

if __name__ == '__main__':

    df = pd.read_csv(input_file, names=['data'])
    df['calibration'] = df['data'].apply(first_last_num)
    print(df['calibration'].sum())