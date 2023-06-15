def calculate_fire():
    # Get user input
    gross_annual_income = float(input("Enter your gross annual income: "))
    monthly_savings = float(input("Enter your total monthly savings (including 401k, IRA, savings accounts, etc.): "))
    monthly_net_income = float(input("Enter your monthly net income: "))
    total_invested_assets = float(input("Enter your total invested assets: "))
    cash_holdings = float(input("Enter your total cash holdings: "))
    stock_percentage = float(input("Enter the percentage of your portfolio in stocks (as a number between 0 and 100): "))
    bond_percentage = float(input("Enter the percentage of your portfolio in bonds (as a number between 0 and 100): "))
    stock_growth_rate = float(input("Enter your expected average growth rate for stocks (the historical average is about 7%): "))
    bond_growth_rate = float(input("Enter your expected average growth rate for bonds (the historical average is about 3%): "))
    cash_growth_rate = float(input("Enter your expected average growth rate for cash (the historical average is about 1%): "))
    safe_withdrawal_rate = float(input("Enter your safe withdrawal rate (as a number between 0 and 100): "))
    desired_annual_spending = float(input("Enter your desired annual spending in retirement: "))

    # Calculate gross monthly income
    gross_monthly_income = gross_annual_income / 12

    # Calculate portfolio growth rate
    portfolio_growth_rate = (stock_percentage * stock_growth_rate + bond_percentage * bond_growth_rate) / 100

    # Calculate income to be lived off if retiring now
    income_if_retired_now = (total_invested_assets * (safe_withdrawal_rate / 100)) + (cash_holdings * (cash_growth_rate / 100))

    # Calculate the monthly savings rate
    savings_rate_gross = (monthly_savings / gross_monthly_income) * 100

    # Calculate the total needed to retire based on the desired annual spending
    total_needed_to_retire = desired_annual_spending / (safe_withdrawal_rate / 100)

    # Calculate the years until this amount is reached, adjusting for cash growth
    years_to_save = (total_needed_to_retire - total_invested_assets - cash_holdings * (1 + cash_growth_rate/100)) / (12 * monthly_savings)
    
    # Now, considering the portfolio growth rate
    years_until_fire = years_to_save / (1 + portfolio_growth_rate/100)

    return savings_rate_gross, income_if_retired_now, years_until_fire

# Run the function and print the results
savings_rate_gross, income_if_retired_now, years_until_fire = calculate_fire()
print(f"Your monthly savings rate based on gross income is {savings_rate_gross:.2f}%")
print(f"If you retired now, you could live off an income of ${income_if_retired_now:.2f} per year.")
print(f"You have approximately {years_until_fire:.1f} years until your FIRE date.")
