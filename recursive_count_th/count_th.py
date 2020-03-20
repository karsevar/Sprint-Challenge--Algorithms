'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # base case:
    # if string length is less than or equal to 1 return 0 
    # if string length is 2 and string == 'th' return 1 
    # else return 0 

    # calculate the mid point in the string 
    # recursively call the count_th function on both sides of the string
    

    if len(word) <= 1:
        return 0 
    if len(word) == 2:
        if word == 'th':
            return 1
        else:
            return 0
    else:
        mid = len(word) // 2
        return count_th(word[:mid+1]) + count_th(word[mid:])