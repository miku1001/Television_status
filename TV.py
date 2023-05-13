# create class named TV
class TV:
    # create constructor
    def __init__(self, channel=1, volume_lvl=0, tv_on=False):
        # create instance variables
        self.channel = channel
        self.volume_lvl = volume_lvl
        self.tv_on = tv_on

    # instance method (turn on TV)
    def turn_on(self):
        self.tv_on = True
        print("The TV is on")

            
    # instance method (turn off TV)
    def turn_off(self):
        self.tv_on = False
        print("The TV is off")

    # instance method (return channel)
    def get_channel(self):
        if self.tv_on:
            return self.channel
    
    # instance method (set new channel)
    def set_channel(self, new_channel):
        if self.tv_on:
            self.channel = new_channel
            
    # instance method (return volume)
# instance method (set new channel)
# instance method (increase channel by 1)
# instance method (decrease channel by 1)
# instance method (increase volume by 1)
# instance method (decrease volume by 1)