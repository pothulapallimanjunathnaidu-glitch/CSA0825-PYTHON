def validate_registration(value):
    cleaned = value.replace(" ", "").replace("-", "").upper()

    if len(cleaned) not in (9, 10):
        return False, cleaned

    if not cleaned[0:2].isalpha() or not cleaned[2:4].isdigit():
        return False, cleaned

    if len(cleaned) == 9:
        letters = cleaned[4:5]
        digits = cleaned[5:9]
    else:
        letters = cleaned[4:6]
        digits = cleaned[6:10]

    valid = letters.isalpha() and digits.isdigit()
    return valid, cleaned


registration = input("Enter registration number: ")
valid, cleaned = validate_registration(registration)
print(cleaned, "is valid" if valid else "is invalid")
