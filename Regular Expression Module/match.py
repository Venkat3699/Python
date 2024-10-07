import re

text = "The sky is black"
pattern = r"black"

match = re.match(pattern, text)
if match:
    print("match found:", match.group())
else:
    print ("match not found")

# Output is: match not found
# re.match() checks for a match only at the beginning of the string. Since "The sky is black" doesn't start with "black," it doesn't find a match.
# re.search(), on the other hand, scans through the entire string and finds the first occurrence of the pattern anywhere in the text, which is what you're aiming for in this case.