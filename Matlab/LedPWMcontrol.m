x = serial('COM5','BAUD',9600);

fopen(x);
valueResistor = 0;
myErorku = 0;
myLasteror = 0;
myFeedback = 0;
KP = 0.2;
KI = 0.6;
KD = 0.07;
erorIntegral = 0;
erorDifferential = 0;
t = 0:1:30;
pwm = 0;
mydata = zeros(size(t));
myr = zeros(size(t));
inp = 0;
while true
    pause(2);
    flushinput(x);
    fprintf(x,double(pwm));
    valueResistor = str2double(fscanf(x));
    
    myErorku = valueResistor - myFeedback;
    erorIntegral = erorIntegral + myErorku;
    erorDifferential = myErorku - myLasteror;
    myLasteror = myErorku;
    
    myFeedback = (KP * myErorku) + (KI * erorIntegral) + (KD * erorDifferential);
    pwm = myFeedback;
    inp=inp+1;
    if inp > 31
        break;
    end
    mydata(inp) = pwm;
    myr(inp) = valueResistor;
    disp(pwm);
end
    plot(t,myr);
    hold on;
    plot(t,mydata);
    hold off;
    xlim([0 30]);
    ylim([0 255]);







