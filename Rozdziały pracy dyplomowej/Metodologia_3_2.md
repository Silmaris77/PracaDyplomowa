## 3.2. Proces Przetwarzania Danych (Preprocessing)

Surowe dane, nawet te wysokiej jakości, rzadko kiedy nadają się bezpośrednio do modelowania. Proces przygotowania danych, znany jako preprocessing, jest kluczowym etapem, który transformuje dane wejściowe do formatu optymalnego dla algorytmów uczenia maszynowego. Celem tego etapu jest nie tylko "wyczyszczenie" danych, ale również wzbogacenie ich o nowe, bardziej informacyjne cechy, co jest fundamentem dla skutecznej inżynierii cech.

### Wstępne Czyszczenie Danych

Jak stwierdzono w sekcji 3.1, zbiór danych był kompletny i nie zawierał duplikatów. Pierwszym krokiem było zatem usunięcie zmiennych, które nie niosły żadnej wartości predykcyjnej:
-   **Zmienne o zerowej wariancji**: `EmployeeCount`, `StandardHours`, `Over18`.
-   **Unikalny identyfikator**: `EmployeeNumber`.

Po usunięciu tych czterech kolumn, do dalszej analizy pozostało 31 zmiennych, które mogły potencjalnie służyć jako predyktory.

### Kodowanie Zmiennych Kategorycznych (Encoding)

Algorytmy uczenia maszynowego operują na liczbach, dlatego konieczne było przekształcenie wszystkich zmiennych nienumerycznych. Zastosowano dwie różne strategie w zależności od natury zmiennej.

#### Zmienne Porządkowe (Ordinal Variables)

Zmienne porządkowe to takie, których kategorie mają naturalną, wewnętrzną hierarchię (np. "niski", "średni", "wysoki"). W ich przypadku zastosowano **kodowanie ręczne (manual mapping)**, aby zachować tę ważną informację.

**Przykłady mapowania:**
-   `JobSatisfaction`: {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'} -> {1, 2, 3, 4}
-   `PerformanceRating`: {1: 'Low', 2: 'Good', 3: 'Excellent', 4: 'Outstanding'} -> {1, 2, 3, 4}
-   `WorkLifeBalance`: {1: 'Bad', 2: 'Good', 3: 'Better', 4: 'Best'} -> {1, 2, 3, 4}

Takie podejście zapewnia, że model "rozumie", iż różnica między satysfakcją na poziomie 1 i 2 jest taka sama jak między 3 i 4.

#### Zmienne Nominalne (Nominal Variables)

Zmienne nominalne to takie, których kategorie nie mają żadnej wewnętrznej kolejności (np. `Department`, `MaritalStatus`). Zastosowanie prostego kodowania numerycznego (np. 1, 2, 3) wprowadziłoby sztuczną hierarchię, której nie ma w danych. Aby tego uniknąć, zastosowano technikę **One-Hot Encoding**.

Technika ta tworzy nową, binarną kolumnę (0 lub 1) dla każdej unikalnej kategorii w oryginalnej zmiennej. Na przykład, zmienna `MaritalStatus` z kategoriami 'Single', 'Married', 'Divorced' została przekształcona w trzy nowe kolumny: `MaritalStatus_Single`, `MaritalStatus_Married`, `MaritalStatus_Divorced`.

### Skalowanie Zmiennych Numerycznych (Scaling)

Zmienne numeryczne w zbiorze danych miały bardzo różne zakresy (np. `Age` od 18 do 60, a `MonthlyIncome` od 1009 do 19999). Algorytmy wrażliwe na odległość, takie jak Regresja Logistyczna czy SVM, mogą przypisywać większą wagę zmiennym o większych wartościach bezwzględnych. Aby temu zapobiec, wszystkie zmienne numeryczne zostały poddane **standaryzacji** przy użyciu `StandardScaler` z biblioteki `scikit-learn`.

Standaryzacja przekształca każdą zmienną w taki sposób, aby jej rozkład miał **średnią równą 0 i odchylenie standardowe równe 1**.

### Zaawansowana Inżynieria Cech (Advanced Feature Engineering)

To najważniejszy etap preprocessingu, w którym na podstawie istniejących danych tworzone są nowe, potencjalnie bardziej informacyjne cechy. Celem jest dostarczenie modelowi zmiennych, które lepiej oddają kontekst biznesowy i ukryte zależności. W ramach tego procesu, z początkowych 31 predyktorów, stworzono dodatkowe cechy, co doprowadziło do finalnego zbioru **42 zmiennych** użytych w modelowaniu.

**Przykłady stworzonych cech:**
-   `MeanSatisfaction`: Średnia z czterech wskaźników satysfakcji (`JobSatisfaction`, `EnvironmentSatisfaction`, `RelationshipSatisfaction`, `WorkLifeBalance`). Agreguje ogólne zadowolenie pracownika.
-   `YearsPerRole`: Stosunek całkowitego stażu w firmie (`YearsAtCompany`) do liczby lat na obecnym stanowisku (`YearsInCurrentRole`). Wysoka wartość może wskazywać na stagnację.
-   `PromotionGap`: Różnica między stażem pracy a czasem od ostatniego awansu (`YearsAtCompany` - `YearsSinceLastPromotion`). Może sygnalizować brak rozwoju.
-   `IncomeToAgeRatio`: Stosunek miesięcznego dochodu do wieku pracownika. Może być wskaźnikiem dopasowania zarobków do etapu kariery.
-   `IsSingle`: Uproszczona, binarna wersja zmiennej `MaritalStatus`, która przyjmuje wartość 1, jeśli pracownik jest stanu wolnego, i 0 w przeciwnym razie.

Ten krok był kluczowy dla osiągnięcia wysokiej wydajności przez prostsze modele, takie jak Regresja Logistyczna, które same w sobie nie potrafią modelować złożonych interakcji między zmiennymi.

### Podział Danych na Zbiory Treningowy i Testowy

Po zakończeniu wszystkich transformacji, finalny zbiór danych został podzielony na dwa podzbiory:
-   **Zbiór treningowy (80% danych)**: Używany do trenowania modeli i strojenia hiperparametrów (poprzez walidację krzyżową).
-   **Zbiór testowy (20% danych)**: Używany do ostatecznej, jednorazowej oceny wydajności wytrenowanych modeli. Zbiór ten był "nietykalny" podczas całego procesu budowy modelu.

Podział został przeprowadzony z użyciem **stratyfikacji** względem zmiennej celu `Attrition`. Oznacza to, że w obu zbiorach (treningowym i testowym) zachowano ten sam odsetek (16.3%) pracowników, którzy odeszli, co zapewnia rzetelną ocenę.