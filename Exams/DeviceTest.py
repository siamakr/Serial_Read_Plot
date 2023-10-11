def my_func():
    chamber = EnviromentalChamber("1234")
    psu = PowerSupply("5678")
    component = TestComponent("9012")

    return chamber.get_data() + psu.get_data() + component.get_data()

class Device(object):
    def __init__(self, device_id):
        self.device_id = device_id
        self.latest_data = 12
        
    @property
    def latest_data(self):
        return self._latest_data
    
    @latest_data.setter
    def latest_data(self,val):
        self._latest_data = val
        
    def get_data(self):
        return self.latest_data
    
class EnviromentalChamber(Device):
    def __init__(self, device_id):
        self._latest_data = 3
        super(EnviromentalChamber,self).__init__(device_id)

class PowerSupply(Device):
    def __init__(self, device_id):
        super(PowerSupply, self).__init__(device_id)
        self._latest_data = 25
        
    def get_data(self):
        return self.latest_data * 2
    
class TestComponent(Device):
    def get_data(self):
        return self._latest_data + 8
        

print(my_func())