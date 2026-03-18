def xau_con():
    s = str(input())
    n = len(s)
    string = ""
    palidrome_String = s[1]

    def vaild_palindrome(s):
        a = len(s)
        for i in range(a // 2):
            if s[i] == s[a - i - 1]:
                continue
            else:
                return False
        return True

    for i in range(n):
        string += s[i]
        if len(string) > 1:
            if vaild_palindrome(s):
                if len(string) > len(palidrome_String):
                    palidrome_String = string
                    continue
                continue
            else:
                string += s[i]
                continue

    return(palidrome_String)
    
print(xau_con())