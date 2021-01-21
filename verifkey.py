import random


def mrz_generator(last_name, first_name, birth_date, sex):
    if len(last_name) > 25:
        while len(last_name) > 25:
            last_name = last_name[:-1]
    elif len(last_name) < 25:
        while len(last_name) < 25:
            last_name += '<'
    first_line = 'ID' + 'FRA' + last_name + random_string(2, 1, 9) + '0' + random_string(3, 1, 9)

    title_code = random_string(12, 1, 9)
    key1 = str(key(title_code))
    key2 = str(key(birth_date))

    if len(first_name) > 14:
        while len(first_name) > 14:
            first_name = first_name[:-1]
    elif len(first_name) < 14:
        while len(first_name) < 14:
            first_name += '<'

    second_line = title_code + key1 + first_name + birth_date + key2 + sex
    final_key = str(key(first_line + second_line))
    second_line += final_key

    print(first_line + '\n' + second_line)
    print(len(first_line))
    print(len(second_line))
    return first_line + '\n' + second_line


def key(string):
    result = 0
    factor = (7, 3, 1)

    for (position, char) in enumerate(string):
        if char == "<":
            value = 0
        elif "0" <= char <= "9":
            value = int(char)
        elif "A" <= char <= "Z":
            value = ord(char) - 55
        else:
            print("Caractère hors bornes")
            break

        result += value * factor[position % 3]
    return result % 10


def random_string(nb_char, start, stop):
    return ''.join([str(random.randrange(start, stop)) for x in range(nb_char)])


if __name__ == '__main__':
    mrz_generator('TANNEN', 'BIFF', '370326', 'M')
