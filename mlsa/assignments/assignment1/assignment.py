import pandas as pd
import numpy as np

us_companies_df = pd.read_csv('./us_companies.csv')
us_taxes_df = pd.read_csv('./us_state_taxes.csv')

# 1. Sort states by number of companies
us_companies_by_state = us_companies_df['State'].value_counts().sort_values(ascending=False)
# print(us_companies_by_state)

# 2. Compute the average earning of all the companies
us_average_earnings = us_companies_df.Earnings_last_year.mean()
print(f"Average earnings in the us: {us_average_earnings}")

# 3. Compute the average earnings of companies in california
california_average_earnings = us_companies_df[us_companies_df.State == 'California'].Earnings_last_year.mean()
print(f"Average earnings in californa: {california_average_earnings}")

# 4. Compute the average earnings in the companies in California and Texas
california_texas_average_earnings = us_companies_df[us_companies_df
                                        .State.isin(['California', 'Texas'])].Earnings_last_year.mean()
print(f"Average earnings in california and texas: {california_texas_average_earnings}")

# 5.1 Create a new dataframe with taxes computed for each company
us_companies_taxes = us_companies_df.merge(us_taxes_df, on='State')
print(f"New dataframe with taxes computed for each company:\n{us_companies_taxes}")

# 5.2 Calculate how many taxes each company should pay
us_companies_taxes['Tax_amount'] = (us_companies_taxes.Earnings_last_year * us_companies_taxes.Tax_percentage)/100
print(f"New dataframe with taxes computed for each company:\n{us_companies_taxes}")

#5.3 Save the new dataframe to a csv file
us_companies_taxes.to_csv('us_companies_taxes.csv', index=False)
