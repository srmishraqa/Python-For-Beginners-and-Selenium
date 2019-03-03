# person has both high income AND good credit score -- eligible for loan
# otherwise -- not eligible for loan

has_high_income = True
has_good_credit_score = False

if has_high_income and has_good_credit_score:
    print("Customer is eligible for a home loan")
else:
    print("Customer is not eligible for a home loan")

# AND : Both should be true
# OR : At least one of the condition should be true
# NOT : reverse the boolean value

if has_high_income or has_good_credit_score:
    print("Customer is eligible for a home loan")
else:
    print("Customer is not eligible for a home loan")