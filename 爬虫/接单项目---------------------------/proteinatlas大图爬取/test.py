import re

text = 'The quick brown fox jumps over the lazy dog.'
pattern = r'((quick|lazy) (brown|dog))'
matches = re.findall(pattern, text)
print(matches)
