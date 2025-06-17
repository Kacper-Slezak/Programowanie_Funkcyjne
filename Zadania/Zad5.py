from functools import reduce
from typing import List, Dict, Any

# Zadanie 5: Zaawansowane Przetwarzanie Kolekcji z 'reduce' i Immutability
# Cel: Mając listę obiektów 'Transaction', użyj funkcji 'reduce' do zagregowania danych
# w bardziej złożony sposób, na przykład do obliczenia salda konta i kategoryzacji transakcji.
# Upewnij się, że proces jest niezmienny, tj. nie modyfikuje oryginalnych obiektów
# ani pośrednich struktur danych akumulatora.

class Transaction:
    def __init__(self, type: str, amount: float):
        self.type = type # "deposit" or "withdrawal"
        self.amount = amount

    def __repr__(self):
        return f"Transaction(type='{self.type}', amount={self.amount})"

def calculate_balance_immutable(transactions: List[Transaction]) -> float:
    """
    Oblicza końcowe saldo konta na podstawie listy transakcji,
    zachowując niezmienność.
    """
    # TODO 1: Zdefiniuj funkcję redukującą (accumulator), która będzie przyjmować
    # aktualne saldo (accumulator) i pojedynczą transakcję.
    # Funkcja powinna zwracać nowe saldo.
    def accumulator(current_balance: float, transaction: Transaction) -> float:
        pass

    # TODO 2: Użyj `reduce` do zastosowania funkcji `accumulator` do listy transakcji.
    # Pamiętaj o początkowym saldzie (initial_value).
    initial_balance = 100.0
    final_balance = None
    return final_balance

def categorize_transactions_immutable(transactions: List[Transaction]) -> Dict[str, List[Transaction]]:
    """
    Kategoryzuje transakcje na depozyty i wypłaty, zwracając nową,
    niezmienną strukturę danych.
    """
    # TODO 3: Zdefiniuj funkcję redukującą, która będzie tworzyć słownik
    # z kategoryzowanymi transakcjami.
    # Pamiętaj o niezmienności: zawsze zwracaj nowy słownik/listę.
    def category_reducer(acc: Dict[str, List[Transaction]], transaction: Transaction) -> Dict[str, List[Transaction]]:
        # TODO 4: Wyjaśnij, dlaczego tutaj konieczne jest tworzenie NOWYCH kopii słownika i list.
        # Odpowiedź 4:
        pass

    # TODO 5: Zdefiniuj początkową wartość akumulatora (initial_categories).
    initial_categories = None

    # TODO 6: Użyj `reduce` do kategoryzacji transakcji.
    categorized_data = None
    return categorized_data

if __name__ == "__main__":
    transaction_list = [
        Transaction("deposit", 50.0),
        Transaction("withdrawal", 20.0),
        Transaction("deposit", 100.0),
        Transaction("withdrawal", 30.0),
        Transaction("deposit", 10.0)
    ]

    # TODO 7: Wywołaj calculate_balance_immutable i wydrukuj wynik.
    # final_account_balance = calculate_balance_immutable(transaction_list)
    # print(f"Końcowe saldo konta: {final_account_balance:.2f} zł")

    # TODO 8: Wywołaj categorize_transactions_immutable i wydrukuj wynik.
    # categorized_transactions = categorize_transactions_immutable(transaction_list)
    # print("Kategoryzowane transakcje:")