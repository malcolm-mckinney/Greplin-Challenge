#Greplin Challenge

import math
from itertools import combinations

#Finds the longest palindrome
def longest_palindrome(seq):
    s = seq.lower()
    palin = ""
    j = 1
    bool = True
    cont = False
    for i in range(len(s) - 1):
        if i == 0:
            continue
        while bool:
            if ord(s[i - j]) == ord(s[i + j]):
                j = j + 1
                cont = True
            else:
                if len(palin) < len(s[i-j + 1:i+j]) and cont:
                    palin = s[(i-j)+ 1 :(i+j)]
                bool = False
                cont = False
        bool = True
        j = 1
    print palin

#Finds the nth fib number using dynamic programming
def f(num):
    arr = [0, 1]
    fib(num, arr)
    return arr[num]

#A helper function for fib series
def fib(n, arr):
    if (len(arr) > n):
        return arr[n]
    arr.insert(n, fib(n-1, arr) + fib(n-2, arr))
    return arr[n]

#Returns true if the number is prime
def isPrime(num):
    for i in xrange(2, (num - 1)/2):
        if num % i == 0:
            return False
    return True

#Returns the number of subsets in the list
def num_subsets(lst):
    count = 0
    for i in range(len(lst)):
        temp = lst[0:i+1]
        for j in range(2,len(temp)):
            combos = combinations(temp,j)
            for c in combos:
                if sum(c) == temp[i]:
                    count = count + 1
    print count


def sum_of_primes(number):
    num = 1
    #starts fibonacci on a sufficiently large value of i
    i = 28
    
    while not isPrime(num) or number > num:
        num = f(i+1)
    num = num + 1
    n = 0
    for i in xrange(2, num):
        if num % i == 0:
            if isPrime(i):
                n = n + i
    print n


if __name__ == '__main__':

    longest_palindrome("Fourscoreandsevenyearsagoour" + "faathersbroughtforthonthiscontainentanewnat" + "ionconceivedinzLibertyanddedicatedtotheprop" + "ositionthatallmenarecreatedequalNowweareeng" + "agedinagreahtcivilwartestingwhetherthatnapt" + "ionoranynartionsoconceivedandsodedicatedcan" + "longendureWeareqmetonagreatbattlefiemldoftz" + "hatwarWehavecometodedicpateaportionofthatfi" + "eldasafinalrestingplaceforthosewhoheregavet" + "heirlivesthatthatnationmightliveItisaltoget" + "herfangandproperthatweshoulddothisButinalar" + "gersensewecannotdedicatewecannotconsecratew" + "ecannothallowthisgroundThebravelmenlivingan" + "ddeadwhostruggledherehaveconsecrateditfarab" + "oveourpoorponwertoaddordetractTgheworldadsw" + "filllittlenotlenorlongrememberwhatwesayhere" + "butitcanneverforgetwhattheydidhereItisforus" + "thelivingrathertobededicatedheretotheulnfin" + "ishedworkwhichtheywhofoughtherehavethusfars" + "onoblyadvancedItisratherforustobeherededica" + "tedtothegreattdafskremainingbeforeusthatfro" + "mthesehonoreddeadwetakeincreaseddevotiontot" + "hatcauseforwhichtheygavethelastpfullmeasure" + "ofdevotionthatweherehighlyresolvethatthesed" + "eadshallnothavediedinvainthatthisnationunsd" + "erGodshallhaveanewbirthoffreedomandthatgove" + "rnmentofthepeoplebythepeopleforthepeoplesha" + "llnotperishfromtheearth")
    
    sum_of_primes(277000)
    num_subsets([3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99])

    
    
    
        
    