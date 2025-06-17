import math
from typing import Callable, Optional

# Zadanie 1: Prosty Kalkulator z Funkcjami Wyższego Rzędu
# Cel: Stwórz kalkulator, który używa funkcji wyższego rzędu do definiowania operacji matematycznych.
# Zamiast czterech oddzielnych funkcji, będziemy mieli jedną funkcję 'calculate',
# która przyjmuje operację (inną funkcję) jako argument.
# Dodatkowo, obsłuż dzielenie przez zero, zwracając 'None' dla wskazania błędu.

class FunctionalCalculator:
    ZERO = 0.0

    def calculate(self, a: float, b: float, operation: Callable[[float, float], float]) -> float:
        """
        Wykonuje operację matematyczną na dwóch liczbach.
        :param a: Pierwsza liczba.
        :param b: Druga liczba.
        :param operation: Funkcja (callable), która definiuje operację (np. dodawanie, odejmowanie).
        :return: Wynik operacji.
        """
        # TODO 1: Zaimplementuj logikę wykonania operacji.
        pass

    def calculate_safe(self, a: float, b: float, operation: Callable[[float, float], Optional[float]]) -> Optional[float]:
        """
        Wykonuje operację matematyczną na dwóch liczbach, zwracając Optional[float]
        w celu bezpiecznej obsługi potencjalnych błędów (np. dzielenia przez zero).
        :param a: Pierwsza liczba.
        :param b: Druga liczba.
        :param operation: Funkcja (callable), która definiuje operację i zwraca Optional[float].
        :return: Wynik operacji lub None, jeśli wystąpił błąd.
        """
        # TODO 2: Zaimplementuj logikę bezpiecznego wykonania operacji.
        pass

if __name__ == "__main__":
    calculator = FunctionalCalculator()

    # TODO 3: Zdefiniuj operacje dodawania, odejmowania i mnożenia jako funkcje lambda.
    add = None
    subtract = None
    multiply = None

    # TODO 4: Zdefiniuj funkcję dzielenia 'divide_safe', która zwraca None w przypadku dzielenia przez zero.
    def divide_safe(x: float, y: float) -> Optional[float]:
        pass

    # Przykładowe użycie (po uzupełnieniu TODOs)
    # print(f"Dodawanie (5 + 3): {calculator.calculate(5, 3, add)}")
    # print(f"Dzielenie (10 / 2) bezpiecznie: {calculator.calculate_safe(10, 2, divide_safe)}")
    # print(f"Dzielenie (5 / 0) bezpiecznie: {calculator.calculate_safe(5, 0, divide_safe)}")