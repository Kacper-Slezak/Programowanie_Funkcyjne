from typing import Callable, List

# Zadanie 3: Filtrowanie i Mapowanie Listy Obiektów
# Cel: Mając listę obiektów 'Product', filtruj te, które spełniają warunek,
# a następnie przekształć je w inną formę, używając 'list comprehensions'.
# Zadbaj o niezmienność. Dodatkowo, wprowadź funkcję do tworzenia dynamicznych filtrów.

class Product:
    def __init__(self, name: str, price: float, in_stock: bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, in_stock={self.in_stock})"

def process_products(products: List[Product]) -> List[str]:
    """
    Filtruje produkty i zwraca listę ich nazw w formacie "Nazwa (Cena zł)"
    dla produktów dostępnych i droższych niż 50.
    """
    # TODO 1: Użyj list comprehension do przefiltrowania produktów,
    # które są "in_stock" (dostępne) ORAZ ich cena jest wyższa niż 50.0.
    # Następnie przekształć je w stringi w formacie "Nazwa (Cena zł)".
    # Wynik powinien być nową listą, nie modyfikując oryginalnej (zasada niezmienności).
    filtered_and_mapped_products = []
    return filtered_and_mapped_products

# TODO 2: Zaimplementuj funkcję 'create_price_filter', która przyjmuje minimalną cenę
# i zwraca inną funkcję, która będzie filtrować produkty na podstawie tej ceny.
def create_price_filter(min_price: float) -> Callable[[Product], bool]:
    pass

if __name__ == "__main__":
    products_list = [
        Product("Laptop", 1200.0, True),
        Product("Myszka", 25.0, True),
        Product("Klawiatura", 75.0, False),
        Product("Monitor", 300.0, True),
        Product("Kamera", 50.0, False),
        Product("Słuchawki", 120.0, True)
    ]

    # TODO 3: Wywołaj 'process_products' i wydrukuj wyniki.
    # processed_names = process_products(products_list)
    # print("Dostępne produkty (powyżej 50 zł):")

    # TODO 4: Użyj 'create_price_filter' do stworzenia dynamicznych filtrów
    # i zastosuj je do listy produktów.
    # filter_above_100 = create_price_filter(100.0)
    # high_value_products = [p for p in products_list if p.in_stock and filter_above_100(p)]
    # print(f"Produkty dostępne i droższe niż 100 zł: {high_value_products}")