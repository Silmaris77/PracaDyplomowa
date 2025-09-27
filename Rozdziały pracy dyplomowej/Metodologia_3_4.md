## 3.4. Framework Cost-Benefit i Optymalizacja Biznesowa

Tradycyjne podejście do modelowania klasyfikacyjnego, skupione na maksymalizacji metryk technicznych, często zawodzi w realnych zastosowaniach biznesowych, gdzie koszty różnych rodzajów błędów są drastycznie nierówne. W problemie predykcji rotacji pracowników, przeoczenie osoby, która zamierza odejść, jest wielokrotnie bardziej kosztowne niż błędne zidentyfikowanie lojalnego pracownika jako zagrożonego. Niniejsza sekcja opisuje autorski framework analityczny, który stawia tę asymetrię kosztów w centrum procesu decyzyjnego.

### Ustalenie Macierzy Kosztów (Cost Matrix)

Fundamentem podejścia wrażliwego na koszty jest zdefiniowanie macierzy kosztów, która kwantyfikuje finansowe konsekwencje każdego z czterech możliwych wyników predykcji. W niniejszej pracy, po konsultacji z literaturą branżową i standardami rynkowymi, przyjęto następujące założenia:

*   **Prawdziwie Pozytywny (TP - True Positive)**: Model poprawnie przewidział odejście. Koszt to koszt interwencji retencyjnej, która jednak się nie powiodła. Dla uproszczenia przyjmujemy go jako równy kosztowi FP.
*   **Prawdziwie Negatywny (TN - True Negative)**: Model poprawnie przewidział pozostanie pracownika. Koszt jest zerowy.
*   **Fałszywie Pozytywny (FP - False Positive)**: Model błędnie przewidział odejście lojalnego pracownika. Koszt to niepotrzebna interwencja retencyjna.
*   **Fałszywie Negatywny (FN - False Negative)**: Model nie przewidział odejścia pracownika. Jest to najbardziej kosztowny błąd.

#### Kwantyfikacja Kosztów Błędów

1.  **Koszt Fałszywie Negatywnego (FN) = 80 000 PLN**
    Jest to suma szacunkowych kosztów związanych z nieplanowanym wakatem i koniecznością zastąpienia pracownika. Składają się na nią:
    *   **Koszty rekrutacji i selekcji**: Ogłoszenia, czas rekruterów, proces rozmów.
    *   **Koszty wdrożenia (Onboarding)**: Czas menedżera i zespołu, formalne szkolenia.
    *   **Utracona produktywność**: Czas, w którym stanowisko jest nieobsadzone, oraz okres, w którym nowy pracownik osiąga pełną wydajność.
    *   **Utrata wiedzy instytucjonalnej**: Know-how i nieformalne relacje, które odchodzą wraz z pracownikiem.

2.  **Koszt Fałszywie Pozytywnego (FP) = 3 500 PLN**
    Jest to koszt niepotrzebnie uruchomionej interwencji retencyjnej, na który składają się:
    *   **Czas pracy menedżera i HR**: Dodatkowe rozmowy, analizy, przygotowanie planu działania.
    *   **Koszt "miękkich" interwencji**: np. zaoferowanie dodatkowego szkolenia, małego projektu rozwojowego.
    *   *Uwaga: Nie uwzględniono tu kosztu podwyżki, zakładając, że jest ona przyznawana na podstawie oceny wyników, a nie tylko jako narzędzie retencyjne.*

**Asymetria kosztów** jest zatem ogromna i wynosi **80 000 / 3 500 ≈ 22.9:1**. Ignorowanie tej dysproporcji prowadziłoby do fundamentalnie błędnych decyzji biznesowych.

### Procedura Optymalizacji Progu Decyzyjnego (Cost-Sensitive Threshold Optimization)

Standardowo, modele klasyfikacyjne używają progu 0.5 do przypisania obserwacji do klasy pozytywnej. W podejściu wrażliwym na koszty, ten próg staje się parametrem, który należy zoptymalizować. Celem jest znalezienie takiego progu, który minimalizuje **Całkowity Koszt Błędów**.

Procedura optymalizacji, zaimplementowana w tej pracy, przebiega następująco:

1.  **Generowanie Prawdopodobieństw**: Dla każdej obserwacji w zbiorze testowym, wytrenowany model generuje prawdopodobieństwo przynależności do klasy 'Yes' (prawdopodobieństwo odejścia), mieszczące się w zakresie [0, 1].

2.  **Iteracyjne Testowanie Progów**: Definiowany jest zakres możliwych progów do przetestowania (np. 1000 punktów od 0.01 do 0.99).

3.  **Symulacja Decyzji i Obliczanie Kosztu**: Dla każdego progu z zadanego zakresu:
    a. Dokonywana jest symulowana klasyfikacja: jeśli prawdopodobieństwo > próg, pracownik jest klasyfikowany jako 'Yes', w przeciwnym razie jako 'No'.
    b. Na podstawie tej klasyfikacji i rzeczywistych etykiet, zliczana jest liczba błędów FN i FP.
    c. Obliczany jest **Całkowity Koszt Błędów** dla danego progu, używając zdefiniowanej macierzy kosztów.

4.  **Wybór Optymalnego Progu**: Po przetestowaniu wszystkich progów, wybierany jest ten, dla którego Całkowity Koszt Błędów był najniższy.

**Pseudokod procedury:**

```
function find_optimal_threshold(probabilities, true_labels, cost_fn, cost_fp):
    min_cost = infinity
    optimal_threshold = 0.5
    
    for threshold in range(0.01, 1.00, 0.01):
        predictions = (probabilities >= threshold)
        
        FN = count_false_negatives(predictions, true_labels)
        FP = count_false_positives(predictions, true_labels)
        
        total_cost = (FN * cost_fn) + (FP * cost_fp)
        
        if total_cost < min_cost:
            min_cost = total_cost
            optimal_threshold = threshold
            
    return optimal_threshold, min_cost
```

Ten optymalny próg, a nie domyślny 0.5, jest następnie używany do podejmowania ostatecznych decyzji biznesowych i stanowi podstawę do obliczenia realnego zwrotu z inwestycji (ROI) z wdrożenia modelu.

### Analiza Wieloscenariuszowa i Testowanie Wrażliwości

Opisany framework jest elastyczny i pozwala na prowadzenie zaawansowanych analiz strategicznych.

*   **Analiza Wieloscenariuszowa**: Kierownictwo może chcieć przetestować różne scenariusze, np.:
    *   **Scenariusz konserwatywny**: Zaniżone koszty FN i zawyżone koszty FP.
    *   **Scenariusz agresywny**: Zawyżone koszty FN i zaniżone koszty FP.
    Uruchomienie procedury optymalizacyjnej dla różnych macierzy kosztów pozwala zobaczyć, jak zmienia się optymalna strategia działania.

*   **Testowanie Wrażliwości**: Można również zbadać, jak bardzo zmienia się optymalny próg decyzyjny w odpowiedzi na niewielkie zmiany w szacunkach kosztów. Jeśli próg jest stabilny w szerokim zakresie założeń, rekomendacje biznesowe są bardziej wiarygodne.

Zastosowanie tego kompleksowego frameworku analitycznego przesuwa punkt ciężkości z czysto technicznej predykcji w stronę strategicznego narzędzia wspomagającego podejmowanie decyzji, które jest w pełni świadome ich finansowych konsekwencji. To właśnie ten krok stanowi o unikalności i praktycznej wartości niniejszej pracy.