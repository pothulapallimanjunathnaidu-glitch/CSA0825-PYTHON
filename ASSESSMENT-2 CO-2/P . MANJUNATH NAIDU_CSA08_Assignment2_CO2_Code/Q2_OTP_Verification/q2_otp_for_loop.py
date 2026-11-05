correct_otp = "4821"
verified = False

for attempt in range(3):
    entered = input("Enter OTP: ").strip()

    if entered == "":
        print("Blank input is not counted.")
        continue

    if entered == correct_otp:
        verified = True
        print("OTP verified.")
        break

    print("Incorrect OTP.")

if not verified:
    print("Access denied.")
