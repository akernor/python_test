from python.test_case.hello import test

test.say('5')


class TestException(Exception):
    pass

class Test2Exception(Exception):
    pass

# try:
#     raise Exception
# except:
#     print('Error')

# try:
#     x = 'Hello'
# except:
#     print('Error')
#
# print(x)

# try:
#     pass
# except:
#     print('Error')

# try:
#     raise Test2Exception('hello BUG')
# except (Test2Exception, TestException) as e:
#     print(e)

try:
    print("444")
# except Exception:
#     print('3')
except TestException:
    print('1')
except Test2Exception:
    print('2')
finally:
    print('The end')





