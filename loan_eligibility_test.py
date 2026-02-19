#!/usr/bin/env python3
# /Users/ramcharan/Documents/AI_LAB/loan_eligibility_test.py
# Simple console app to evaluate basic loan eligibility

def evaluate_eligibility(age, monthly_income, employment_type, existing_loan_amount, requested_loan_type, requested_loan_amount):
    reasons = []
    eligible = True

    # Age check
    if age < 21:
        eligible = False
        reasons.append("Applicant is too young (minimum 21).")
    if age > 65:
        eligible = False
        reasons.append("Applicant is over the maximum eligible age (65).")

    # Employment normalization
    emp = employment_type.strip().lower()
    if emp not in ("salaried", "self-employed", "self employed", "self"):
        eligible = False
        reasons.append("Employment type must be 'salaried' or 'self-employed'.")

    # Minimum income by loan type & employment
    min_income = 0
    if requested_loan_type == "home":
        min_income = 3000 if emp == "salaried" else 5000
        income_multiplier = 300   # approximate max loan = monthly_income * multiplier
    elif requested_loan_type == "car":
        min_income = 2000 if emp == "salaried" else 3000
        income_multiplier = 60
    elif requested_loan_type == "personal":
        min_income = 1500 if emp == "salaried" else 2500
        income_multiplier = 24
    else:
        eligible = False
        reasons.append("Unknown loan type requested.")

    if monthly_income < min_income:
        eligible = False
        reasons.append(f"Monthly income below minimum for {requested_loan_type} loan (min {min_income}).")

    # Debt-to-income (DTI) check (use existing loan amount as proxy)
    # Compute DTI as existing_loan_amount / (monthly_income * 12)
    try:
        dti = existing_loan_amount / (monthly_income * 12)
    except ZeroDivisionError:
        dti = 1.0
    if dti > 0.4:
        eligible = False
        reasons.append(f"High debt-to-income ratio (existing loans ≈ {dti:.2%} of annual income).")

    # Requested loan amount vs permitted by income
    if 'income_multiplier' in locals():
        max_allowed = monthly_income * income_multiplier
        if requested_loan_amount > max_allowed:
            eligible = False
            reasons.append(f"Requested loan amount {requested_loan_amount:.0f} exceeds allowed maximum based on income ({max_allowed:.0f}).")

    return eligible, reasons

def prompt_float(prompt_text):
    while True:
        val = input(prompt_text).strip()
        try:
            return float(val)
        except ValueError:
            print("Please enter a valid number.")

def prompt_int(prompt_text):
    while True:
        val = input(prompt_text).strip()
        try:
            return int(val)
        except ValueError:
            print("Please enter a valid integer.")

def prompt_choice(prompt_text, choices):
    choices_str = "/".join(choices)
    while True:
        val = input(f"{prompt_text} ({choices_str}): ").strip().lower()
        if val in choices:
            return val
        # accept small variants
        if val.replace("-", " ") in choices:
            return val.replace("-", " ")
        print(f"Please choose one of: {choices_str}.")

def main():
    print("Loan Eligibility Checker")
    name = input("Customer name: ").strip()
    age = prompt_int("Age: ")
    monthly_income = prompt_float("Monthly income (numeric): ")
    employment_type = prompt_choice("Employment type", ["salaried", "self-employed"])
    existing_loan_amount = prompt_float("Existing total loan amount (numeric, 0 if none): ")
    loan_type = prompt_choice("Loan type requested", ["home", "car", "personal"])
    requested_loan_amount = prompt_float("Requested loan amount: ")

    eligible, reasons = evaluate_eligibility(
        age,
        monthly_income,
        employment_type,
        existing_loan_amount,
        loan_type,
        requested_loan_amount
    )

    print("\n--- Decision ---")
    print(f"Customer: {name}")
    if eligible:
        print("Result: Eligible for the requested loan.")
    else:
        print("Result: Not eligible for the requested loan.")
        print("Reasons:")
        for r in reasons:
            print(f" - {r}")

if __name__ == "__main__":
    main()