s=tf('s');
PID=(29.24)+(15.51/s)-(840.334/(s+35))
syms Kp Kd Ki N
NPID_num=[Kp+N*Kd Kp*N+Ki N*Ki];
NPID_den=[1 N 0];
eqn1=PID.Numerator{1}(1)==NPID_num(1);
eqn2=PID.Numerator{1}(2)==NPID_num(2);
eqn3=PID.Numerator{1}(3)==NPID_num(3);
eqn4=PID.Denominator{1}(2)==NPID_den(2);
solx=vpasolve([eqn1 eqn2 eqn3 eqn4]);
Kp=subs(Kp,solx.Kp)
Kd=subs(Kd,solx.Kd)
Ki=subs(Ki,solx.Ki)
N=subs(N,solx.N)