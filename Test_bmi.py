import  lab2.bmi as bmi  


def test_bmi_underweight():
    if bmi < 18.5:
        print ("Under Weight")


def test_bmi_overweight():
    if bmi > 25.0:
        print ("Over Weight")


def test_bmi_normalweight():
    if bmi >= 18.5 or bmi <= 25.0:
        print ("Normal Weight")
