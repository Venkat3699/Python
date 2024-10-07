import re
text = "DevOps is more familiar"
pattern = r"familiar"
replacement = "simple and easier"
new_text = re.sub(pattern, replacement, text)
print(new_text)

# output is: DevOps is more simple and easier