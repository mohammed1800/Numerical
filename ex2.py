import pulp as p
Lp_prob =p.LpProblem('Problem',p.LpMaximize)
w=p.LpVariable("w", lowBound =0)
x=p.LpVariable("x", lowBound =0)
y=p.LpVariable("y", lowBound =0)
z=p.LpVariable("z", lowBound =0)
Lp_prob +=20*w+12*x+40*y+25*z
Lp_prob +=w+x+y+z<=50
Lp_prob +=3*w+2*x+y<=100
Lp_prob +=x+2*y<=90
Lp_prob +=w>=0
Lp_prob +=x>=0
Lp_prob +=y>=0
Lp_prob +=z>=0

print(Lp_prob)
status=Lp_prob.solve()
print(p.LpStatus[status])
print(p.value(w),p.value(x),p.value(y),p.value(y),p.value(z),p.value(Lp_prob.objective))
