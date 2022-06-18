import re


def reverseOnlyLetters(S):
    # s = re.sub('[^a-zA-Z]', '', S)[::-1]
    # r = ""
    # j = 0
    # for i in range(len(S)):
    #     if re.match('[^a-zA-Z]', S[i]):
    #         r += S[i]
    #     else:
    #         r += s[j]
    #         j += 1
    # return r
    s = list(S)
    i , j = 0 , len(s)-1
    while i <=j:
        if not s[i].isalpha():
            i +=1
            continue
        if not s[j].isalpha():
            j-=1
            continue
        s[i], s[j] = s[j], s[i]
        i +=1
        j -=1
    return "".join(s)


if __name__ == '__main__':
    print(reverseOnlyLetters("a-bC-dEf-ghIj"))
