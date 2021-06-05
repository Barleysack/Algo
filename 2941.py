s = input().lower()
k = len(s)
A= s.count("c=")
B=s.count("c-")
if "dz=" in s:
  C = s.count("dz=")
else:
  C=0
if "z=" in s:
  D=s.count("z=")-C
else:
  D=0
D=s.count("d-")
E = s.count("lj")
F = s.count("nj")
G=s.count("s=")
wtf = A+B+(2*C)+D+E+F+G
result = k -wtf
print(result)