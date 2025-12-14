"""
Основные функции для работы с квадратными уравнениями и теоремой Виета
"""
import math


def solve_quadratic(a, b, c):
    """
    Решение квадратного уравнения ax² + bx + c = 0
    
    Args:
        a, b, c: коэффициенты уравнения
        
    Returns:
        list: список корней (может быть пустым, содержать 1 или 2 корня)
    """
    if a == 0:
        if b == 0:
            return []
        return [-c / b]
    
    discriminant = b*b - 4*a*c
    
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2*a)]
    else:
        sqrt_d = math.sqrt(discriminant)
        return [
            (-b + sqrt_d) / (2*a),
            (-b - sqrt_d) / (2*a)
        ]


def check_vieta(roots, p, q):
    """
    Проверка теоремы Виета для уравнения x² + px + q = 0
    
    Args:
        roots: список корней
        p, q: коэффициенты уравнения
        
    Returns:
        bool: True если теорема выполняется
    """
    if len(roots) != 2:
        return False
    
    sum_correct = abs(sum(roots) - (-p)) < 1e-6
    prod_correct = abs(roots[0] * roots[1] - q) < 1e-6
    
    return sum_correct and prod_correct


def find_divisors(n):
    """
    Находит все делители числа n (включая отрицательные)
    
    Args:
        n: целое число
        
    Returns:
        list: отсортированный список делителей
    """
    if n == 0:
        return [0]
    
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.extend([i, -i])
    
    return sorted(set(divisors))


def find_roots_vieta(p, q):
    """
    Поиск целых корней уравнения x² + px + q = 0 методом Виета
    
    Args:
        p, q: коэффициенты уравнения
        
    Returns:
        list или None: список корней если найдены, иначе None
    """
    target_sum = -p
    target_prod = q
    
    divisors = find_divisors(target_prod)
    
    for r1 in divisors:
        if r1 == 0 and target_prod != 0:
            continue
            
        r2 = target_prod // r1 if r1 != 0 else 0
        
        if r1 + r2 == target_sum and r1 * r2 == target_prod:
            return sorted([r1, r2])
    
    return None


def vieta_sum_product(a, b, c):
    """
    Вычисляет сумму и произведение корней по теореме Виета
    
    Args:
        a, b, c: коэффициенты уравнения ax² + bx + c = 0
        
    Returns:
        tuple: (сумма, произведение)
    """
    if a == 0:
        return None, None
    
    return -b/a, c/a


def generate_equation_with_roots(r1, r2):
    """
    Создает коэффициенты уравнения x² + px + q = 0 по заданным корням
    
    Args:
        r1, r2: корни уравнения
        
    Returns:
        tuple: (p, q) коэффициенты
    """
    p = -(r1 + r2)
    q = r1 * r2
    
    return p, q
