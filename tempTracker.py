"""class to find min, max and mean temperatures"""

class TempTracker(object):
    def __init__(self):
        # for min
        self.min_temp = float('inf')

        # for max
        self.max_temp = float('-inf')

        # For mean
        self.number_of_readings = 0
        self.total_sum = 0.0  
        self.mean = None

    def insert(self, temp):

        if (temp >=0 and temp<111):
            # for min
            if (temp > self.max_temp):
                self.max_temp = temp
            
            # for max
            if (temp < self.min_temp):
                self.min_temp = temp

            # for mean
            self.number_of_readings += 1
            self.total_sum += temp
            self.mean = self.total_sum / self.number_of_readings

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

if __name__ == '__main__':

    temp = TempTracker()
    temp.insert(1)
    temp.insert(55)
    temp.insert(90)
    temp.insert(110)    
    
    print("Max temperature is " + str(temp.get_max()))
    print("Min temperature is " + str(temp.get_min()))
    print("Mean is " + str(temp.get_mean()))
