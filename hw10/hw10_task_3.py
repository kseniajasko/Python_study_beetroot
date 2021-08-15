# Task 3
#
# TV controller

class TVController():
    channels = []
    active_channel = None

    def __init__(self, channels):
        if not channels or len(channels) == 0:
            print('Error, pass channels list')
            return
        else:
            self.channels = channels

    def first_channel(self):
        self.active_channel = self.channels[0]
        return self.active_channel


    def last_channel(self):
        self.active_channel = self.channels[-1]
        return self.active_channel


    def is_exist(self, search_channel):
        for i in self.channels:
            if i == search_channel or self.channels.index(i) == int(search_channel)-1:
                print('Channel exist')
                return True

        else: print("No such channel")
        return False

    def turn_channel(self, num_turn_ch = 0):
        if num_turn_ch == 0:
            print("Please enter channel number")
            return

        for i in self.channels:
            if self.channels.index(i) == int(num_turn_ch)-1:
                self.active_channel = i
                print(self.active_channel)
                break
        else:
            print("Wrong number channel")

    def current_channel(self):
        if not self.active_channel:
            print("No active channel")
            return
        print(f"Active channel is {self.active_channel}")

    def next_channel(self):
        if not self.active_channel:
            print("No turned on channels")
            return

        ind1 = 0
        for i in self.channels:
            if i == self.active_channel:
                ind1 = self.channels.index(i)+1
                break

        if  ind1 > len(self.channels)-1:
            self.active_channel = self.channels[0]
            print(self.active_channel)
            return self.active_channel
        else:
            self.active_channel = self.channels[ind1]
            print(self.active_channel)
            return self.active_channel

    def previous_channel(self):
        if not self.active_channel:
            print("No turned on channels")
            return

        for i in self.channels:
            if i == self.active_channel:
                ind2 = self.channels.index(i) - 1
                self.active_channel = self.channels[ind2]
                break
        print(self.active_channel)

CHANNELS = ["BBC", "Discovery", "TV1000", "MTV"]
controller = TVController(CHANNELS)


controller.first_channel()
controller.last_channel()

# #number or name channel
controller.is_exist(2)

# #number channel
controller.turn_channel(1)

controller.next_channel()
controller.previous_channel()


controller.current_channel()