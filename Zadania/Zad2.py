from functools import reduce
from typing import Dict, Optional, List

# Zadanie 2: Analiza Statystyk Listy Liczb (Funkcyjne Podejście)
# Cel: Zoptymalizuj kod do analizy listy liczb (min, max, średnia, suma),
# wykorzystując funkcję 'reduce' do wykonania wszystkich obliczeń w jednym przejściu.
# Odpowiedz na pytania w komentarzach.

def analyze_numbers_functional_single_pass(numbers: List[int]) -> Dict[str, Optional[float]]:
    """
    Analizuje listę liczb i zwraca statystyki (min, max, suma, średnia)
    wykorzystując funkcyjne podejście i pojedyncze przejście z reduce.
    """
    if not numbers:
        return {"min": None, "max": None, "sum": 0, "average": None}

    # TODO 1: Jakie korzyści płyną z pojedynczego przejścia po liście w porównaniu do wielu pętli?
    # Odpowiedź 1:

    # TODO 2: Zaimplementuj funkcję redukującą (akumulator), która będzie zbierać min, max, sumę i count.
    # Ta funkcja powinna przyjmować bieżący stan (słownik) i nową liczbę, zwracając nowy stan.
    def stats_accumulator(acc: Dict[str, float], x: int) -> Dict[str, float]:
        pass

    # TODO 3: Zdefiniuj początkową wartość akumulatora (initial_stats) dla funkcji reduce.
    # Pamiętaj o obsłudze przypadku, gdy 'numbers' nie jest pusta.
    initial_stats = None

    # TODO 4: Użyj 'reduce' z zaimplementowanym akumulatorem i wartością początkową.
    final_stats = None

    # TODO 5: Wyciągnij końcowe wartości statystyk i oblicz średnią, pamiętając o przypadku dzielenia przez zero.
    min_value = None
    max_value = None
    total_sum = None
    average_value = None

    return {
        "min": float(min_value) if min_value is not None else None,
        "max": float(max_value) if max_value is not None else None,
        "sum": float(total_sum),
        "average": average_value
    }

if __name__ == "__main__":
    numbers_list = [3, 7, 2, 9, 4, 10, 5]
    # stats = analyze_numbers_functional_single_pass(numbers_list)
    # print(f"Maksymalna wartość: {stats['max']}")