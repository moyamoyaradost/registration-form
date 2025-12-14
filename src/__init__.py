"""
Vieta Theorem Trainer - Модуль для изучения теоремы Виета
"""

from .vieta_core import (
    solve_quadratic,
    check_vieta,
    find_divisors,
    find_roots_vieta,
    vieta_sum_product,
    generate_equation_with_roots
)

__all__ = [
    'solve_quadratic',
    'check_vieta',
    'find_divisors',
    'find_roots_vieta',
    'vieta_sum_product',
    'generate_equation_with_roots'
]

__version__ = '1.0.0'
