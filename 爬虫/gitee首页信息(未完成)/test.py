def a(s=' '):
    a=''
    len_=0
    for i in range(len(s)):
        # print(s[i::])
        for j in s[i::]:
            if(j in a):
                break
            else:
                # print(a[len(a)-1])
                a+=j
        if len(a)>len_:
            len_=len(a)
        a=''
    return len_
print(a() )