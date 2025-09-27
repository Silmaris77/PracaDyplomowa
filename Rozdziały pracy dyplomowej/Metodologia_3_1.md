## 3.1. Charakterystyka Danych Źródłowych

Podstawą każdej analizy data science jest zbiór danych. Jego jakość, struktura i trafność determinują potencjalną wartość i wiarygodność uzyskanych wyników. W niniejszym rozdziale szczegółowo scharakteryzowano zbiór danych wykorzystany do budowy i ewaluacji modeli predykcyjnych, omawiając jego pochodzenie, strukturę, zmienną celu oraz wstępną ocenę jakości i aspekty etyczne.

### Źródło i Ogólna Charakterystyka Zbioru Danych

Badanie zostało przeprowadzone na publicznie dostępnym zbiorze danych **"IBM HR Analytics Employee Attrition & Performance"**. Został on stworzony przez analityków danych z firmy IBM i udostępniony na platformie Kaggle w celu promowania badań i rozwoju w obszarze analityki HR. Jest to jeden z najpopularniejszych i najczęściej cytowanych zbiorów danych w tej dziedzinie, stanowiący standardowy benchmark dla modeli predykcji rotacji.

Kluczową cechą tego zbioru jest fakt, że są to **dane fikcyjne**, wygenerowane w celu naśladowania realnych wyzwań analitycznych w obszarze HR, bez naruszania prywatności prawdziwych pracowników. Dzięki temu możliwe jest prowadzenie zaawansowanych analiz bez konieczności przechodzenia przez skomplikowane i restrykcyjne procedury związane z przetwarzaniem danych wrażliwych.

### Struktura i Zawartość Zbioru Danych

Oryginalny zbiór danych ma postać tabelaryczną i składa się z **1470 obserwacji**, z których każda reprezentuje jednego, unikalnego pracownika. Każdy pracownik jest opisany za pomocą **35 zmiennych (cech)**, obejmujących szerokie spektrum informacji demograficznych, behawioralnych i organizacyjnych.

Zmienne w zbiorze można podzielić na kilka kategorii:

*   **Dane demograficzne**: `Age`, `Gender`, `MaritalStatus`.
*   **Dane dotyczące roli w organizacji**: `JobRole`, `JobLevel`, `Department`.
*   **Dane dotyczące wynagrodzenia i benefitów**: `MonthlyIncome`, `PercentSalaryHike`, `StockOptionLevel`.
*   **Dane dotyczące satysfakcji i zaangażowania**: `JobSatisfaction`, `EnvironmentSatisfaction`, `RelationshipSatisfaction`, `WorkLifeBalance`.
*   **Dane dotyczące historii zatrudnienia i wydajności**: `YearsAtCompany`, `YearsInCurrentRole`, `YearsSinceLastPromotion`, `PerformanceRating`.
*   **Dane behawioralne**: `OverTime`, `BusinessTravel`, `DistanceFromHome`.

Taka różnorodność cech pozwala na budowę modeli, które mogą uchwycić złożone, wielowymiarowe przyczyny decyzji o odejściu z pracy.

### Zmienna Celu (`Attrition`) i Problem Niezbalansowania Klas

Centralnym punktem analizy jest zmienna celu – `Attrition`. Jest to zmienna binarna, która przyjmuje jedną z dwóch wartości:
*   **'Yes'**: Pracownik odszedł z firmy (klasa pozytywna/mniejszościowa).
*   **'No'**: Pracownik pozostał w firmie (klasa negatywna/większościowa).

Analiza rozkładu tej zmiennej ujawnia fundamentalne wyzwanie metodologiczne, charakterystyczne dla problemów predykcji rotacji: **silne niezbalansowanie klas**.

*   Liczba pracowników, którzy odeszli (`Attrition` = 'Yes'): **237**
*   Liczba pracowników, którzy zostali (`Attrition` = 'No'): **1233**

Oznacza to, że klasa pozytywna (pracownicy, których chcemy zidentyfikować) stanowi zaledwie **16.3%** wszystkich obserwacji.

