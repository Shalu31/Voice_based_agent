from tools.eligibility import check_eligibility

def executor(memory):
    age = memory.get("age")
    income = memory.get("income")
    return check_eligibility(age, income)
