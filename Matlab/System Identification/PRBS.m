clear;
TimeCountMax = 2000;
SamplingTime = 0.01;
RandMinTime = 0.5;
RandMaxTime = 2;
RandStatus = 0;
Time(1) = 0;
Signal(1) = 0;
for i=2:TimeCountMax+1,
    Time(i) = SamplingTime * (i-1);
    Signal(i)=Signal(i-1);
    if RandStatus == 0
        ControlTime = RandMinTime+(RandMaxTime-RandMinTime)*rand;
        StartTime = Time(i);
        RandStatus = 1;
        if Signal(i) >= 1
            Signal(i) = 1-Signal(i-1);
        
        else Signal(1) <= 0
            Signal(i) = 1+Signal(i-1);
        end
    end
    if (Time(i)-StartTime)>ControlTime
        RandStatus = 0;
    end
end
SinyalGenerator=[Time' Signal'];
plot(Time,Signal);