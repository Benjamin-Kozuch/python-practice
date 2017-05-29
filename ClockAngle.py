def clock_angle(hour,minute): #hour 1-12, Minute 00-59

    print " ---- "
    print "hour: " + str(hour)
    print "minute: " + str(minute)


    hour %= 12 #Since 12 is really 0 
    
    hour *= (360/12)

    hour += (float(minute)/60.0) * (360/12)

    minute = (float(minute)/60.0) * 360

    
    print "hour angle: " + str(hour)
    print "minute angle: " + str(minute)
    print "Difference: " + str(abs(hour-minute))
    print " ---- "
    print "      "


clock_angle(12,0)
clock_angle(12,30)
clock_angle(3,0)
clock_angle(3,30)
clock_angle(6,45)











    



