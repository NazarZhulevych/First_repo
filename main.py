import re

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email, re.IGNORECASE)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("User name:", match.group(1))
    print("User domain:", match.group(2))
else:
    print("Not found")

