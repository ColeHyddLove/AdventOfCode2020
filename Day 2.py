# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 02:50:00 2021

@author: colel
"""

"""
The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" 

You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords
wouldn't have been allowed by the Official Toboggan Corporate Policy that was
in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of
passwords (according to the corrupted database) and the corporate policy when
that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy
indicates the lowest and highest number of times a given letter must appear for
the password to be valid. For example, 1-3 a means that the password must 
ontain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg,
is not; it contains no instances of b, but needs at least 1. The first and
third passwords are valid: they contain one a or nine c, both within the limits
of their respective policies.

How many passwords are valid according to their policies?
"""
text_file = open("input_Day2.txt","r")
S = text_file.readlines()
text_file.close()

#Section of Test Code for rsplit() method of string
'''
poltest = S[21]
print(poltest)
s1,s2 = poltest.rsplit("-")
print(s1)
lowlim = int(s1)
print(s2)
ss2 = s2.rsplit(" ")[0]
uplim = int(ss2)
s3,s4 = s2.rsplit(": ")
print(lowlim, uplim, s3[len(s3)-1])
''' 

"""
Input: Set of Strings
Output: Number of Valid Passwords
"""

def countInvalid(S):
    count_invalid = 0;
    
    for i in range(len(S)):
        pol = S[i]
        s1,s2 = pol.rsplit("-")
        lowlim = int(s1)
        uplim = int(s2.rsplit(" ")[0])
        s3,s4 = s2.rsplit(": ")
        charspec = s3[len(s3)-1]
        
        pw = pol.rsplit(": ")[1]
        charsum = 0;
        
        for i in range(len(pw)):
            if pw[i] == charspec:
                charsum+=1;
            if pw[i] == "\n":
                continue
        if charsum < lowlim or charsum > uplim:
            count_invalid+=1;
        
    return len(S)-count_invalid
    
print(countInvalid(S))

"""
While it appears you validated the passwords correctly, they don't seem to be
what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the 
password policy rules from his old job at the sled rental place down the street!
The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the
first character, 2 means the second character, and so on. (Be careful; Toboggan
Corporate Policies have no concept of "index zero"!) Exactly one of these 
positions must contain the given letter. Other occurrences of the letter are 
irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

def countInvalid2(S):
    count_invalid = 0;
    
    for i in range(len(S)):
        pol = S[i]
        s1,s2 = pol.rsplit("-")
        lowloc = int(s1)
        uploc = int(s2.rsplit(" ")[0])
        s3,s4 = s2.rsplit(": ")
        charspec = s3[len(s3)-1]
        
        pw = s4
        valpass = 0
        
        if pw[lowloc-1] == charspec:
            valpass+=1
        if pw[uploc-1] == charspec:
            valpass+=1
        if valpass > 1 or valpass == 0:
            count_invalid+=1
        
    return len(S)-count_invalid

print(countInvalid2(S))