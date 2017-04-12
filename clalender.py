month = int(input ("enter the no of days (28-31) :"))
day = int(input ("enter the no of days (0-sun,1-mon,2-tue,3-wed,4-thu,5-fri,6-sat) : "))
print('m','t','w','th','f','s','s')
i = 1
for i in range (1,month+1) :
        i <= month
        print (i,end=" ")
    
      
        if (i+day)%7 == 0 :
            print (" "*day)
            i = i + 1
           
