#Chapter02-1
#파이썬 완전 기초
#Print 사용법

print('Python Start')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print()

# separator 옵션
print('P','Y','T','H','O','N',sep='|')
print('010','1234','1234',sep='-')
print('python','naver.com',sep='@')

# end 옵션
print('Welcome to',end=' ')
print('IT News',end=' ')
print('Web Site')
print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)
print()

#format 사용(d ex)3, s ex)'python , f ex)3.1445454)
print('%s %s' %('one','two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two'))

print(  )
# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s'%('nice'))
print('%.5s'%('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f

print('%1.8f' % (3.1414242412))
print('{:f}'.format(3.14124214))
print('%06.2f' % (3.141414142142145235))
print('{:06.2f}' .format(3.141414142142145235))