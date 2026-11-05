correct_otp = "4821"
attempts = 0
verified = False

while attempts < 3:
    entered = input("Enter OTP (blank to skip): ").strip()

    if entered == "":
        print("Blank input is not counted.")
        continue

    attempts += 1

    if entered == correct_otp:
        verified = True
        print("OTP verified.")
        break

    print("Incorrect OTP. Attempts used:", attempts)
else:
    print("Maximum attempts reached.")

if not verified:
    print("Access denied.")
