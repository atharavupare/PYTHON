#!/usr/local/bin/python3.7
import sys

class SpeedLimitError(Exception): #INHERITANCE FOR OUR USER DEFINED CLASS FROM DEFAULT EXCEPTION CLASS IS NECESSARY TO WRITE USER DEFINED EXCEPTION CLASS
    def __init__(self, speed):
        self.speed = speed
    def __str__(self): #TO PRINT OBJECT
        return "Vehicle Speed is " + str(self.speed)

class SpeedBelowLimit(SpeedLimitError):
    def __init__(self, speed):
        SpeedLimitError.__init__(self, speed)

class SpeedAboveLimit(SpeedLimitError):
    def __init__(self, speed):
        SpeedLimitError.__init__(self, speed)

if __name__=="__main__":
    while True:
        try:
            speed = float(input("Enter Speed: "))
            if speed < 20:
                x = SpeedBelowLimit(speed)
                raise x #throwing an object means throwing exception for that class, in this case SpeedBelowLimit is inherited from SpeedLimitError which is in turn inherited from Exception
                #raise SpeedBelowLimit(speed)
            elif speed > 80:
                raise SpeedAboveLimit(speed)
            else:
                print("Speed In Limit")
                break
        except ValueError as t:
            print("TypeError:", t)
        except SpeedBelowLimit as e:
            print("Speed Below Limit:", e)
        except SpeedAboveLimit as e:
            print("Speed Above Limit:", e)
