#import pyfiglet
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
    def get_volume(self):
        if self.tv_on:
            return self.volume_lvl
        
    # instance method (set new channel)
    def set_volume(self, new_volume_lvl):
        if self.tv_on:
            self.volume_lvl = new_volume_lvl

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
            self.volume_lvl += 1

    # instance method (decrease volume by 1)
    def volume_down(self):
        if self.tv_on:
            self.volume_lvl -= 1

# Create a Test Driver program named TestTV
class Test_TV:
    def test(self):   
        # Object 1(TV1)
        print("TV1 Status".center(50))
        print("=" * 50)
        tv1 = TV()
        tv1.turn_on()
        tv1.get_channel()
        tv1.set_channel(6)
        tv1.channel_up()
        tv1.channel_up()
        tv1.channel_down()
        tv1.get_volume()
        tv1.set_volume(6)
        tv1.volume_up()
        tv1.volume_up()
        tv1.volume_down()
        print(f"TV1's channel is {tv1.channel} and volume level is {tv1.volume_lvl}")

        # Object 2(TV2)
        print("TV2 Status".center(50))
        print("=" * 50)
        tv2 = TV()
        tv2.turn_on()
        tv2.get_channel()
        tv2.set_channel(6)
        tv2.channel_up()
        tv2.channel_up()
        tv2.channel_down()
        tv2.get_volume()
        tv2.set_volume(6)
        tv2.volume_up()
        tv2.volume_up()
        tv2.volume_down()
        print(f"TV2's channel is {tv2.channel} and volume level is {tv2.volume_lvl}")

#__start__
test_run = Test_TV()
test_run.test()