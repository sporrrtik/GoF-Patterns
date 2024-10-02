from abc import ABC, abstractmethod
from datetime import datetime

# Наблюдатель
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Субъект
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Субъект - Работник
class Worker(Subject):
    def __init__(self, name: str):
        self._observers = []
        self._name = name
        self._status = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        message = f"Работник {self._name}: {self._status} в {datetime.now()}"
        for observer in self._observers:
            observer.update(message)

    def start_work(self):
        self._status = "начал работу"
        self.notify()

    def end_work(self):
        self._status = "завершил работу"
        self.notify()

# Наблюдатель - Логировщик времени
class TimeLogger(Observer):
    def update(self, message: str):
        print(f"[Логировщик времени] {message}")

# Наблюдатель - Служба уведомлений
class NotificationService(Observer):
    def update(self, message: str):
        print(f"[Служба уведомлений] Уведомление: {message}")

# Использование паттерна
if __name__ == "__main__":
    worker = Worker("Иван")
    time_logger = TimeLogger()
    notification_service = NotificationService()

    worker.attach(time_logger)
    worker.attach(notification_service)

    worker.start_work()
    worker.end_work()
