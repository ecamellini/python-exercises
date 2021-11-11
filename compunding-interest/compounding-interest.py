"""
Compounding interest calculator.
"""

yearly_deposit = float(input("Yearly deposit: "))
yearly_interest = float(input("Average yearly interest: "))
yearly_multiplier = (100.0 + yearly_interest) / 100.0
years = int(input("Years: "))

total = 0

for i in range(1, years + 1):
    total = (total + yearly_deposit) * yearly_multiplier
    print(f"Year {i}: {total} ")


print(f"\n\nFinal amount: {total}")
print(f"Capital gain (pre-taxes): {total - yearly_deposit * years}")
