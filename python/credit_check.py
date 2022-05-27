def credit_check(str_integers):
    account_identifier = [int(char) for char in str_integers]
    #2x every other digits, starting from right most
    if len(account_identifier) % 2 == 0: #if even
        start = 0
    else:
        start = 1

    for i in (range(start, len(account_identifier), 2)):
        account_identifier[i]*=2 
    
    #summed digits over 10:
    for i in range(len(account_identifier)):
        digit = str(account_identifier[i]) #to check number of digits
        if len(digit) >=2:
            total = 0
            for num in digit:
                total += int(num)
            account_identifier[i] = total

    results_sum = sum(account_identifier)
    if results_sum % 10 == 0:
        return 'The number is valid!'
    
    return 'The number is invalid!'

        


    # Your Luhn Algorithm Here
    # Expected Output:
    # If it is valid, print "The number is valid!"
    # If it is invalid, print "The number is invalid!"

