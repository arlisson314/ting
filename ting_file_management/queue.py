from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.__len__():
            return None
        return self.data.pop(0)

    def search(self, index):
        if 0 > index or index > self.__len__():
            raise IndexError()
        else:
            return self.data[index]
