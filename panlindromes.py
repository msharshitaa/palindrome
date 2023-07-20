def palindrome(string,start,end):

    if start>=end:
        return 1
    if string[start]!=string[end]:
        return 0
    return palindrome(string,start+1,end-1)

string=input()
print(palindrome(string,0,len(string)-1))