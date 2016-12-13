import re
import argparse

def is_abba(test_string):
    abba_counter = []
    abba_found = False
    for c in test_string:
        if len(abba_counter) == 0:
            abba_counter.append(c)
        elif len(abba_counter) == 1:
            if abba_counter[0] != c:
                abba_counter.append(c)
            else:
                abba_counter = [c]
        elif len(abba_counter) == 2:
            if c == abba_counter[1]:
                abba_counter.append(c)
            else:
                abba_counter.pop(0)
                abba_counter.append(c)
        elif len(abba_counter) == 3:
            if c == abba_counter[0]:
                abba_found = True
                break
            else:
                abba_counter.pop(0)
                abba_counter.pop(0)
                abba_counter.append(c)
    return abba_found

def break_down_ip(ip):
    ip_parts = {"nonhypernet": [], "hypernet": []}
    ip_parts["nonhypernet"].append(re.search('^[a-z]+\[', ip).group(0)[:-1])
    ip_parts["nonhypernet"].extend([m[1:-1] for m in re.findall('\][a-z]+\[', ip)])
    ip_parts["nonhypernet"].append(re.search('\][a-z]+$', ip).group(0)[1:])
    ip_parts["hypernet"].extend([m[1:-1] for m in re.findall('\[[a-z]+\]', ip)])
    return ip_parts

def is_tls(ip):
    ip_parts = break_down_ip(ip)
    for s in ip_parts["hypernet"]:
        if is_abba(s):
            return False
    for s in ip_parts["nonhypernet"]:
        if is_abba(s):
            return True
    return False

def find_aba(string_to_inspect):
    i = 0
    aba_strings = []
    while i < len(string_to_inspect)-2:
       check_aba = string_to_inspect[i:i+3]
       if check_aba[0] == check_aba[2] and check_aba[0] != check_aba[1]:
           aba_strings.append(check_aba)
       i+=1
    return aba_strings

def bab_exists(aba_strings, hypernet_sequences):
    for s in aba_strings:
        bab_sequence = s[1] + s[0] + s[1]
        for h in hypernet_sequences:
            if h.find(bab_sequence) != -1:
                return True
    return False

def supports_sls(ip):
    ip_parts = break_down_ip(ip)
    aba_strings = []
    for nh in ip_parts["nonhypernet"]:
        aba_strings.extend(find_aba(nh))
    if aba_strings:
        return bab_exists(aba_strings, ip_parts["hypernet"])
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int)
    args = parser.parse_args()
    f = open('seven/input', 'r')
    lines = [line.strip() for line in f.readlines()]
    if args.part == 1:
        correct_ip_count = 0
        for line in lines:
            if is_tls(line):
                correct_ip_count += 1
        print(correct_ip_count)
    elif args.part == 2:
        sls_count = 0
        for line in lines:
            if supports_sls(line):
                sls_count += 1
        print(sls_count)
