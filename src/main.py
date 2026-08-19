# -*- coding: utf-8 -*-
"""
Dragon Pet Game
Простая текстовая игра, где ты заботишься о своём дракончике.
"""

from dragon import Dragon

def main():
    print("=" * 50)
    print("🐉  Добро пожаловать в Dragon Pet Game!  🐉")
    print("=" * 50)
    print()

    name = input("Как назовём твоего дракончика? → ").strip()
    if not name:
        name = "Искра"

    pet = Dragon(name)
    print(f"\nПрекрасно! {name} появился на свет! 🐣🔥\n")

    while pet.is_alive():
        pet.status()
        print("\nЧто будем делать?")
        print("1. Покормить 🍖")
        print("2. Поиграть 🎾")
        print("3. Уложить спать 💤")
        print("4. Тренировать огонь 🔥")
        print("5. Выйти")

        choice = input("\nТвой выбор (1-5): ").strip()

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.train_fire()
        elif choice == "5":
            print(f"\nДо встречи! {pet.name} будет скучать по тебе... 🐉")
            break
        else:
            print("Не понимаю... Попробуй ещё раз.")

        # Небольшой естественный рост голода и усталости
        pet.hunger = min(100, pet.hunger + 5)
        pet.energy = max(0, pet.energy - 3)

        if not pet.is_alive():
            print(f"\nО нет... {pet.name} слишком плохо себя чувствует.")
            print("Игра окончена. Позаботься лучше в следующий раз!")
            break

    print("\nСпасибо, что играл! 🔥")

if __name__ == "__main__":
    main()
