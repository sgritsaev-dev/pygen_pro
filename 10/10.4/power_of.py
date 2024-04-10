class PowerOf():
    def __init__(self, number) -> None:
        PowerOf.number = number
        PowerOf.ind = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.ind+=1
        return self.number**self.ind 
    
power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
        