import time
import random
class SecuritySystem:
    def __init__(self,system_name,price):
        self.system_name = system_name
        self.price = price
        raw_time = time.gmtime()
        formatted_date = time.strftime("%d/%m/%Y",raw_time)
        self.setup_date = formatted_date

    def activate_alarm(self):
        print("The security alarm has been activated")
        raw_time = time.gmtime()
        formatted_time = time.strftime("%I:%M:%S",raw_time)
        print(f"Security alarm activated at {formatted_time}")

    def check_door_status(self):
        lock = random.randint(1,2)
        if lock == 1:
            print("The door is locked")
        else:
            print("The door is unlocked")

    def detect_motion(self):
        print("Motion is being detected")

class HomeEntertainment:
    def __init__(self,system_name,price):
        self.system_name = system_name
        self.price = price
        raw_time = time.gmtime()
        formatted_date = time.strftime("%d/%m/%Y",raw_time)
        self.setup_date = formatted_date

    def play_music(self,song):
        print(f"Now playing '{song}'..")

    def adjust_volume(self,level):
        print(f"Current volume level: {level}")

    def connect_bluetooth(self,device):
        print(f"Device '{device}' is connected through bluetooth")

class SmartHome(SecuritySystem,HomeEntertainment):
    def __init__(self,system_name,price):
        SecuritySystem.__init__(self,system_name,price)
        HomeEntertainment.__init__(self,system_name,price)
        raw_time = time.gmtime()
        formatted_date = time.strftime("%d/%m/%Y",raw_time)
        self.setup_date = formatted_date

    def control_lights(self,status):
        print(f"Lights are turned {status}")

    def check_temperature(self):
        print(f"Current room temperature: {random.randint(15,25)}")


smart_home = SmartHome("Google Home",20000)
smart_home.activate_alarm()
smart_home.check_door_status()
smart_home.detect_motion()
smart_home.connect_bluetooth("Bose mini speaker")
smart_home.play_music("Centuries")
smart_home.adjust_volume(75)
smart_home.control_lights("OFF")
smart_home.check_temperature()
    




