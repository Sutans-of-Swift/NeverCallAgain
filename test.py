#! /usr/bin/env python3
import random
import string

def get_random_id(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

message_id = get_random_id(10)
print(message_id)

with open("testfile.txt", "w") as f:
    f.write(message_id+"\n")
