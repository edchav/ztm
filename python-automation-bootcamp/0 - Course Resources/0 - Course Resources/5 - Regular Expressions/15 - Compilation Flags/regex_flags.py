import re

# text = 'Python is Fun. But PYTHONS are scary!'
#
# matches = re.findall('Python', text, re.IGNORECASE)
#
# print(matches)


text = '''
Python, in your syntax we find delight,
Turning complex problems into something light.
python, your eloquence is truly a sight,
In the world of coding, you are a knight.
'''

matches = re.findall('light.+python', text, re.IGNORECASE | re.DOTALL)
print(matches)
# matches = re.findall('^python',text, re.IGNORECASE | re.MULTILINE)


