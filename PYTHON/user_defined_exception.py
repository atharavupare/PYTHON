#!/usr/local/bin/python3.7

class SpeedLimitError(Exception):
    def __init__(self, speed):
        self.speed = speed
    def __str__(self):
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
            speed = int(input("Enter Speed: "))
            if speed < 20:
                x = SpeedBelowLimit(speed)
                raise x
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
