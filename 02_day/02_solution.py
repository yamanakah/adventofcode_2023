import re
import numpy as np
import pandas as pd
from io import StringIO

input_file = '02_input.txt'
bag = {'red': 12, 'green': 13, 'blue': 14}
colors = list(bag.keys())

def max_cubes(data: str, color: str) -> int:
    '''Return the maximum number of revealed cubes for corresponding color'''
    
    regex = fr"(\d+) {color}"
    nums = [int(x) for x in re.findall(regex, data)]
    if nums:
        return int(max(nums))
    else:
        return 0

def is_possible_game(data: str) -> bool:
    '''Returns whether game is possible given bag restrictions'''

    for c in colors:
        if max_cubes(data=data, color=c) > bag[c]:
            return False
    
    return True

def cubeset_power(data: str) -> int:
    '''Returns the product of the maximum number of revealed cubes for each
      color'''
    
    nums = []
    for c in colors:
        nums.append(max_cubes(data, color=c)) 

    return  np.prod(nums)

if __name__ == '__main__':

    with open(input_file) as f:
        data = [line for line in f]
    data = pd.Series(data)

    # part 1
    bool_list = data.apply(is_possible_game)
    print(sum(data.index[bool_list] + 1))

    # part 2
    power = data.apply(cubeset_power)
    print(sum(power))