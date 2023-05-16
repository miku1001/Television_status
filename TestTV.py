# iMPORT CLASS TV
from TV import TV
from termcolor import colored

# Create a Test Driver program named TestTV
class TestTV:
    def test(self):   
        # Object 1(TV1)
        print("\033[1;31;40m TV1 Status \033[0m".center(80))
        print(colored(("-" * 72), color='red'))
        tv1 = TV()
        tv1.turn_on()
        tv1.get_channel()
        tv1.set_channel(5)
        tv1.channel_up()
        tv1.channel_up()
        tv1.channel_down()
        tv1.get_volume()
        tv1.set_volume(6)
        tv1.volume_up()
        tv1.volume_up()
        tv1.volume_down()

        # Print the volume and channel
        print(f"TV1's channel is\033[33m {tv1.channel}\033[0m and volume level is \033[34m{tv1.volume_lvl}\033[0m \n")

        # Object 2(TV2)
        print("\033[1;31;40m TV2 Status \033[0m".center(80))
        print(colored(("-" * 72), color='red'))
        tv2 = TV()
        tv2.turn_on()
        tv2.get_channel()
        tv2.set_channel(4)
        tv2.channel_up()
        tv2.channel_up()
        tv2.channel_down()
        tv2.get_volume()
        tv2.set_volume(4)
        tv2.volume_up()
        tv2.volume_up()
        tv2.volume_down()

        # Print the volume and channel
        print(f"TV2's channel is\033[33m {tv2.channel}\033[0m and volume level is \033[34m{tv2.volume_lvl}\033[0m")

#__start__
test_run = TestTV()
test_run.test()