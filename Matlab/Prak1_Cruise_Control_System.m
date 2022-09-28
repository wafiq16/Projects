m = 750;
b = 40;
r = 3;
kp = 800;
ki = 40;
kd = 1;
num = [kd kp ki];
den = [m+kd b+kp ki];
t = 0:0.1:20;
step(r*num, den, t);
axis([0 20 0 5]);
ylabel('Velocity (m/sec)');

