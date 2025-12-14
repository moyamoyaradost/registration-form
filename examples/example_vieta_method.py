"""
Пример поиска корней методом подбора (теорема Виета)
Демонстрирует как быстро найти корни без формулы дискриминанта
"""
import sys
sys.path.insert(0, '../src')

from vieta_core import find_roots_vieta, find_divisors

# Несколько примеров уравнений
equations = [
    (-5, -6, "x² - 5x - 6 = 0"),
    (-3, 2, "x² - 3x + 2 = 0"),
    (2, -8, "x² + 2x - 8 = 0"),
    (-7, 12, "x² - 7x + 12 = 0"),
]

print("="*60)
print("ПРИМЕРЫ: Поиск корней методом Виета")
print("="*60)

for p, q, equation in equations:
    print(f"\n{equation}")
    print(f"Сумма корней должна быть: {-p}")
    print(f"Произведение корней должно быть: {q}")
    
    divisors = find_divisors(q)
    print(f"Делители {q}: {divisors}")
    
    roots = find_roots_vieta(p, q)
    if roots:
        print(f"✅ Корни: {roots}")
        print(f"   Проверка: {roots[0]} + {roots[1]} = {sum(roots)}, "
              f"{roots[0]} × {roots[1]} = {roots[0] * roots[1]}")
    else:
        print(f"❌ Целые корни не найдены")
    
    print("-"*60)
