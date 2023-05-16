# import library for header
from pyfiglet import Figlet
from termcolor import colored

# Create header
f = Figlet(font='3-d')
print(colored(f.renderText("Television"), 'green').center(50))
print(colored(("=" * 72), color='green'))
# create class named TV
class TV:
    # create constructor
    # Set default channel, volume, power status
    def __init__(self, channel=1, volume_lvl=0, tv_on=False):
        # create instance variables
        self.channel = channel
        self.volume_lvl = volume_lvl
        self.tv_on = tv_on

    # instance method (turn on TV)
    def turn_on(self):
        self.tv_on = True
        print("The TV is " + colored("ON", color='green'))

            
    # instance method (turn off TV)
    def turn_off(self):
        self.tv_on = False
        print("The TV is " + colored("OFF", color='red'))

    # instance method (return channel)
    def get_channel(self):
        if self.tv_on:
            return self.channel
    
    # instance method (set new channel)
    def set_channel(self, new_channel):
        if self.tv_on:
            self.channel = new_channel
            
    # instance method (return volume)
    def get_volume(self):
        if self.tv_on:
            return self.volume_lvl
        
    # instance method (set new channel)
    def set_volume(self, new_volume_lvl):
        if self.tv_on:
            self.volume_lvl = new_volume_lvl
            # Max 100
            if self.volume_lvl > 100:
                self.volume_lvl = 100

    # instance method (increase channel by 1)
    def channel_up(self):
        if self.tv_on:
            self.channel += 1
            
    # instance method (decrease channel by 1)
    def channel_down(self):
        if self.tv_on:
            self.channel -= 1

    # instance method (increase volume by 1)
    def volume_up(self):
        if self.tv_on:
            # Max 100
            if self.volume_lvl < 100:
                self.volume_lvl += 1
            else:
                self.volume = 100

    # instance method (decrease volume by 1)
    def volume_down(self):
        if self.tv_on:
            # Min 00
            if self.volume_lvl > 0:
                self.volume_lvl -= 1
