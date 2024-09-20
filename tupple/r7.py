import re
txt = "The rain in Spain"
x = re.findall("[^a-z]", txt)
print(x)
#o/p:
#['T', ' ', ' ', ' ', 'S']
