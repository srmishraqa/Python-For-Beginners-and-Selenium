# Cost of house 1M $
# credit report good -- 10% down payment
# credit report not good -- 20% down payment

has_credit_good = True
house_cost = 1000000

if has_credit_good:
    down_pay = house_cost * 0.10

else:
    down_pay = house_cost * 0.20

print(f"The customer have to give $ {down_pay} as down payment")




