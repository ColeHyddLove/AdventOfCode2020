# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:51:19 2021

@author: colel
"""

text_file = open("input_Day5.txt","r")
S = text_file.read()
text_file.close()

S_split = S.split("\n")

#print(S_split)
ex = "BBFFBBFRLL"


def get_ID(string):
    num_rows = range(128)
    seat_row_min = min(num_rows)
    seat_row_max = max(num_rows)
    ##print(seat_row_min, seat_row_max)
    
    for c in string[:-3]:
        #Consider lower half
        if c == "F":
            seat_row_max = int((len(num_rows)/2) - 1) + seat_row_min
            num_rows = range(seat_row_min, seat_row_max+1)
            ##print(seat_row_min, seat_row_max)
            continue
        #Consider upper half
        seat_row_min = int(len(num_rows)/2) + seat_row_min
        num_rows = range(seat_row_min, seat_row_max+1)
        ##print(seat_row_min, seat_row_max)
        
    
    ##print("Final: ", seat_row_min, seat_row_max)
    ##print("Final Row: ", int(seat_row_min))
    
    num_cols = range(8)
    seat_col_min = min(num_cols)
    seat_col_max = max(num_cols)
    ##print(seat_col_min, seat_col_max)
    
    for c in string[-3:]:
        #Consider left half
        if c == "L":
            seat_col_max = int((len(num_cols)/2)-1) + seat_col_min
            num_cols = range(seat_col_min, seat_col_max+1)
            ##print(seat_col_min, seat_col_max)
            continue
        #Consider right half
        seat_col_min = int(len(num_cols)/2) + seat_col_min
        num_cols = range(seat_col_min, seat_col_max+1)
        ##print(seat_col_min, seat_col_max)
        
    ##print("Final Column: ", int(seat_col_min))
    
    ##print("Seat ID: ", 8*int(seat_row_min)+int(seat_col_min))
    return 8*int(seat_row_min)+int(seat_col_min)

##print(get_ID(ex))
    
def find_bigID(S):
    big_ID = 0
    
    for s in S:
        #print(s)
        if big_ID < get_ID(s):
            #print(get_ID(s))
            big_ID = get_ID(s)
            
    return big_ID

print("Largest ID: ", find_bigID(S_split))

def list_IDs(S):
    seats = {}
    for s in S:
        seats[get_ID(s)] = s
    
    ##print(seats)
    
    for n in range(len(seats)):
        if n+1 in seats and n-1 in seats and n not in seats:
            return n
    
    return -1

print("My seat ID: ", list_IDs(S_split))


    
