# CSA08 – Python Programming Assignment 2 (CO2)

## Student details
- Student Name: Enter your name
- Register Number: Enter your register number
- Department / Branch: Enter your department
- Class / Section: Enter your class and section
- Python Version: Python 3.10 or later

## Required GitHub repository name
`CSA08-<RegisterNumber>-Assignment2`

## Requirements
- Python 3.10 or later (Q1 uses `match-case`).
- No third-party Python packages are required.

## Folder structure
- `Q1_Electricity_Subsidy/` – if/elif/else, nested if, Boolean condition, match-case
- `Q2_OTP_Verification/` – while loop, for loop, break, continue, loop-else, security-question example
- `Q3_Registration_Validator/` – string methods and regular-expression validation
- `Q4_String_Performance/` – concatenation, join, f-strings and timing benchmark
- `Q5_Functions_Scope/` – default arguments, parameter types, multiple return values and scope
- `Q6_Stair_Recursion/` – naive recursion, memoization, call counting and iteration
- `Q7_Design_Challenge/` – optimized message generation and benchmark

## Run
Open a terminal in the relevant folder and run, for example:
`python q1_subsidy.py`

Run the other `.py` files in the same way. For OTP, the demonstration OTP is `4821`.

## Important submission notes
1. Replace the student-detail placeholders in the assignment document and this README.
2. Run every program on your own computer.
3. Capture genuine screenshots showing your code and its output.
4. Keep the actual benchmark timings printed by Q4 and Q7. Do not copy invented timing values.
5. The Q6 program prints the actual recursive call counts.
6. Create the GitHub repository with the exact required name and upload these folders.
7. Add the real repository URL to the first page of the assignment.
8. Export the completed assignment document as PDF and submit it to the required portals.

## Complexity summary
- Q1: O(1) for the fixed set of branches; O(n) worst case for n sequential conditions.
- Q2: O(k) time for k attempts; O(1) extra space using loops.
- Q3: O(n) time for an input string of length n; O(n) extra space for the cleaned string.
- Q4: `join` is generally suitable for combining many strings; record actual timings on your computer.
- Q5: Function operations shown are O(1) apart from list growth, which is O(1) amortized per append.
- Q6: Naive recursion is exponential; memoized recursion is O(n) time and O(n) space; iterative is O(n) time and O(1) extra space.
- Q7: List-and-join avoids repeated rebuilding of the growing message; compare actual timings on your computer.
