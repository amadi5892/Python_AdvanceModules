import re 

text = "The agent's phone number is 408-555-1234. Call soon!"

print('phone' in text)

pattern = 'phone'

print(re.search(pattern,text))

print(3+4)