**Implikacje niezbalansowania klas:**
1.  **Problem z metrykami**: Standardowa metryka dokładności (accuracy) staje się myląca. Model, który zawsze przewidywałby, że nikt nie odejdzie, osiągnąłby dokładność na poziomie 83.7%, mimo że byłby całkowicie bezużyteczny z biznesowego punktu widzenia.
2.  **Tendencja modeli do ignorowania klasy mniejszościowej**: Wiele algorytmów, dążąc do minimalizacji ogólnego błędu, może nauczyć się ignorować rzadką klasę pozytywną, ponieważ "opłaca się" im koncentrować na poprawnej klasyfikacji dominującej grupy.
3.  **Konieczność stosowania specjalistycznych technik**: Problem ten wymusza zastosowanie zaawansowanych technik, takich jak metody próbkowania (oversampling/undersampling), ważenie klas czy – co jest centralnym punktem tej pracy – optymalizacja progu decyzyjnego w podejściu wrażliwym na koszty.

### Wstępna Ocena Jakości Danych (Data Quality Assessment)

Przed przystąpieniem do właściwego modelowania, przeprowadzono podstawową ocenę jakości danych w celu zidentyfikowania potencjalnych problemów, które mogłyby wpłynąć na wyniki analizy.

1.  **Brakujące wartości (Missing Values)**: Przeprowadzono analizę kompletności danych dla wszystkich 35 zmiennych. Stwierdzono, że zbiór danych jest **w 100% kompletny** – nie zidentyfikowano żadnych brakujących wartości. Jest to cecha charakterystyczna dla przygotowanych, "czystych" zbiorów danych i upraszcza fazę preprocessingu.

2.  **Duplikaty (Duplicate Records)**: Sprawdzono, czy w zbiorze istnieją zduplikowane wiersze (reprezentujące tych samych pracowników). Nie znaleziono żadnych duplikatów.

3.  **Zmienne o zerowej wariancji (Constant Columns)**: Zidentyfikowano trzy zmienne, które miały taką samą wartość dla wszystkich 1470 pracowników:
    *   `EmployeeCount`: zawsze 1.
    *   `StandardHours`: zawsze 80.
    *   `Over18`: zawsze 'Y'.
    Zmienne te nie niosą żadnej informacji predykcyjnej (mają zerową wariancję) i zostały usunięte ze zbioru danych na wczesnym etapie przetwarzania.

4.  **Unikalne identyfikatory**: Zmienna `EmployeeNumber` jest unikalnym identyfikatorem dla każdego pracownika. Jako taka, nie ma wartości predykcyjnej i również została usunięta z puli cech używanych do modelowania.

Wstępna ocena wykazała, że zbiór danych jest wysokiej jakości, co pozwala skoncentrować się na bardziej zaawansowanych etapach analizy, takich jak inżynieria cech i optymalizacja modeli, zamiast na podstawowym czyszczeniu danych.

### Aspekty Etyczne i Ograniczenia Zbioru Danych

Wykorzystanie fikcyjnego zbioru danych ma kluczowe znaczenie z perspektywy etycznej. Pozwala na uniknięcie fundamentalnych problemów związanych z prywatnością, zgodą na przetwarzanie danych i potencjalną dyskryminacją, które zostały szerzej omówione w rozdziale 2.3.

Należy jednak pamiętać o ograniczeniach takiego podejścia:
*   **Uproszczenie rzeczywistości**: Dane syntetyczne, mimo że dobrze zaprojektowane, mogą nie oddawać w pełni złożoności i "szumu" charakterystycznego dla realnych danych HR.
*   **Generalizowalność**: Model zbudowany na tych danych może wymagać dodatkowej kalibracji i walidacji przed wdrożeniem w konkretnej organizacji, która ma swoją unikalną specyfikę.

Mimo tych ograniczeń, zbiór "IBM HR Analytics" stanowi doskonałe i bezpieczne środowisko do rozwoju i testowania metodologii analitycznych, które następnie mogą być adaptowane do rzeczywistych problemów biznesowych, z uwzględnieniem wszystkich wymogów prawnych i etycznych.