__author__ = 'Filip'

def look_and_say(s):
    new_input = ''
    last_character = ''
    count = 0
    for character in s:
        if character != last_character and last_character != '':
            new_input += str(count) + last_character
            count = 1
        else:
            count += 1
        last_character = character
    new_input += str(count) + last_character

    return new_input


input = '1321131112'

for i in range(50):
     input = look_and_say(input)

print(len(input))

