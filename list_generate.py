#V4 module de création de liste
import time

class v4(object):
    def round_number(num):
        if num - int(num) > 0.5:
            num += 1
        return int(num)
    
    def calculate_large_number(seed, s):
        current_number = seed
        turns_count = 1
        while current_number < 10 ** 1005:
            turns_count += 1 + s * seed
            current_number = current_number * turns_count
        return current_number
    
    def generate(self, seed, Fin, MIN, MAX):
        seed = int(seed)
        liste = {}
        turns_count = 0
        difference = MAX - MIN
        difference_in_leng = len(str(difference))
        difference_in_leng_max = int('9'*difference_in_leng)
        turns_count_large_number = 0
        large_number = str(v4.calculate_large_number(seed, difference_in_leng))
        while Fin != turns_count:
            turns_count += 1
            if turns_count_large_number > 1005:
                large_number = str(v4.calculate_large_number(seed, turns_count))
                turns_count_large_number = 0
            
            t = -1
            temp = 0
            while t+1 != difference_in_leng:
                t += 1
                turns_count_large_number += 1
                temp += int(large_number[int(large_number[turns_count_large_number])+int(large_number[turns_count_large_number+1])+int(large_number[turns_count_large_number+2])])*(10**t)
            
            temp = (temp*difference)/difference_in_leng_max
            liste[turns_count] = v4.round_number(temp) + MIN
        return liste