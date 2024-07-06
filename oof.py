from hashlib import sha1 as OOF_sha1
from random import choice as OOF_choice
from string import ascii_lowercase as OOF_ascii_lowercase
from random import randint as OOF_randint


def gen_OFF_word(size=10):
    return "".join([OOF_choice(OOF_ascii_lowercase) for i in range(size)])


OOF_hash = "O_O_F"
OOF_word = "O_O_F"
OOF_counter = 0
OOFS = list()
OOF_len = int(input("How many OOFs do you want? [don't try too many] "))
OOF_words = list()
OOF_hashes = list()
OOF_size = int(input("how much do you want to [OO]F? "))

assert OOF_size >= 2, "OOF must be at least 2"
OOF_string = ("O" * OOF_size) + "F"

for OOF in range(OOF_len):

    while OOF_string not in OOF_hash:
        OOF_counter += 1
        OOF_word = gen_OFF_word(OOF_randint(10, 12))
        OOF_hash = OOF_sha1(OOF_word.encode()).hexdigest().replace("0", "O").upper()

    OOF_words.append(OOF_word)
    OOF_hashes.append(OOF_hash)
    OOFS.append(OOF_counter)
    OOF_counter = 0
    OOF_word = "O_O_F"
    OOF_hash = "O_O_F"

for OOF_word, OOF_hash, OOF_counter in zip(OOF_words, OOF_hashes, OOFS):
    OOF_index = OOF_hash.index("OOF")
    OOF_hash = (
        OOF_hash[:OOF_index] + "[" + OOF_string + "]" + OOF_hash[OOF_index + OOF_size :]
    )
    print(f"{OOF_counter}\t{OOF_word}\t{OOF_hash}")

OOF_AVG = sum(OOFS) / OOF_len
print(f"average required to OOF is {OOF_AVG}")
