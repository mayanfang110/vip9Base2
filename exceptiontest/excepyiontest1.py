# try:
#     open('test111.txt','r')
# except:
#     open('test111','w')

#不会
# try:
#     print(num)
# except (NameError,ZeroDivisionError):
#     print('0不能做除数')
# try:
#     print(num)
# except:
#     print('0不能做除数')




# try:
#     print(num)
# except Exception as result:
#     print(result)


# try:
#     print(num)
# except :
#     print('哈哈')

try:

    f = open('test.txt', 'r')
except Exception as result:
    print('哈哈')
    f = open('test.txt', 'w')
# else:
#     print('没有异常，真开⼼')
# finally:
#     f.close()
