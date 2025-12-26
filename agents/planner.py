def planner(memory):
    if not memory.has("age"):
        return {"action": "ask_age"}

    if not memory.has("income"):
        return {"action": "ask_income"}

    return {"action": "check_eligibility"}
