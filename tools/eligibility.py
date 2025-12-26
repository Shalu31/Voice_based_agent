import json

def check_eligibility(memory):
    with open("data/schemes.json", "r", encoding="utf-8") as f:
        schemes = json.load(f)

    eligible = []

    age = memory.get("age")
    income = memory.get("income")

    for scheme in schemes:
        if age >= scheme["min_age"] and income <= scheme["max_income"]:
            eligible.append(scheme["name"])

    return eligible

