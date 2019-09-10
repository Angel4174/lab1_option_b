# CS3
# Angel Rodriguez II
# Lab 1 - Option B
# Diego Aguirre
# 09-09-2019
# Purpose: This code will generate numbers 000 to 9999999 recursively
#           and find a hashed password using a brute_force technique.

import hashlib
import itertools

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def main():
    with open("password.txt", 'r') as f:
        for line in f:
            print(line, end=" ")  # prints each line of the file provided
            currentline = line.split(
                ",")  # splits up each line where it is seperated by a comma and stores it into an array.
            user_num = currentline[0]
            salt_val = currentline[1]
            hash_val = currentline[2]
            set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for i in range(3, 8):  # will make sure to only generate number values from 3 to 7 digits long
                permutation_with_rep([], set, salt_val, hash_val, user_num, i)
            # print(user_num + " password: " + brute_Force(3, 8, 1000, salt_val, hash_val))


# def add_zeros(n,zeros):
#     guess = str(n)
#     while len(guess) < zeros: #checks to see if the generated guess is less than the length it is supposed to be.
#         guess = "0" + guess #adds the zeros to the beginning of the number
#     return guess

# def brute_Force(n, max, limit, salt_val, hash_val):
#     if n < max:
#         for i in range(limit):
#             guess = add_zeros(i, n)
#             salt_guess = guess + salt_val #concatenates the guess with the salt value
#             if hash_with_sha256(salt_guess) == hash_val.rstrip(): #calls the hash method and compares the guess and salted hash with the actual hash value.
#                 return guess
#         return brute_Force(n+1, max, limit*10, salt_val, hash_val) #recursive call that adds 1 digit each call, and increased the range of the for loop to the correct value.

def permutation_with_rep(cur_perm, unused_set, salt_val, hash_val, user_num, i):
    if(len(cur_perm) == i):
        guess = ""
        guess = guess.join(cur_perm) #.join method will create a string from the characters in the cur_perm array
        salt_guess = guess + salt_val
        if hash_with_sha256(salt_guess) == hash_val.rstrip(): #compares the hashed guess with the correct hash
            print(user_num + " password: " + guess)
        return
    for item in unused_set:
        new_cur_perm = cur_perm.copy()
        new_unused_set = unused_set.copy()
        new_cur_perm.append(item)
        permutation_with_rep(new_cur_perm, new_unused_set, salt_val, hash_val, user_num, i)

main()