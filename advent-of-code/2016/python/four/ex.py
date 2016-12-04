import argparse
import functools
import re

def parse_encrypted_name(encrypted_name):
    m = re.search("[a-z-]+[a-z]", encrypted_name)
    name = m.group(0)
    m = re.search("[0-9]+", encrypted_name)
    sector_id = int(m.group(0))
    m = re.search("\[[a-z]+\]", encrypted_name)
    checksum = m.group(0)[1:-1]
    return (name, sector_id, checksum)

def is_checksum_valid(name, checksum):
    character_counts = {}
    for character in name.replace("-", ""):
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    character_counts = sorted(character_counts.items(), key=functools.cmp_to_key(ltfunc), reverse=True)

    checksum_generated = ""
    for k in character_counts[:5]:
        checksum_generated += k[0]
    return checksum_generated == checksum

def ltfunc(a,b):
  if a[1]==b[1]:
    if a[0] < b[0]:
      return 1
    else:
      return -1
  else:
    if a[1] < b[1]:
      return -1
    else:
      return 1

def decrypt_name(encrypted_string, sector_id):
    s = ""
    for c in encrypted_string:
        if c == "-":
            s += " "
        else:
            s += chr(((ord(c) - 97 + sector_id)%26)+97)
    return s

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int)
    args = parser.parse_args()
    f = open('four/input', 'r')
    lines = f.readlines()
    codes = []
    for line in lines:
        codes.append(line.strip())
    if args.part == 1:
        sum_of_sector_ids = 0
        for code in codes:
            encryption_parts = parse_encrypted_name(code)
            if is_checksum_valid(encryption_parts[0], encryption_parts[2]):
                sum_of_sector_ids += encryption_parts[1]
        print(sum_of_sector_ids)
    elif args.part == 2:
        for code in codes:
            encryption_parts = parse_encrypted_name(code)
            if is_checksum_valid(encryption_parts[0], encryption_parts[2]):
                decrypted_name = decrypt_name(encryption_parts[0], encryption_parts[1])
                if "north" in decrypted_name.lower():
                    print(decrypted_name, encryption_parts[1])
