x = serial('COM4','BAUD',115200);

fopen(x);
data = 0;
s = 0:1:30;
j = 0:1:300;
t = 0:1:5;
pwmLambat = 100;
pwmSedang = 200;
pwmCepat = 250;
OutPWM = 0;
suhu = zeros(size(s));
jarak = zeros(size(j));
inp = 0;
i = 0;
kunci = '0';
checksum = 0;
suhuHangat = 0;
suhuDingin = 0;
suhuPanas = 0;
jarakDekat = 0;
jarakSedang = 0;
jarakJauh = 0;

while true
    %pause(2);
    %flushinput(x);
    fprintf(x,double(OutPWM));
    data = fscanf(x);
    %data = str2double(data);
    if strcmp(data,'A') || (kunci == 'E')
        kunci = 'A';
    elseif data == 'B' & kunci == 'A'
        kunci = 'B';
    elseif kunci == 'B'
        suhu = str2double(data);
        kunci = 'C';
    elseif kunci == 'C'
        jarak = str2double(data);
        kunci = 'D';
    elseif kunci == 'D'
        checksum = str2double(data);
        kunci  = 'E';
    end
    
    if suhu <= 22.5
        suhuDingin = 1;
    elseif suhu > 22.5 & suhu <=25
        suhuDingin = (25-suhu)/(25-22.5);
    else 
        suhuDingin = 0;
    end
    
    if suhu <= 22.5
        suhuHangat = 0;
    elseif suhu > 22.5 & suhu <=25
        suhuHangat = (suhu-22.5)/(25-22.5);
    elseif suhu > 25 & suhu <=27.5
        suhuHangat = (27.5-suhu)/(27.5-25);
    else 
        suhuHangat = 0;
    end
    
    if suhu <= 25
        suhuPanas = 0;
    elseif suhu > 25 & suhu <=27.5
        suhuPanas = (suhu - 25)/(27.5-25);
    else 
        suhuPanas = 1;
    end
    
    if jarak <= 10
        jarakDekat = 1;
    elseif jarak > 10 & jarak <=20
        jarakDekat = (20-jarak)/(20-10);
    else 
        jarakDekat = 0;
    end
    
    if jarak <= 10
        jarakSedang = 0;
    elseif jarak > 10 & jarak <=20
        jarakSedang = (jarak-10)/(20-10);
    elseif jarak > 20 & jarak <=30
        jarakSedang = (30-jarak)/(30-20);
    else 
        jarakSedang = 0;
    end
    
    if jarak <= 20
        jarakJauh = 0;
    elseif jarak > 20 & jarak <=30
        jarakJauh = (jarak - 20)/(30-20);
    else 
        jarakJauh = 1;
    end
        
    rule00 = (min(suhuDingin,jarakDekat));
    rule01 = (min(suhuDingin,jarakSedang));
    rule02 = (min(suhuDingin,jarakJauh));
    
    rule10 = (min(suhuHangat,jarakDekat));
    rule11 = (min(suhuHangat,jarakSedang));
    rule12 = (min(suhuHangat,jarakJauh));
    
    rule20 = (min(suhuPanas,jarakDekat));
    rule21 = (min(suhuPanas,jarakSedang));
    rule22 = (min(suhuPanas,jarakJauh));
    
    PWM0 = (rule00 * pwmLambat) + (rule01 * pwmLambat) + (rule02 * pwmLambat);
    PWM1 = (rule10 * pwmLambat) + (rule11 * pwmSedang) + (rule12 * pwmCepat);
    PWM2 = (rule20 * pwmCepat) + (rule21 * pwmCepat) + (rule22 * pwmCepat);
    PWMTot = PWM0 + PWM1 + PWM2;
    
    DEF0 = (rule00) + (rule01) + (rule02);
    DEF1 = (rule10) + (rule11) + (rule12);
    DEF2 = (rule20) + (rule21) + (rule22);
    DEFTot = DEF0 + DEF1 + DEF2;
    
    OutPWM = PWMTot / DEFTot;
    
    %mydata(inp) = pwm;
    %myr(inp) = valueResistor;
    %disp(data);
    %disp(kunci);
    disp(OutPWM);
    %disp(jarak);
    %disp(suhu);
end

fclose(x);







