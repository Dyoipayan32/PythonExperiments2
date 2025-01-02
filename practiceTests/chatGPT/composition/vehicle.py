from practiceTests.chatGPT.composition.engine import Engine


class Vehicle:
    def __init__(self):
        # contained object
        self.engine = Engine()

    # contained object
    def play_v1(self):
        print("Vehicle will start")

    def play_v2(self):
        print("This is v2")

    def play_v3(self):
        print("This is v3")

    # contained object
    class MusicPlayer:
        def __init__(self):
            pass

        def play_m1(self):
            print("m1- music is playing.")

        def play_m2(self):
            print("This is m2")

        def play_m3(self):
            print("This is m3")


# container object
vehicle = Vehicle()
vehicle.play_v1()
vehicle.engine.start_engine()
vehicle.engine.stop_engine()
musicPlayer = vehicle.MusicPlayer()
musicPlayer.play_m1()
