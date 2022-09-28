x = serial('COM5','BAUD',2000000);

fopen(x);
valueResistor = 0;
a = 0;
while true
    fprintf(x,a);
    valueResistor = str2double(fscanf(x));
    if (valueResistor <= 500) 
        a = 0;
    else
        a = 1;
    end
    disp(valueResistor);
    disp(a);
end



