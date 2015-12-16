__author__ = 'Filip'

def step(text):
    s = list(text)
    for i in range(len(s)-1, -1, -1):
        if s[i] == 'z':
            s[i] = 'a'
        else:
            s[i] = chr(ord(s[i])+1)
            return ''.join(s)

def validate(text):
    if 'i' in text or 'o' in text or 'l' in text:
        return False

    paircount = 0
    previous = None
    characters = iter(text)
    for char in characters:
        if char == previous:
            paircount += 1
            if paircount >= 2:
                break
            previous = next(characters, None)
            continue
        previous = char
    else:
        return False

    for i in range(len(text)-2):
        o0 = ord(text[i])
        o1 = ord(text[i+1])
        o2 = ord(text[i+2])
        if o2-o1==1 and o1-o0==1:
            return True

    return False


input = 'cqjxjnds'

printouts = 0
while printouts < 2:
   input = step(input)
   if validate(input):
       print input
       printouts += 1

