age_str = input("What is your current age?")

# how many days, weeks months left if we
# live until 90 years?
# 365 days, 52 weeks, 12 months in a year

age_days = int(age_str)*365
age_weeks = int(age_str) * 52
age_months = int(age_str) * 12

age_90_days = 90 * 365
age_90_weeks = 90 * 52
age_90_months = 90 * 12

#instructor calculated years_remaining first, then just calculated that 3 times, quicker than my solution
days_left = age_90_days - age_days
weeks_left = age_90_weeks - age_weeks
months_left = age_90_months - age_months

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left until 90!")