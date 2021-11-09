'''Programming technique used to solve pattern of 
overlapping subproblems is called dynamic programming'''

from datetime import  date, datetime
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)
n = 20
start = datetime.now()
print(fib(n)) # big issue! 2^n complexity.. so 2^50 times... 
print(f"It took {datetime.now()-start} seconds to calculate {n}th fib number")

'''TO solve the above problem we need to store the results form subtrees
and re-use them. This process is called Memoization.
For this purpose we need some fast access data structure and in our scenario
that would be Python's dictionary.'''

print('Dynamic Programming Approach'.center(100,'-'))

def fib_dyn(n, result={}):
    if n in result:
        return result[n]
    if n <=2:
        return 1
    result[n] = fib_dyn(n-1,result)+fib_dyn(n-2,result)
    return result[n]

start = datetime.now()
n = 8
print(fib_dyn(n))
print(f"It took {datetime.now()-start} seconds to calculate {n}th fib number through DP")


print('GRID TRAVELLER'.center(100,'-'))
print('RECURSIVE APPROACH'.center(100,'.'))

def grid_traveler(m,n):
    """
    m - number of rows.
    n - number of columns
    """
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m-1, n) + grid_traveler(m,n-1)

m = 4
n = 13
start = datetime.now()
print(grid_traveler(m,n))
print(f"It took {datetime.now()-start} seconds to produce the result for {m,n} grid")

print('DYNAMIC PROGRAMMING APPROACH'.center(100,'.'))

def grid_traveler(m,n, memo={}):
    key = f"{m},{n}"
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler(m-1,n, memo) + grid_traveler(m,n-1, memo)
    return memo[key]

start = datetime.now()
print(grid_traveler(m,n))
print(f"It took {datetime.now()-start} seconds to produce the result for {m,n} grid")

print('canSum MEMOIZATION'.center(100,'-'))
print('RECURSIVE APPROACH'.center(100,'.'))
#O(n^m) time complexicity
#O(m) space complexicity
def can_sum(target_sum, num_list):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in num_list:
        remainder = target_sum - num
        if can_sum(remainder, num_list):
            return True
    
    return False

target_sum = 30
num_list = [14,7]
start = datetime.now()
print(can_sum(target_sum, num_list))
print(f"It took {datetime.now() - start} seconds to finish using recursive approach")  #took 3 minutes for 300, [14,7] input.


print('DYNAMIC PROGRAMMING APPROACH'.center(100,'.'))

#O(m*n) complexicity
def can_sum(target_sum, num_list, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in num_list:
        remainder = target_sum - num
        if can_sum(remainder, num_list):
            memo[target_sum] = True
            return True
        
    memo[target_sum] = False
    return False


target_sum = 30
num_list = [14,7]
start = datetime.now()
print(can_sum(target_sum, num_list))
print(f"It took {datetime.now() - start} seconds to finish using recursive approach")  #took 00.000014 seconds for 300, [14,7] input.


print('howSum'.center(100,'-'))

"""
Same as canSum, however this should return an array containing any combination of elements that can add up to target sum.
If there is no combination that can add up to target sum then return null.
If there are multiple combination then return any one.
"""

print('RECURSIVE APPROACH'.center(100,'.'))
#O(n^m * m) - time complexicity
def how_sum(target_sum, num_list):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in num_list:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, num_list)
        if remainder_result != None:
            return remainder_result+[num]   
    return None

# import sys
# sys.setrecursionlimit(2000)
# import resource
# resource.setrlimit(2000)
target_sum = 30
num_list = [14, 7]
start = datetime.now()
print(how_sum(7,[5, 1, 3, 7]))
print(how_sum(target_sum,num_list))
print(f"It took {datetime.now() - start} seconds to produce result for {target_sum, num_list}") #3.3289507 seconds for 300, [7,14]

