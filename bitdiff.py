def diff(c, d):
  c = int(c, 16)
  d = int(d, 16)
  return '{:b}'.format(c ^ d).count('1') 
  
import sys
s = open(sys.argv[1], 'r').read().strip()
t = open(sys.argv[2], 'r').read().strip()
print(s)
print(t)    

diff = sum(diff(c, d) for (c, d) in zip(s, t))
total = len(s) * 4
print('%d/%d' % (diff, total))
