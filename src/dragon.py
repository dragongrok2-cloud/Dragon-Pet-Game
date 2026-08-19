# -*- coding: utf-8 -*-
"""Класс дракона-питомца"""

class Dragon:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 50      # 0 = сыт, 100 = очень голоден
        self.happiness = 70   # 0 = грустный, 100 = счастливый
        self.energy = 80      # 0 = устал, 100 = полон сил
        self.age = 0          # дни
        self.level = 1
        self.experience = 0

    def status(self):
        print(f"\n=== {self.name} ===")
        print(f"Уровень: {self.level} | Опыт: {self.experience}/100")
        print(f"Возраст: {self.age} дней")
        print(f"Голод:     {self._bar(self.hunger)} {self.hunger}/100")
        print(f"Счастье:   {self._bar(self.happiness)} {self.happiness}/100")
        print(f"Энергия:   {self._bar(self.energy)} {self.energy}/100")

    def _bar(self, value: int) -> str:
        filled = value // 10
        return "█" * filled + "░" * (10 - filled)

    def feed(self):
        if self.hunger <= 10:
            print(f"{self.name} уже сыт и не хочет есть!")
            return
        self.hunger = max(0, self.hunger - 30)
        self.happiness = min(100, self.happiness + 10)
        self.energy = min(100, self.energy + 5)
        self._gain_exp(10)
        print(f"Ты покормил {self.name}! Он доволен 🍖")

    def play(self):
        if self.energy < 20:
            print(f"{self.name} слишком устал, чтобы играть...")
            return
        self.happiness = min(100, self.happiness + 25)
        self.energy = max(0, self.energy - 20)
        self.hunger = min(100, self.hunger + 15)
        self._gain_exp(15)
        print(f"Вы весело поиграли с {self.name}! 🎾")

    def sleep(self):
        print(f"{self.name} сладко спит... 💤")
        self.energy = min(100, self.energy + 40)
        self.hunger = min(100, self.hunger + 10)
        self.age += 1
        self._gain_exp(5)

    def train_fire(self):
        if self.energy < 30:
            print(f"{self.name} слишком устал для тренировки огня.")
            return
        self.energy = max(0, self.energy - 30)
        self.hunger = min(100, self.hunger + 20)
        self._gain_exp(25)
        print(f"{self.name} учится дышать огнём! 🔥 Рррр!")

    def _gain_exp(self, amount: int):
        self.experience += amount
        if self.experience >= 100:
            self.experience -= 100
            self.level += 1
            print(f"\n🎉 {self.name} достиг уровня {self.level}!")

    def is_alive(self) -> bool:
        return self.hunger < 100 and self.happiness > 0
