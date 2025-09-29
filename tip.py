def total_bill(amount, tip_perc):
    total = amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

total_bill(350,15)