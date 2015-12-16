__author__ = 'Filip'

with open('input.txt') as f:
    text = f.read()

long_text = text.replace('\n','')
longer_text = long_text.replace("\\", "\\\\").replace('"','\\"')
decoded_string = text.decode('string_escape')
short_text = decoded_string.replace('"\n"','')

long_text_length = len(long_text)
short_text_length = len(short_text) - 2
longer_text_length = len(longer_text)

print long_text_length - short_text_length
print longer_text_length - long_text_length
print long_text
print short_text
