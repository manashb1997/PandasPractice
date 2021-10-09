import math as m

print('Program to evaluate the roots of an equation of form ax^2+bx+c=0')


a = float(input('Enter value of a: '))
b = float(input('Enter value of b: '))
c = float(input('Enter value of c: '))
uroot = m.sqrt((b*b) - (4*a*c))

root1 = (-b + uroot )/(2*a)
root2 = (-b - uroot )/(2*a)

print('The roots are {} or {}.'.format(round(root1,3), round(root2,3)))

