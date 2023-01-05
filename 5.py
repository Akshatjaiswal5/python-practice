import cmath
a=int(input('Enter A:'))
b=int(input('Enter B:'))
c=int(input('Enter C:'))
d=(b**2)-4*a*c
sol1=(-b-cmath.sqrt(d))/2*a;
sol2=(-b+cmath.sqrt(d))/2*a;
print('Solutions are {0} and {1}'.format(sol1,sol2))
