import random
import re
import time

def normalize_number(number):
    digits = re.sub(r"\D", "", number or "")
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]
    if len(digits) == 11 and digits.startswith("0"):
        digits = digits[1:]
    return digits

def normalize_name(name):
    return " ".join((name or "").lower().split())

def merge_contacts(contact_lists):
    merged = {}
    for contacts in contact_lists:
        for contact in contacts:
            number = normalize_number(contact.get("phone", ""))
            email = (contact.get("email") or "").strip().lower()
            name = " ".join((contact.get("name") or "Unknown").split())
            if not number and not email:
                continue
            key = number if number else email
            if key not in merged:
                merged[key] = {"name": name, "numbers": set(), "emails": set()}
            if number:
                merged[key]["numbers"].add(number)
            if email:
                merged[key]["emails"].add(email)
            if merged[key]["name"] == "Unknown" and name != "Unknown":
                merged[key]["name"] = name
    return list(merged.values())

phone_a = [
    {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "ravi@example.com"},
    {"name": "Anu", "phone": "9876543210", "email": "anu@example.com"}
]
phone_b = [
    {"name": "ravi kumar", "phone": "9840012345", "email": "RAVI@example.com"},
    {"name": "Kiran", "phone": "", "email": "kiran@example.com"},
    {"name": "Anu", "phone": "98765-43210", "email": ""}
]
sim = [
    {"name": "Ravi", "phone": "09840012345", "email": "ravi.work@example.com"},
    {"name": "", "phone": "", "email": ""}
]

result = merge_contacts([phone_a, phone_b, sim])
for contact in result:
    print({"name": contact["name"], "numbers": sorted(contact["numbers"]), "emails": sorted(contact["emails"])})

print("Same name, different number:", merge_contacts([[{"name": "Ravi", "phone": "9000000001"}, {"name": "Ravi", "phone": "9000000002"}]]))

for n in (1000, 100000):
    data = [[{"name": f"Person{i}", "phone": f"+91 {9000000000 + i}", "email": f"p{i}@example.com"} for i in range(n)]]
    start = time.perf_counter()
    merged = merge_contacts(data)
    dictionary_time = time.perf_counter() - start
    print(f"{n} contacts: dictionary merge={dictionary_time:.6f}s, output contacts={len(merged)}")
