
text = "python is great"
new_text = text.split()
print(new_text)
# output is: ['python', 'is', 'great']

# Another Example:

text1 = "the,sky,is,blue"
new_text1 = text1.split(",")
print(new_text1)
#output is: ['the', 'sky', 'is', 'blue']

# Real time example:

arn = "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE"
new_arn = arn.split("/")
print(new_arn)
#output is: ['arn:aws:ec2:us-east-1:123456789012:vpc', 'vpc-0e9801d129EXAMPLE']