print('DYNAMIC PROGRAMMING APPROACH'.center(100,'.'))
#O(n*m^2) -time complexicity
#O(m*m)
def how_sum(target_sum, num_list, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    for num in num_list:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, num_list, memo)
        if remainder_result != None:
            memo[target_sum] = remainder_result + [num]
            return memo[target_sum]
        
    memo[target_sum] = None
    return None


target_sum = 300
num_list = [14, 7]
start = datetime.now()
print(how_sum(7,[5, 1, 3, 7]))
print(how_sum(target_sum,num_list))
print(f"It took {datetime.now() - start} seconds to produce result for {target_sum, num_list}") # 0:00:00.000032 seconds for answer.


print('bestSUM'.center(100,'-'))
print('RECURSIVE APPROACH'.center(100,'.'))
#O(n^m*m) - time
#O(m*m)
def best_sum(target_sum, num_list):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None

    for num in num_list:
        remainder = target_sum - num
        combination_remainder = best_sum(remainder, num_list)
        if combination_remainder != None:
            combination = combination_remainder + [num]
            if shortest_combination == None:
                shortest_combination = combination
            elif len(combination) < len(shortest_combination):
                shortest_combination = combination
    
    return shortest_combination

target_sum = 30
num_list = [2, 3, 5]
start = datetime.now()
print(best_sum(target_sum, num_list))
print(f"It took {datetime.now() - start} seconds to produce output for {target_sum, num_list}")

print('DYNAMIC PROGRAMMING'.center(100,'.'))

