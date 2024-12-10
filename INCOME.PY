def calculate_income_tax(income):
  """Calculates income tax based on the given rules."""

  if income <= 250000:
    tax = 0
  elif income <= 500000:
    tax = (income - 250000) * 0.05
  elif income <= 1000000:
    tax = (income - 500000) * 0.2 + 12500
  else:
    tax = (income - 1000000) * 0.3 + 112500

  return tax
income =int(input("Enter your income:: "))
tax = calculate_income_tax(income)
print("Income:", income)
print("Tax:", tax)
