"""
Utils by Icaro D. Temponi (Umbranox)
https://github.com/icarohs7
"""
from typing import Callable, TypeVar

T = TypeVar("T")
Predicate = Callable[[T], bool]
__all__ = ["files", "validation", "T", "Predicate"]
