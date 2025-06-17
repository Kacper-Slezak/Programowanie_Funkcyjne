from typing import Callable, List, Any

# Zadanie 4: Kompozycja Funkcji do Przetwarzania Danych
# Cel: Zaimplementuj funkcję 'compose', która przyjmuje wiele funkcji i zwraca jedną, złożoną funkcję,
# która je wywołuje w odpowiedniej kolejności (od prawej do lewej).
# Następnie zaimplementuj 'pipeline' dla kolejności od lewej do prawej.
# Użyj tych funkcji do przetworzenia listy danych.

def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Tworzy złożoną funkcję, która wykonuje podane funkcje w kolejności
    od prawej do lewej (jak w matematyce: f(g(x))).
    :param functions: Funkcje do skomponowania.
    :return: Skomponowana funkcja.
    """
    # TODO 1: Zaimplementuj logikę kompozycji funkcji.
    pass

def pipeline(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Tworzy złożoną funkcję (pipeline), która wykonuje podane funkcje w kolejności
    od lewej do prawej.
    :param functions: Funkcje do skomponowania.
    :return: Skomponowana funkcja.
    """
    # TODO 2: Zaimplementuj logikę pipeline'u funkcji.
    pass

if __name__ == "__main__":
    # Przykładowe funkcje do kompozycji
    def add_five(x: int) -> int: return x + 5
    def multiply_by_two(x: int) -> int: return x * 2
    def to_string(x: int) -> str: return str(x) + "!"
    def capitalize_string(s: str) -> str: return s.upper()

    print("--- Kompozycja funkcji (f(g(x))) ---")
    # TODO 3: Użyj 'compose' do stworzenia funkcji, która najpierw doda 5,
    # potem pomnoży przez 2, potem zamieni na string, a na końcu zamieni na duże litery.
    # Pamiętaj o kolejności (od prawej do lewej dla compose).
    # transform_data_composed = compose(...)
    # print(f"Wynik compose dla 3: {transform_data_composed(3)}")

    print("\n--- Pipeline funkcji (f | g | h) ---")
    # TODO 4: Użyj 'pipeline' do stworzenia funkcji, która najpierw doda 5,
    # potem pomnoży przez 2, potem zamieni na string, a na końcu zamieni na duże litery.
    # Pamiętaj o kolejności (od lewej do prawej dla pipeline).
    # transform_data_pipeline = pipeline(...)
    # print(f"Wynik pipeline dla 3: {transform_data_pipeline(3)}")

    # TODO 5: Zastosuj jedną ze skomponowanych funkcji do listy liczb za pomocą 'map'.
    # numbers_to_process = [1, 2, 3]
    # processed_numbers = list(map(..., numbers_to_process))
    # print(f"Przetworzona lista: {processed_numbers}")