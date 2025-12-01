import time

def check_age_consistency(age, birth_year):
    current_seconds = time.time()
    seconds_per_year = 365 * 24 * 60 * 60
    current_year = int(1970 + current_seconds / seconds_per_year)

    expected_age = current_year - birth_year
    return expected_age == age

print(check_age_consistency(19, 2006))