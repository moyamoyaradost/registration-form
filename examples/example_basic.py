"""
Простой пример использования теоремы Виета
Решает уравнение x² - 5x - 6 = 0
"""
import sys
sys.path.insert(0, '../src')

from vieta_core import solve_quadratic, check_vieta, vieta_sum_product

# Уравнение: x² - 5x - 6 = 0
a, b, c = 1, -5, -6

print("="*50)
print("ПРИМЕР: Решение уравнения x² - 5x - 6 = 0")
print("="*50)

# Решаем через дискриминант
roots = solve_quadratic(a, b, c)
print(f"\n1. Корни (через дискриминант): {roots}")

# Вычисляем сумму и произведение
if len(roots) == 2:
    sum_roots = sum(roots)
    prod_roots = roots[0] * roots[1]
    
    print(f"\n2. Вычисления:")
    print(f"   Сумма корней: {sum_roots}")
    print(f"   Произведение корней: {prod_roots}")

# Проверка по теореме Виета
vieta_sum, vieta_prod = vieta_sum_product(a, b, c)
print(f"\n3. По теореме Виета:")
print(f"   Сумма = -b/a = -({b})/{a} = {vieta_sum}")
print(f"   Произведение = c/a = {c}/{a} = {vieta_prod}")

# Проверка
p, q = b, c
is_correct = check_vieta(roots, p, q)
print(f"\n4. Проверка: {'✅ Теорема подтверждается!' if is_correct else '❌ Ошибка'}")
