# https://www.codewars.com/kata/539de388a540db7fec000642/train/python
from datetime import strptime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # Check that coupon is not expired
    if entered_code == correct_code:
        curr_date = strptime(current_date)
        exp_date = strptime(expiration_date)
        if curr_date < exp_date:
            return true
        else:
            return false
