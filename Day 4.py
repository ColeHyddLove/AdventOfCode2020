# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 01:06:13 2021

@author: colel

"""

text_file = open("input_Day4.txt","r")
S = text_file.read()
text_file.close()

#print(S)
S_split = S.split("\n\n")
S_ssplit = [string.replace("\n", " ") for string in S_split]
S_s3plit = [string.split() for string in S_ssplit]

def conv2dict(passport_list):
    dictionary = {}
    
    for item in passport_list:
        item_parts = item.split(":")
        key = item_parts[0]
        value = item_parts[1]
        dictionary[key] = value
    
    return dictionary

passports = [conv2dict(item) for item in S_s3plit]

def is_valid_pass(passport):
    has_birth_year = "byr" in passport
    has_issue_year = "iyr" in passport
    has_expiration_year = "eyr" in passport
    has_height = "hgt" in passport
    has_hair_color = "hcl" in passport
    has_eye_color = "ecl" in passport
    has_passport_id = "pid" in passport
    has_country_id = "cid" in passport
    
    return (has_birth_year and
            has_issue_year and
            has_expiration_year and
            has_height and
            has_hair_color and
            has_eye_color and
            has_passport_id)
    
valid_passports = [passport for passport in passports if is_valid_pass(passport)]
print(len(valid_passports))

def has_valid_values(passport):
    has_valid_birth_year = 1920 <= int(passport["byr"]) <= 2002
    has_valid_issue_year = 2010 <= int(passport["iyr"]) <= 2020
    has_valid_expiration_year = 2020 <= int(passport["eyr"]) <= 2030
    
    has_valid_height = False
    height_units = passport["hgt"][-2:]
    if height_units == "cm":
        height = int(passport["hgt"][:-2])
        has_valid_height = 150 <= height <= 193
    elif height_units == "in":
        height = int(passport["hgt"][:-2])
        has_valid_height = 59 <= height <= 76
        
    def is_valid_hex_string(string):
        test_value = string.lower()
        is_valid = True

        for character in test_value:
            if character not in "0123456789abcdef":
                is_valid = False
                break

        return is_valid
        
    has_valid_hair_color = False
    if len(passport["hcl"]) == 7:
        digits = passport["hcl"][1:]
        has_valid_hair_color = is_valid_hex_string(digits)
            
    has_valid_eye_color = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    def is_valid_passport_id(value):
        is_valid = False
        
        if len(value) == 9:
            is_valid = True

            for character in value:
                if character not in "0123456789":
                    is_valid = False
                    break
        
        return is_valid
    
    has_valid_passport_id = is_valid_passport_id(passport["pid"])
                 
    return (has_valid_birth_year and
            has_valid_issue_year and
            has_valid_expiration_year and
            has_valid_height and
            has_valid_hair_color and
            has_valid_eye_color and
            has_valid_passport_id)
    
real_valid_passports = [passport for passport in valid_passports if has_valid_values(passport)]
print(len(real_valid_passports))