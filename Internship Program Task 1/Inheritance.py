class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print("Making a call...")

    def receive_call(self):
        print("Receiving a call...")

    def take_picture(self):
        print("Taking a picture...")

    def send_message(self):
        print("Sending a message...")

    def check_network(self):
        print("Network type:",self.network_type)

    def check_storage(self):
        print("Storage:",self.storage)

    def check_ram(self):
        print("RAM:",self.ram)

    def check_camera(self):
        print("Front camera:",self.front_camera)
        print("Rear camera:",self.rear_camera)


class Apple(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)

    def take_a_picture(self):
        print("Taking a picture with Apple camera...")

    def send_message(self):
        print("Sending a message with Apple messaging app...")

    def check_storage(self):
        print("Storage:",self.storage,"(Apple storage)")

class Samsung(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)

    def take_a_picture(self):
        print("Taking a picture with Samsung camera...")

    def send_message(self):
        print("Sending a message with Samsung messaging app...")

    def check_storage(self):
        print("Storage:",self.storage,"(Samsung storage)")

apple_phone1 = Apple("Touch Screen", "4G", True, "5MP", "12MP", "4GB", "64GB")

samsung_phone1 = Samsung("Touch Screen", "4G", True, "12MP", "32MP", "4GB", "64GB")

apple_phone1.make_call()
apple_phone1.receive_call()
apple_phone1.take_picture()
apple_phone1.send_message()
apple_phone1.check_network()
apple_phone1.check_storage()
apple_phone1.check_ram()
apple_phone1.check_camera()

print("\n")

samsung_phone1.make_call()
samsung_phone1.receive_call()
samsung_phone1.take_picture()
samsung_phone1.send_message()
samsung_phone1.check_network()
samsung_phone1.check_storage()
samsung_phone1.check_ram()
samsung_phone1.check_camera()