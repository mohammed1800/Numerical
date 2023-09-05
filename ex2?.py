import pulp as p
Lp_prob = p.LpProblem('Problem',p.LpMaximize)
x1=p.LVariable("x1",lowBound=0)
x2=p.LVariable("x2",lowBound=0)
x3=p.LVariable("x3",lowBound=0)
x4=p.LVariable("x4",lowBound=0)
Lp_prob +=20*x1+12*x2+40*x3+25*x4
Lp_prob +=x1+x2+x3+x4<=50
Lp_prob +=3*x1+2*x2+x3<=100
Lp_prob +=x2+2*x3+x4
Lp_prob +=x1<=0
Lp_prob +=x2<=0
Lp_prob +=x3<=0
Lp_prob +=x4<=0
print(Lp_prob)
status=Lp_prob.solve()
print(p.LpStatus[status])
print(p.value(x1),p.value(x2),p.value(x3),p.value(x4),p.value(Lp_prob.objective))
