a=int(input('Enter A:'))
b=int(input('Enter B:'))
c=int(input('Enter C:'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**.5
print('Area is '+str(area))