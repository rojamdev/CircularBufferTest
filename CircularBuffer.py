import random
import time


class CircularBuffer:

    def __init__(self, size):
        self.size = size
        self.circular_array = [0] * self.size
        self.write_index = 0
        
    def set_data(self, data):
        self.circular_array[self.write_index] = data

    def get_data(self, delay):

        if delay > 0 & delay < self.size:
            
            read_index = self.write_index - delay

            if read_index < 0:
                read_index += self.size

            sample = self.circular_array[read_index]

            return sample

    def next_sample(self):
        self.write_index += 1

        if (self.write_index >= (self.size)):
            self.write_index = 0


def create_audio(length, res):
    
    array = []
    
    for i in range(0, length - 1):
        sample = random.randint(0, res) / res
        array.append(sample)

    return array


def main():
    
    audio = create_audio(100, 100)
    print(audio)

    circular_buffer = CircularBuffer(8)

    sample_delay = 5

    for i in range(0, len(audio)):
        sample = audio[i]
        circular_buffer.set_data(sample) 

        print(circular_buffer.circular_array)
        print(sample, circular_buffer.get_data(sample_delay))
        
        circular_buffer.next_sample()

        time.sleep(1)


main()