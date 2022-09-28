graphJarak = [];
graphSuhu = [];
graphOutPWM = [];

jarakDekat = float('single');
jarakSedang = float('single');
jarakJauh = float('single');

suhuDingin = float('single');
suhuHangat = float('single');
suhuPanas = float('single');

pwmLambat = 1000;
pwmSedang = 2000;
pwmCepat = 4000;
t = 1;
T = 100;

s = serial('COM9','BaudRate', 9600);
fclose(s);
fclose(instrfind);

fopen(s);

while true
    jarak = fread(s, 1, 'float');
    suhu = fread(s, 1, 'float');

    graphJarak(t) = jarak;
    if jarak <= 17
        jarakDekat = 1; 
        jarakSedang = 0;
        jarakJauh = 0;
    elseif jarak > 17 && jarak <= 51 
        jarakDekat = (51 - jarak) / (51 - 17); 
        jarakSedang = (jarak - 17) / (51 - 17);
        jarakJauh = 0;
    elseif jarak > 51 && jarak <= 87
        jarakDekat = 0;    
        jarakSedang = (87 - jarak) / (87 - 51); 
        jarakJauh = (jarak - 51) / (87 - 51);
    elseif jarak > 87
        jarakDekat = 0;
        jarakSedang = 0;
        jarakJauh = 1;
    end
    
    graphSuhu(t) = suhu;
    
    if suhu <= 15.1
        suhuDingin = 1; 
        suhuHangat = 0;
        suhuPanas = 0;
    elseif suhu > 15.1 && suhu <= 25.3 
        suhuDingin = (25.3 - suhu) / (25.3 - 15.1); 
        suhuHangat = (suhu - 15.1) / (25.3 - 15.1);
        suhuPanas = 0;
    elseif suhu > 25.3 && suhu <= 35.5
        suhuDingin = 0;    
        suhuHangat = (35.5 - suhu) / (35.5 - 25.3); 
        suhuPanas = (suhu - 25.3) / (35.5 - 25.3);
    elseif suhu > 35.5
        suhuDingin = 0;
        suhuHangat = 0;
        suhuPanas = 1;
    end
    
    rule00 = min([suhuDingin jarakDekat]);
    rule01 = min([suhuDingin jarakSedang]);
    rule02 = min([suhuDingin jarakJauh]);
    
    rule10 = min([suhuHangat jarakDekat]);
    rule11 = min([suhuHangat jarakSedang]);
    rule12 = min([suhuHangat jarakJauh]);
    
    rule20 = min([suhuPanas jarakDekat]);
    rule21 = min([suhuPanas jarakSedang]);
    rule22 = min([suhuPanas jarakJauh]);
    
    PWM0 = (rule00 * pwmLambat) + (rule01 * pwmLambat) + (rule02 * pwmLambat);
    PWM1 = (rule10 * pwmLambat) + (rule11 * pwmSedang) + (rule12 * pwmCepat);
    PWM2 = (rule20 * pwmCepat) + (rule21  * pwmCepat) + (rule22 * pwmCepat);
    PWMTotal = PWM0 + PWM1 + PWM2;
    
    DEF0 = rule00 + rule01 + rule02;
    DEF1 = rule10 + rule11 + rule12;
    DEF2 = rule20 + rule21 + rule22;
    DEFTotal = DEF0 + DEF1 + DEF2;
    
    OutPWM = PWMTotal / DEFTotal;
    graphOutPWM(t) = OutPWM;
    
    t=t+1;
    
    subplot(3,1,1)
    plot(graphJarak), xlabel('Iterasi'), ylabel('jarak (m)'), title('Data jarak')
    axis([T*fix(t/T),T+T*fix(t/T),0,100]);
    subplot(3,1,2)
    plot(graphSuhu), xlabel('Iterasi'), ylabel('suhu (C)'), title('Data suhu')
    axis([T*fix(t/T),T+T*fix(t/T),0,40]);
    subplot(3,1,3)
    plot(graphOutPWM), xlabel('Iterasi'), ylabel('Nilai'), title('Out PWM')
    axis([T*fix(t/T),T+T*fix(t/T),0,4096]);
    grid;
    drawnow
    fwrite(s, OutPWM, 'uint16');
end