### Zadanie 1: Prosty Kalkulator z Funkcjami Wyższego Rzędu  

**Cel**: Stwórz elastyczny kalkulator, który nie ma wbudowanych sztywnych operacji (+, -,\*, /), 
ale zamiast tego przyjmuje funkcje jako argumenty. Pomyśl o tym, jak o uniwersalnej 
maszynie, której "mówisz", jaką operację ma wykonać, przekazując jej odpowiednią funkcję. 
Pamiętaj też o bezpiecznym dzieleniu – zwróć specjalną wartość (None), gdy dzielenie przez 
zero jest niemożliwe. To Twoje pierwsze spotkanie z funkcjami wyższego rzędu w praktyce!  

  
### Zadanie 2: Analiza Statystyk Listy Liczb (Funkcyjne Podejście)  

**Cel**: Zoptymalizuj obliczanie statystyk (min, max, suma, średnia) z listy liczb. Zamiast przebiegać przez listę wiele razy (raz dla min, raz dla max itd.), użyj funkcji reduce, aby wykonać wszystkie te obliczenia w jednym, spójnym przejściu. Będziesz musiał stworzyć "akumulator", który zbierze wszystkie dane podczas tej pojedynczej iteracji. Pomyśl o tym jak o jednym, efektywnym procesie, który przetwarza surowe dane w kompleksowy raport.  
  
### Zadanie 3: Filtrowanie i Mapowanie Listy Obiektów 

**Cel**: Naucz się, jak efektywnie przetwarzać listy obiektów, korzystając z tzw. "list 
comprehensions". Twoim zadaniem będzie wybranie konkretnych produktów (filtrowanie) i 
przekształcenie ich w nowy format (mapowanie) – wszystko to w jednej, zwięzłej linii kodu. 
Dodatkowo, zaimplementuj "fabrykę filtrów", czyli funkcję, która tworzy inne funkcje 
filtrujące z dynamicznie ustawianymi kryteriami. To pokaże, jak tworzyć elastyczny i 
możliwy do wielokrotnego użytku kod.  

  
###  Zadanie 4: Kompozycja Funkcji do Przetwarzania Danych  

**Cel**: Poznaj potężne wzorce programowania funkcyjnego: kompozycję funkcji i pipeline. Zbudujesz dwie uniwersalne funkcje (compose i pipeline), które potrafią połączyć wiele małych, prostych funkcji w jedną, bardziej złożoną. Pomyśl o tym, jak o układaniu klocków Lego: z pojedynczych elementów tworzysz skomplikowane konstrukcje, które przetwarzają dane krok po kroku. Różnica będzie w kolejności, w jakiej te klocki są ze sobą łączone.  

  
### Zadanie 5: Zaawansowane Przetwarzanie Kolekcji z reduce i Immutability  

**Cel**: Pogłębij swoją wiedzę o funkcji reduce i zrozum kluczową koncepcję niezmienności (immutability). Będziesz agregować bardziej złożone dane (transakcje bankowe) w salda i kategoryzowane listy. Najważniejsze jest, aby podczas tych operacji nigdy nie modyfikować oryginalnych danych ani pośrednich struktur, lecz zawsze tworzyć nowe kopie. To zadanie pomoże Ci pisać kod, który jest bezpieczniejszy i łatwiejszy do rozumienia w złożonych systemach.