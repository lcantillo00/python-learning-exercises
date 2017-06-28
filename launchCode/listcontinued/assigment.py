def sum_of_initial_odds(nums):
    # your code here
    sum=0
    for i in nums:
        if i%2==1:
            sum+=i
        else:
            break
    return sum    
