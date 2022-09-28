u = IdentData.signals(1,1).values;
y = IdentData.signals(1,2).values;
Ts = 0.01;
Motor = iddata(y,u,Ts);
% show input - output data
plot(Motor);
% do system identification
ze = detrend(Motor);
m1 = pem(ze);

% create model
MtrMdlDg = ss(m1.a,m1.b,m1.c,m1.d,Ts);  
MtrMdlAn = d2c(MtrMdlDg);

% show tranfer function
[numd,denumd] = ss2tf(MtrMdlDg.a,MtrMdlDg.b,MtrMdlDg.c,MtrMdlDg.d)
[numa,denuma] = ss2tf(MtrMdlAn.a,MtrMdlAn.b,MtrMdlAn.c,MtrMdlAn.d)

%compare(Motor,dcTf1,dcTf2)
