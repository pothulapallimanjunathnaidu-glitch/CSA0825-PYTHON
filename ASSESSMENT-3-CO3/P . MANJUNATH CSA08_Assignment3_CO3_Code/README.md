# CSA08 – Python Programming Assignment 3 (CO3)

## Student details
- Student Name: Enter your name
- Register Number: Enter your register number
- Department / Branch: Enter your department
- Class / Section: Enter your class and section
- Python Version: Python 3.10 or later

## Required GitHub repository name
`CSA08-<RegisterNumber>-Assignment3`

## Requirements
- Python 3.10 or later.
- No third-party Python packages are required. All programs use the Python standard library.

## Folder structure
- `Q1_Lists_Slicing/` – rainfall lists, slicing, moving averages and timing.
- `Q2_Tuples_Mutability_Copying/` – tuples, grid aliasing, shallow/deep copies and memory tests.
- `Q3_Dictionaries_Complaints/` – word frequencies, grouping, top-k words and performance comparison.
- `Q4_Sets_Elective_Clash/` – union, intersection, difference, symmetric difference and membership tests.
- `Q5_List_Comprehension_Sensors/` – cleaning readings with loops, comprehensions, map and filter.
- `Q6_Nested_Railway_Timetable/` – nested timetable, station search, sorting and station index.
- `Q7_Contact_Merging/` – contact normalization, dictionary-based merging and timing.

## Run
Open a terminal in a question folder and run:
`python q1_rainfall.py`

Use the corresponding `.py` filename in each other folder. For example:
`python q2_tuples_copying.py`

## Important submission notes
1. Replace the student-detail placeholders in this README.
2. Run every program on your own computer and check the output.
3. Capture genuine screenshots showing your code and output.
4. Benchmark timings and memory sizes depend on your computer. Use the values printed by your own run; do not copy sample timings.
5. Create the GitHub repository with the exact required name and upload all question folders.
6. Commit progressively, with at least one commit for each task.
7. Add your real GitHub repository URL to the assignment document.

## Complexity summary
- Q1: Weekly totals and moving averages are O(n); running-sum moving average is O(n), while a direct 7-value sum per window is O(7n).
- Q2: Tuple/list indexing is O(1); copying a nested structure takes O(n) time, and deep copying also traverses nested objects.
- Q3: Dictionary word counting is O(n) average over the total number of words; list.count repeated for distinct words is O(n*d).
- Q4: Set membership and set operations are O(1) average per membership and O(n) for operations over n elements.
- Q5: Cleaning and conversion are O(n); a list comprehension uses O(n) result memory, while a generator is lazy.
- Q6: A full timetable scan is O(total stops); a station index reduces query work to the trains listed for that station.
- Q7: Dictionary-based contact merging is O(n) average for n contacts; comparing every pair is O(n^2).

## Assignment coverage note
The scripts demonstrate the main implementation tasks and runnable experiments. The written pseudocode, memory diagrams, explanations, design decisions, and full analysis requested in the PDF should also be included in your written report. Benchmark values must be measured on your own device.
