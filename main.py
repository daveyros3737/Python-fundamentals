def calculateFutureValue(monthlyInvestment, monthlyRate, months):
    futureValue = 0.0
    for i in range(months):
        futureValue =(futureValue + monthlyInvestment) * (1 + monthlyRate)
    return futureValue
print (calculateFutureValue(5.0))