def calculate_presents(house_id):
    presents = 0

    for elf_id in range(1,house_id + 1):
        if house_id % elf_id == 0:
            presents += 10 * elf_id
    return presents


input = 29000000

house_id = 947520
presents = 0
max_presents = 0
while house_id > 0:
    house_id -= 64
    presents = calculate_presents(house_id)
    if presents > input:
        print 'id: {}. presents: {}.'.format(house_id, presents)

print house_id

presents = calculate_presents(1000000)
presents = calculate_presents(999990)
print presents
print float(presents)/float(input)


