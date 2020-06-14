from abc import ABC, abstractmethod


class Persistor(ABC):

    @abstractmethod
    def read_raw_data(self, data):
        raise NotImplementedError

    @abstractmethod
    def save_raw_data(self, data):
        raise NotImplementedError

    @abstractmethod
    def save_csv(self, data):
        raise NotImplementedError

    @abstractmethod
    def append_data(self, data, record):
        raise NotImplementedError
