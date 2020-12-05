import re


def valid(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if fields - passport.keys():
        return False
    if int(passport['byr']) > 2002 or int(passport['byr']) < 1920:
        return False
    if int(passport['iyr']) > 2020 or int(passport['iyr']) < 2010:
        return False
    if int(passport['eyr']) > 2030 or int(passport['eyr']) < 2020:
        return False
    if not re.search("#([0-9a-f]{6})", passport['hcl']):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if len(passport['pid']) != 9 or not passport['pid'].isnumeric():
        return False    
    if not passport['hgt'].endswith('cm') and not passport['hgt'].endswith('in'):
        return False
    if passport['hgt'].endswith('cm'):
        if int(passport['hgt'][:-2]) > 193 or int(passport['hgt'][:-2]) < 150:
            return False
    if passport['hgt'].endswith('in'):
        if int(passport['hgt'][:-2]) > 76 or int(passport['hgt'][:-2]) < 59:
            return False
    return True


with open('Day 4/input.txt') as f:
    data = f.readlines()

data = [entry.strip().split(',') for entry in data]

passports = []
for passport in data:
    passports.append(dict(p.split(':') for p in passport))

passports = [passport for passport in passports if valid(passport)]
print(len(passports))
