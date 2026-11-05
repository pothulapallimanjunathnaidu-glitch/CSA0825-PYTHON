correct_otp = "4821"
correct_answer = "blue"
verified = False

for attempt in range(3):
    entered = input("Enter OTP: ").strip()

    if not entered:
        print("Blank input is not counted.")
        continue

    if entered == correct_otp:
        verified = True
        break

    print("Wrong OTP.")

if not verified:
    answer = input("Registered security word: ").strip().lower()
    if answer == correct_answer:
        final_otp = input("One final OTP attempt: ").strip()
        verified = (final_otp == correct_otp)

print("Access granted." if verified else "Access denied.")
