seg=int(input())
h=int
m=int
s=int

h = seg//60**2
seg = seg-h*60**2

m = seg//60
seg=seg - m*60

s = seg%60
print('{}:{}:{}'.format(h,m,s))