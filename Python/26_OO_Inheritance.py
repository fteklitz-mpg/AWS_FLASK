# OO_Inheritance.py
# used for hierarchical relationships

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnecting.")


class Printer(Device):    #Printer class inherits from Device
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"printing {pages} pages.")
        self.remaining_pages -= pages
        

print("Printer as Device")
printer = Device("Printer", "USB")
print(printer)
printer.disconnect()

print("Printer as child class of Device")
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(30)


