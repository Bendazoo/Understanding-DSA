import time

class Array():

    def __init__(self):
        self.list = []
        self.index = 0
        self.length = 0
    
    def add_element(self, element):
        self.list.append(element)
        self.length += 1
        

    def check_element(self, index):
        value = self.list[index]
        return value
    
    def max_element(self):
        num = 0
        for i in range(len(self.list)):
            if self.list[i] > num:
                num = self.list[i]
        return num

    def insertion_sort(self):
        if self.length == 0 :
            return None
        if self.length == 1:
            return self.list
        else:
            for i in range(self.length):
                num = self.list[i]
                while num > self.list[index]:
                    temp = self.list[index]
                    self.list[i] = temp
                    self.list[index] = num
                    num = self.list[index]
                    index += 1

                

                    
                    
                    
        
    def __str__(self):
        return str(self.list)

    def __len__(self):
        return self.length

    


if __name__ == "__main__":
    start_time = time.time()

    array = Array()

    array.add_element(12)
    array.add_element(11)
    array.add_element(13)
    array.add_element(5)
    array.add_element(6)
    print(array)




    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time) 