import pandas as pd
import numpy as np

def create_amortization_table(loan_amount=110000000, annual_rate=0.09, years=20, monthly_payment=1000000):
    # Setup initial values
    monthly_rate = annual_rate / 12
    periods = years * 12
    
    # Create empty lists to store values
    remaining_balance = []
    interest_paid = []
    principal_paid = []
    total_paid = []
    
    balance = loan_amount
    
    # Calculate amortization schedule
    for month in range(1, periods + 1):
        # Calculate interest for this month
        interest = balance * monthly_rate
        
        # Calculate principal for this month
        principal = monthly_payment - interest
        
        # Update balance
        balance = balance - principal
        
        # Store values
        remaining_balance.append(round(balance))
        interest_paid.append(round(interest))
        principal_paid.append(round(principal))
        total_paid.append(round(monthly_payment))
    
    # Create DataFrame
    df = pd.DataFrame({
        'Bulan': range(1, periods + 1),
        'Cicilan': total_paid,
        'Pokok': principal_paid,
        'Bunga': interest_paid,
        'Sisa Pinjaman': remaining_balance
    })
    
    # Only show some representative months
    months_to_show = [1, 2, 3, 12, 24, 36, 60, 120, 180, 240]
    df_summary = df[df['Bulan'].isin(months_to_show)]
    
    return df_summary

# Create and format the table
df = create_amortization_table()

# Format the table for display
def format_currency(x):
    return f"Rp {x:,.0f}"

print("\nTabel Amortisasi KPR:")
print(f"Pinjaman Awal: Rp 110,000,000")
print(f"Bunga: 9% per tahun")
print(f"Tenor: 20 tahun")
print(f"Cicilan per bulan: Rp 1,000,000\n")

formatted_df = df.copy()
for col in ['Cicilan', 'Pokok', 'Bunga', 'Sisa Pinjaman']:
    formatted_df[col] = formatted_df[col].apply(format_currency)

print(formatted_df.to_string(index=False))

# Calculate total interest paid
total_interest = df['Bunga'].sum()
print(f"\nTotal bunga yang dibayar selama 20 tahun: {format_currency(total_interest)}")