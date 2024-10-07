import re
from os.path import split

text = "apple,orange,mango,banana"
pattern = r","
split_result = re.split(pattern, text)
print(split_result)

# output is: ['apple', 'orange', 'mango', 'banana']