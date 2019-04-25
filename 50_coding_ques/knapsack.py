'''

2. 0-1 Knapsack
Question: 
    Given a list of items with values and weights, as well as a max weight,
    find the maximum value you can generate from items where the sum of the
    weights is less than the maxWeight.

Eg.
    items = {(w:1, v:6), (w:2, v:10), (w:3, v:12)}
    maxWeight = 5
    knapsack(items, maxWeight) = 22
    
    value = [60, 100, 120]
    weight = [10,20,30]
    W = 50
    solution = 220
'''

'''
Approach :
    1. recursive, check all combinations
    2. tree like structure, where values and weight decrease as we go down
    3. Base cases 
        - when weight is more than max weight
        - n==0 or maxW == 0
    4. We need a max function somewhere as we are looking for a max value

Explanation:
    We divide it into subproblems and then take the max of it
    first one is recursive call without the weight[n-1]
    second one is recursive call with n-1
    we return the max of it
    Think in terms of n-1, and weight[n-1]

'''

maxW = 5
# n is len(value)
def knapsack(weight, value, maxWeight, n):
    if n==0 or maxWeight==0:
        return 0
    
    if weight[n-1]> maxWeight:
        return knapsack(weight, value, maxWeight, n-1)
    
    else:
        a = knapsack(weight, value, maxWeight-weight[n-1], n-1)
        print('a: ',a, 'weight: ',weight, 'max: ', maxWeight-weight[n-1], 'n: ', n)
        b = knapsack(weight, value, maxWeight, n-1)
        print('b: ', b)
        c = max(value[n-1] + a, b)
        print('c: ',c)
        return c

value = [60, 100, 120]
weight = [10,20,30]
maxW = 50
solution = 220
print(knapsack(weight, value, maxW, len(value)))


'''
** we are calling function inside the max function
** one time with n-1 and the other time with the reduced weight
'''