#O(m^2 * n)
def best_sum(target_sum, num_list, memo = {}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in num_list:
        remainder = target_sum - num
        combination_remainder = best_sum(remainder, num_list, memo)
        if combination_remainder != None:
            combination = combination_remainder + [num]
            if shortest_combination == None:
                shortest_combination = combination
            elif len(combination) < len(shortest_combination):
                shortest_combination = combination
    
    memo[target_sum] = shortest_combination
    return shortest_combination

target_sum = 300
num_list = [2, 3, 25]
start = datetime.now()
print(best_sum(target_sum, num_list))
print(f"It took {datetime.now() - start} seconds to produce output for {target_sum, num_list}")


print('canConstruct'.center(100,'-'))
print('RECURSIVE APPROACH'.center(100,'.'))


def can_construct(target, word_bank):
    if target == '':
        return True
    
    for word in word_bank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if can_construct(suffix, word_bank):
                    return True
        except ValueError:
            pass
        
    return False

start = datetime.now()
print(can_construct('skateboard',['sk','ate','skat','skate','boar']))
print(f"It took {datetime.now() - start} seconds to fulfill this operation")

print('DYNAMIC PROGRAMMING'.center(100, '.'))

def can_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True

    for word in word_bank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if can_construct(suffix, word_bank, memo):
                    memo[target] = True
                    return True
        except ValueError:
            pass
    
    memo[target] = False
    return False

start = datetime.now()
# print(can_construct('skateboard',['sk','ate','skat','skate','boar']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee']))
print(f"It took {datetime.now() - start} seconds to fulfill this operation")


print('countConstruct'.center(100,'-'))
print('RECURSIVE APPROACH'.center(100,'.'))

def count_construct(target, word_bank):
    if target == '':
        return 1
    total = 0
    for word in word_bank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                result = count_construct(suffix, word_bank)
                if result:
                    total += result
        except ValueError:
            pass
    
    return total

start = datetime.now()
print(count_construct('purple',['purp','le','pur','ple','purpl']))
print(f"It took {datetime.now()- start} seconds to finish count construct operation")

print('DYNAMIC PROGRAMMING'.center(100,'.'))

def count_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    
    total = 0
    for word in word_bank:
        try:
            if target.index(word)  == 0:
                suffix = target[len(word):]
                result = count_construct(suffix, word_bank, memo)
                if result:
                    total += result
        except ValueError:
            pass
        
    memo[target] = total
    return memo[target]

start = datetime.now()
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee']))
print(f"It took {datetime.now()- start} seconds to finish count construct operation")

print('allConstruct'.center(100,'-'))
print('RECURSIVE APPROACH'.center(100,'.'))

def all_construct(target, word_bank):
    if target == '':
        return [[]]
    final_result = []
    for word in word_bank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                result_suffix = all_construct(suffix, word_bank)
                target_ways = []
                if type(result_suffix) == list:
                    for val in result_suffix:
                        val.insert(0,word)
                        target_ways.append(val)
                    final_result += target_ways
        except ValueError:
            pass
    return final_result

start = datetime.now()
print(all_construct('purple',['purp','le','pur','ple','purpl']))
print(all_construct('hello',['cat','dog','ox']))
# print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','eee','ee','eeeee','eeee','f']))
print(f"It took {datetime.now()-start} seconds to obtain the result")

print('DYNAMIC PROGRAMMING APPROACH'.center(100,'.'))

def all_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                suffix_ways = all_construct(suffix, word_bank, memo)
                target_ways = []
                if type(suffix_ways) == list:
                    for val in suffix_ways:
                        val.insert(0, word)
                        target_ways.append(val)
                result += target_ways
        except ValueError:
            pass
    memo[target] = result
    return memo[target]

start = datetime.now()
print(all_construct('purple',['purp','le','pur','ple','purpl']))
print(all_construct('hello',['cat','dog','ox']))
# print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','eee','ee','eeeee','eeee','f']))
print(f"It took {datetime.now()-start} seconds to obtain the result")


print('TABULATION'.center(100,'*'))
print('fib by TABULATION'.center(100,'.'))

def fib(n):
    table = [0] * (n+1)
    table[1] = 1
    for index in range(1,n+1):
        try:
            table[index+1] += table[index]
            table[index+2] += table[index]
        except IndexError:
            pass
    return table[n]

start = datetime.now()
print(fib(100))
print(f"it took {datetime.now()- start} seconds to produce fib result througb tabulation")

print('gridTraveller by TABULATION'.center(100,'.'))

def grid_traveler(m,n):
    table = [[0] * (n+1) for i in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j+1 <= n:
                table[i][j+1] += current
            if i+1 <= m:
                table[i+1][j] += current
    return table[m][n]

print(grid_traveler(3,3))

print('canSum by TABULATION'.center(100,'.'))

def can_sum(target_sum, num_list):
    table = [False]* (target_sum+1)
    table[0] = True
    for index in range(target_sum+1):
        if table[index]:
            for num in num_list:
                try:
                    table[index+num] = True
                except:
                    pass
    return table[target_sum]


start = datetime.now()
print(can_sum(7,[5,10,4]))
print(f"It took {datetime.now()-start} seconds to finish this operation.")

print('howSUM by TABULATION'.center(100,'.'))


def how_sum(target, num_list):
    table = [None] * (target+1)
    table[0] = []
    for index in range(target+1):
        if table[index] is not None:
            for num in num_list:
                try:
                    table[index+num] = table[index]+[num]
                except:
                    pass
        
    return table[target]

start = datetime.now()
print(how_sum(7,[3,4,5]))
print(how_sum(300, [7, 14]))
print(f"It took {datetime.now()-start} seconds to finish this operation.")

print('bestSum by TABULATION'.center(100,'.'))

def best_sum(target_sum, num_list):
    table = [None] * (target_sum+1)
    table[0] = []
    for index in range(target_sum+1):
        if table[index] != None:
            for num in num_list:
                combination = table[index] + [num]
                try:
                    if (len(table[index+num]) > len(combination)) or (table[index+num] == None):
                        table[index+num] = combination
                except:
                    if index+num <= target_sum:
                        table[index+num] = combination

    return table[target_sum]

start = datetime.now()
print(best_sum(7,[2,3,5,4,7]))
print(best_sum(300, [7, 14]))
print(best_sum(100,[5,20,25,50]))
print(f"It took {datetime.now()-start} seconds to finish this operation.")
