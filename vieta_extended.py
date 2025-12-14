from sympy import symbols, solve
import random

def analyze_quadratic(a, b, c):
    """Анализ квадратного уравнения ax² + bx + c = 0 с применением теоремы Виета"""
    print(f"\n=== Анализ уравнения {a}x² + {b}x + {c} = 0 ===")
    
    x = symbols('x')
    eq = a*x**2 + b*x + c
    roots = solve(eq, x)
    
    print(f"Корни: {roots}")
    
    if len(roots) == 2:
        sum_roots = sum(roots)
        prod_roots = roots[0] * roots[1]
        
        print(f"Сумма корней: {sum_roots}")
        print(f"Произведение корней: {prod_roots}")
        
        # Проверка по теореме Виета
        theoretical_sum = -b/a
        theoretical_prod = c/a
        
        print(f"\nПо теореме Виета:")
        print(f"Сумма корней = -b/a = -({b})/{a} = {theoretical_sum}")
        print(f"Произведение корней = c/a = {c}/{a} = {theoretical_prod}")
        
        # Проверка совпадения
        if abs(float(sum_roots) - theoretical_sum) < 0.0001 and abs(float(prod_roots) - theoretical_prod) < 0.0001:
            print("✅ Теорема Виета подтверждается!")
        else:
            print("❌ Ошибка в вычислениях")
    else:
        print("Уравнение имеет менее 2 действительных корней")

def find_roots_by_vieta(p, q):
    """
    Поиск корней уравнения x² + px + q = 0 методом подбора (теорема Виета)
    Сумма корней = -p, произведение = q
    """
    print(f"\n=== Поиск корней уравнения x² + {p}x + {q} = 0 методом Виета ===")
    print(f"Ищем два числа r₁ и r₂ такие, что:")
    print(f"r₁ + r₂ = {-p}")
    print(f"r₁ × r₂ = {q}")
    
    # Перебираем делители q
    if q == 0:
        divisors = [0, 1, -1]
    else:
        divisors = []
        for i in range(1, abs(q) + 1):
            if q % i == 0:
                divisors.extend([i, -i, q//i, -q//i])
        divisors = list(set(divisors))  # Убираем дубликаты
    
    print(f"Возможные делители {q}: {sorted(set(divisors))}")
    
    solutions = []
    for r1 in divisors:
        if r1 == 0 and q != 0:
            continue
        r2 = q / r1 if r1 != 0 else 0
        if r1 + r2 == -p:
            solutions.append((r1, r2))
    
    if solutions:
        print(f"Найденные пары корней: {solutions}")
        print(f"Корни: {sorted(set([r for pair in solutions for r in pair]))}")
    else:
        print("Целые корни не найдены. Возможно, корни дробные или иррациональные.")
    
    return solutions

def interactive_examples():
    """Интерактивные примеры для практики"""
    print("\n" + "="*50)
    print("ИНТЕРАКТИВНЫЕ ПРИМЕРЫ ДЛЯ ПРАКТИКИ")
    print("="*50)
    
    examples = [
        (1, -5, -6),   # x² - 5x - 6 = 0
        (1, -3, 2),    # x² - 3x + 2 = 0  
        (1, 2, -8),    # x² + 2x - 8 = 0
        (1, -7, 12),   # x² - 7x + 12 = 0
        (2, -6, 4),    # 2x² - 6x + 4 = 0
    ]
    
    for a, b, c in examples:
        analyze_quadratic(a, b, c)
        if a == 1:  # Для приведенных уравнений показываем метод подбора
            find_roots_by_vieta(b, c)
        print("-" * 50)

def generate_random_equation():
    """Генерация случайного уравнения с целыми корнями"""
    print("\n=== СЛУЧАЙНОЕ УРАВНЕНИЕ ДЛЯ ТРЕНИРОВКИ ===")
    
    # Генерируем два случайных корня
    r1 = random.randint(-10, 10)
    r2 = random.randint(-10, 10)
    
    # Составляем уравнение по корням: (x - r1)(x - r2) = x² - (r1+r2)x + r1*r2
    p = -(r1 + r2)  # коэффициент при x
    q = r1 * r2     # свободный член
    
    print(f"Решите уравнение: x² + {p}x + {q} = 0")
    print("Попробуйте найти корни методом Виета!")
    print(f"Подсказка: ищите два числа, сумма которых = {-p}, произведение = {q}")
    
    input("\nНажмите Enter, чтобы увидеть решение...")
    
    print(f"\nРешение:")
    print(f"Корни: {sorted([r1, r2])}")
    analyze_quadratic(1, p, q)

def main():
    print("ИЗУЧЕНИЕ ТЕОРЕМЫ ВИЕТА С PYTHON")
    print("="*40)
    
    # Основной пример из вашего кода
    print("\n1. Ваш исходный пример:")
    x = symbols('x')
    eq = x**2 - 5*x - 6
    roots = solve(eq, x)
    print("Корни:", roots)
    sum_roots = sum(roots)
    prod_roots = roots[0] * roots[1]
    print("Сумма корней:", sum_roots)
    print("Произведение корней:", prod_roots)
    
    # Расширенный анализ
    print("\n2. Расширенный анализ:")
    interactive_examples()
    
    # Генерация случайного примера для практики
    print("\n3. Тренировка:")
    generate_random_equation()

if __name__ == "__main__":
    main()