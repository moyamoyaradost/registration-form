import math
import random

def solve_quadratic_basic(a, b, c):
    """Решение квадратного уравнения через дискриминант (без SymPy)"""
    discriminant = b*b - 4*a*c
    
    if discriminant < 0:
        return []  # Нет действительных корней
    elif discriminant == 0:
        return [-b / (2*a)]  # Один корень
    else:
        sqrt_d = math.sqrt(discriminant)
        return [(-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a)]

def find_integer_roots_vieta(p, q):
    """
    Поиск целых корней уравнения x² + px + q = 0 методом Виета
    Без использования внешних библиотек
    """
    print(f"\n=== Поиск корней x² + {p}x + {q} = 0 методом Виета ===")
    print(f"Ищем r₁ и r₂: r₁ + r₂ = {-p}, r₁ × r₂ = {q}")
    
    if q == 0:
        # Один корень 0, второй -p
        return [0, -p]
    
    # Находим все делители q
    divisors = []
    for i in range(1, abs(q) + 1):
        if q % i == 0:
            divisors.extend([i, -i])
    
    print(f"Делители {q}: {sorted(set(divisors))}")
    
    # Проверяем все пары делителей
    for r1 in divisors:
        r2 = q // r1
        if r1 + r2 == -p:
            print(f"Найдены корни: r₁ = {r1}, r₂ = {r2}")
            return sorted([r1, r2])
    
    print("Целых корней нет")
    return None

def vieta_trainer():
    """Тренажер для быстрого решения уравнений методом Виета"""
    print("\n" + "="*50)
    print("ТРЕНАЖЕР ТЕОРЕМЫ ВИЕТА")
    print("Решайте уравнения за 5-15 секунд!")
    print("="*50)
    
    examples = [
        # (p, q, описание)
        (-5, -6, "x² - 5x - 6 = 0"),
        (-3, 2, "x² - 3x + 2 = 0"), 
        (2, -8, "x² + 2x - 8 = 0"),
        (-7, 12, "x² - 7x + 12 = 0"),
        (1, -12, "x² + x - 12 = 0"),
        (-4, 3, "x² - 4x + 3 = 0"),
        (6, 9, "x² + 6x + 9 = 0"),
        (-1, -6, "x² - x - 6 = 0"),
    ]
    
    for i, (p, q, description) in enumerate(examples, 1):
        print(f"\n{i}. {description}")
        print("   Подсказки:")
        print(f"   • Сумма корней = {-p}")
        print(f"   • Произведение корней = {q}")
        
        if q > 0:
            print("   • Корни одного знака (оба + или оба -)")
        elif q < 0:
            print("   • Корни разных знаков (один +, другой -)")
        else:
            print("   • Один из корней равен 0")
        
        input("   Нажмите Enter для показа решения...")
        
        # Показываем решение методом Виета
        vieta_roots = find_integer_roots_vieta(p, q)
        
        # Проверяем через дискриминант
        classic_roots = solve_quadratic_basic(1, p, q)
        classic_roots = [round(r, 3) for r in classic_roots]
        
        print(f"   Проверка через дискриминант: {classic_roots}")
        print("   " + "-"*40)

def quick_reference():
    """Быстрая справка по теореме Виета"""
    print("\n" + "="*50)
    print("БЫСТРАЯ СПРАВКА: ТЕОРЕМА ВИЕТА")
    print("="*50)
    print("Для уравнения ax² + bx + c = 0:")
    print("• Сумма корней: r₁ + r₂ = -b/a")
    print("• Произведение корней: r₁ × r₂ = c/a")
    print()
    print("Для приведенного уравнения x² + px + q = 0:")
    print("• Сумма корней: r₁ + r₂ = -p")
    print("• Произведение корней: r₁ × r₂ = q")
    print()
    print("АЛГОРИТМ БЫСТРОГО РЕШЕНИЯ:")
    print("1. Найти все делители свободного члена q")
    print("2. Проверить, какая пара дает нужную сумму -p")
    print("3. Это и есть корни!")
    print()
    print("ПРИЗНАКИ:")
    print("• Если q > 0 → корни одного знака")
    print("• Если q < 0 → корни разных знаков")  
    print("• Если q = 0 → один корень равен 0")

def generate_practice_problems(n=5):
    """Генерация задач для самостоятельной практики"""
    print(f"\n=== {n} ЗАДАЧ ДЛЯ САМОСТОЯТЕЛЬНОГО РЕШЕНИЯ ===")
    
    problems = []
    for i in range(n):
        # Генерируем корни
        r1 = random.randint(-8, 8)
        r2 = random.randint(-8, 8)
        
        # Составляем коэффициенты
        p = -(r1 + r2)
        q = r1 * r2
        
        problems.append((p, q, r1, r2))
        print(f"{i+1}. x² + {p}x + {q} = 0")
    
    input("\nНажмите Enter для показа ответов...")
    
    print("\nОТВЕТЫ:")
    for i, (p, q, r1, r2) in enumerate(problems, 1):
        print(f"{i}. Корни: {sorted([r1, r2])}")

def main():
    print("ТЕОРЕМА ВИЕТА: ПОЛНОЕ РУКОВОДСТВО")
    print("="*40)
    
    while True:
        print("\nВыберите режим:")
        print("1. Быстрая справка")
        print("2. Тренажер с примерами") 
        print("3. Сгенерировать задачи для практики")
        print("4. Решить конкретное уравнение")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == "1":
            quick_reference()
        elif choice == "2":
            vieta_trainer()
        elif choice == "3":
            try:
                n = int(input("Сколько задач сгенерировать? (по умолчанию 5): ") or "5")
                generate_practice_problems(n)
            except ValueError:
                print("Некорректный ввод, генерирую 5 задач")
                generate_practice_problems(5)
        elif choice == "4":
            try:
                print("Введите коэффициенты для уравнения x² + px + q = 0:")
                p = int(input("p = "))
                q = int(input("q = "))
                find_integer_roots_vieta(p, q)
                
                # Дополнительная проверка
                roots = solve_quadratic_basic(1, p, q)
                if roots:
                    print(f"Проверка (точное решение): {[round(r, 4) for r in roots]}")
            except ValueError:
                print("Некорректный ввод")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор")

if __name__ == "__main__":
    main()