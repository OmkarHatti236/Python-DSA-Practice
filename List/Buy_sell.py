'''You are given an array prices where prices[i] is the price of a 
given stock on the ith day.You want to maximize your profit by choosing a
 single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return'''


def max(prices,size):
    if(size==0):
        return 0
    minstock=prices[0]
    maxprofit=0
    for i in range(1,size):
        if minstock>prices[i]:
            minstock=prices[i]
        else:
            if maxprofit<prices[i]-minstock:
                maxprofit=prices[i]-minstock
    return maxprofit

prices=[5,4,3,2,1]
x=max(prices,len(prices))
if x:
    print(" Maximum profit got: ",x)
else:
    print("you Lost you money")