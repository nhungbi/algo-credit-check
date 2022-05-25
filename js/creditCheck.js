exports.creditCheck = function(strIntegers) {
    const arrayStrInt = strIntegers.split('')
    const accountIdentifier = arrayStrInt.map(function (elt) { return Number(elt)} ) // convert str of integers to Number
    //2x every othher digits
    for (let i = 0; i < accountIdentifier.length; i+=2) {
        accountIdentifier[i] *= 2
    }

    //summed digits over 10
    for (let x=0; x< accountIdentifier.length; x++) {
        digit = String(accountIdentifier[x])
        if (digit.length >= 2) {
            let total = 0
            for (num of digit) {
                total += Number(num)}
            accountIdentifier[x] = total}
         }
    resultsSum = accountIdentifier.reduce((current,next) => current + next, 0)

    if (resultsSum % 10 === 0) {
        return 'The number is valid!'
    }

    return 'The number is invalid!'

}

