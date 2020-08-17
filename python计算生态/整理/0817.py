"""
理解题题 写出下列程序的运行结果
2020.8.17
"""

# def func(s,i,j):
#     if i<j:
#         func(s,i+1,j-1)
#         s[i],s[j] = s[j],s[i]
#
# def main():
#     a = [10,6,23,-90,0,3]
#     func(a,0,len(a)-1)
#     for i in range(6):
#         print(a[i])
#
# main()

"""
3
0
-90
23
6
10
"""



# i = 1
# while (i+1) :
#     if i>4:
#         print("%d"%i)
#         i+=1
#         break
#     print("%d"%i)
#     i += 1
#     i += 1

"""
1
3
5
"""

# def foo(s):
#     if s == "":
#         return s
#     else:
#         return foo(s[1:])+s[0]
#
# print(foo("Happy New Year"))
"""
raeY weN yppaH
"""
#
# def func(a,n,m):
#     if n == 0:
#         return 1
#     else:
#         num = func(a,n/2,m)
#
#     if n%2 == 0 :
#         return num * num % m
#     else:
#         return num * num * a % m
#
# print(func(5,6,7))
"""
1
"""

# def foo(list,num):
#     if num == 1:
#         list.append(0)
#     elif num ==2:
#         foo(list,1)
#         list.append(1)
#     elif num>2:
#         foo(list,num-1)
#         list.append(list[-1]+list[-2])
#
# mylist = []
# foo(mylist,10)
# print(mylist)
"""
[0,1,1,2,3,5,8,13,21,34]
"""

def func(a,b):
    if(a<b):
        a,b = b,a
    r = a%b
    if r==0:
        return b
    else:
        return func(b,r)

ans = func(342,84)
print(ans)
"""
6
"""





