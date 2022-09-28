function sysCall_init()
    
    motor_kanan = sim.getObjectHandle('Joint1')
    motor_kiri = sim.getObjectHandle('Joint2')
    
    -- input
    Jarak = 0
    Orientasi = 0  
    t = 0
    
    R = 70
    D = 90
    
    V = Jarak/t
    
    wr = (1*V/R) + (D*Orientasi/R)
    wl = (1*V/R) - (D*Orientasi/R)
    

    sim.setJointTargetVelocity(motor_kanan, w1);
    sim.setJointTargetVelocity(motor_kiri, w2);
    
    corout=coroutine.create(coroutineMain)
end

function sysCall_actuation()
    
    if coroutine.status(corout)~='dead' then
        local ok,errorMsg=coroutine.resume(corout)
        if errorMsg then
            error(debug.traceback(corout,errorMsg),2)
        end
    end

    --sim.setJointPosition(motor1, teta1)
    --sim.setJointPosition(motor2, teta2)
    --sim.setJointPosition(motor3, teta3)

    --sim.setJointTargetPosition(motor1, teta1)
    --sim.setJointTargetPosition(motor2, teta2)
    --sim.setJointTargetPosition(motor3, teta3)

    --print(qx,qy)
end

function sysCall_cleanup()
    -- do some clean-up here
end

function coroutineMain()
    -- Put some initialization code here

    
    -- Put your main loop here, e.g.:
    --
    
    i = 0
    while (i<4) do
        --sim.setJointPosition(motor1, i*teta1/7)
        --sim.setJointPosition(motor2, i*teta2/7)
        --sim.setJointPosition(motor3, i*teta3/7)
        --sim.setJointPosition(motor1, (i*(teta1_1 * math.pi/180)/7))
        --sim.setJointPosition(motor2, (i*(teta2_1 * math.pi/180)/7))
        --sim.setJointPosition(motor3, (i*(teta3_1 * math.pi/180)/7))
        
        sim.setJointTargetPosition(motor1, (teta1+(i*(teta1_1-teta1)/7)) * math.pi/180)
        sim.setJointTargetPosition(motor2, (teta2+(i*(teta2_1-teta2)/7)) * math.pi/180)
        sim.setJointTargetPosition(motor3, (teta3+(i*(teta3_1-teta3)/7)) * math.pi/180)
        
        i = i + 1
        print(i)      
        sim.wait(1, false)
    end
    -- while true do
    --     local p=sim.getObjectPosition(objHandle,-1)
    --     p[1]=p[1]+0.001
    --     sim.setObjectPosition(objHandle,-1,p)
    --     sim.switchThread() -- resume in next simulation step
    -- end
end

-- See the user manual or the available code snippets for additional callback functions and details