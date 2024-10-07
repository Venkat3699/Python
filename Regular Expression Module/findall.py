import re
from re import search

text = "the sky is blue"
pattern = r"blue"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")

# Output is: pattern found: blue


# Another Example:
new = "DevOps is more familiar"
pattern = r"DevOps"

search = re.search(pattern, new)
if search:
    print("pattern found:", search.group())
else:
    print ("pattern not found")

# Output:
# pattern found: more
# pattern found: DevOps
# pattern not found (here, I had given AWS for Search)