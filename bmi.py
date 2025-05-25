def calculate_bmi(height, weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))
    
    bmi = weight / (height * height)
    print ("BMI = " + str(bmi))
    bmi = calculate_bmi(weight=57, height=1.73) 
    
    if (bmi < 18.5):
        print ("under weight")
        return -1
    elif (bmi>18.5 and bmi<=25.0):
        print ("nomral weight")
        return 0
    elif(bmi>25):
        print ("over weight")
        return 1
