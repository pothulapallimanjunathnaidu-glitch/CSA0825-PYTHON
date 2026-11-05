import re

value = input("Enter registration number: ")
cleaned = re.sub(r"[ -]", "", value).upper()
pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"

if re.fullmatch(pattern, cleaned):
    print(cleaned, "is valid")
else:
    print(cleaned, "is invalid")
