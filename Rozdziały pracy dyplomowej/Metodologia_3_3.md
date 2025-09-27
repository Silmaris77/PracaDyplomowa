## 3.3. Modelowanie i Ewaluacja

Po starannym przygotowaniu i przetworzeniu danych, kolejnym krokiem jest właściwy proces modelowania predykcyjnego. Etap ten obejmuje wybór i trening algorytmów, ich optymalizację oraz, co kluczowe, zdefiniowanie metryk, które posłużą do oceny ich wydajności zarówno pod kątem technicznym, jak i biznesowym. W tej sekcji opisano systematyczne podejście zastosowane w niniejszej pracy.

### Przegląd Porównywanych Algorytmów

Jak uzasadniono w rozdziale 2.4, do analizy wybrano cztery algorytmy reprezentujące różne rodziny modeli uczenia maszynowego, co pozwala na kompleksowe porównanie ich skuteczności w problemie predykcji rotacji:
1.  **Regresja Logistyczna** (model liniowy)
2.  **Maszyny Wektorów Nośnych (SVM)** (model oparty na marginesie)
3.  **Lasy Losowe (Random Forest)** (model zespołowy typu bagging)
4.  **XGBoost** (model zespołowy typu boosting)

### Strategia Walidacji i Optymalizacji Modeli

W celu zapewnienia rzetelności wyników i uniknięcia przeuczenia (overfitting), zastosowano wieloetapową strategię walidacji i optymalizacji.

1.  **Walidacja Krzyżowa (Cross-Validation)**: Cały proces treningu i optymalizacji odbywał się wyłącznie na zbiorze treningowym. Zastosowano **5-krotną walidację krzyżową (5-fold Cross-Validation)**. Zbiór treningowy był dzielony na 5 równych części. Model był trenowany 5 razy, za każdym razem na 4 częściach, a walidowany na pozostałej jednej. Uśredniony wynik z tych 5 "przebiegów" dawał stabilną i wiarygodną ocenę wydajności modelu.

2.  **Strojenie Hiperparametrów (Hyperparameter Tuning)**: Każdy z algorytmów posiada zestaw hiperparametrów, które sterują jego działaniem (np. siła regularyzacji w regresji logistycznej, liczba drzew w lesie losowym). W celu znalezienia ich optymalnej kombinacji, wykorzystano metodę **`GridSearchCV`** z biblioteki `scikit-learn`. Metoda ta, w połączeniu z walidacją krzyżową, systematycznie testowała różne kombinacje hiperparametrów, wybierając tę, która dawała najlepszy uśredniony wynik (w tym przypadku najwyższą metrykę AUC-ROC).

3.  **Finalna Ewaluacja na Zbiorze Testowym**: Po znalezieniu najlepszych hiperparametrów, każdy z modeli został ostatecznie wytrenowany na *całym* zbiorze treningowym, a następnie jego wydajność została jednorazowo zmierzona na odłożonym na bok **zbiorze testowym**. Wyniki uzyskane na tym zbiorze są ostatecznym, raportowanym wskaźnikiem wydajności modeli.

### Metryki Ewaluacji Modeli

Wybór odpowiednich metryk jest kluczowy, zwłaszcza w problemie z niezbalansowanymi klasami. W niniejszej pracy zastosowano dwupoziomowy system metryk: standardowe metryki klasyfikacji oraz metryki zorientowane na koszt biznesowy.

#### Standardowe Metryki Klasyfikacji

*   **AUC-ROC (Area Under the Receiver Operating Characteristic Curve)**: Główna metryka używana do porównywania ogólnej mocy dyskryminacyjnej modeli. Mierzy zdolność modelu do odróżniania klasy pozytywnej od negatywnej, niezależnie od wybranego progu decyzyjnego. Wartość AUC od 0.5 oznacza model losowy, a 1.0 model idealny.
*   **Precyzja (Precision)**: Odsetek pozytywnych predykcji, które były poprawne. Odpowiada na pytanie: "Jaki procent pracowników, których oznaczyliśmy jako zagrożonych odejściem, faktycznie odszedł?".
*   **Czułość (Recall / Sensitivity)**: Odsetek wszystkich pozytywnych przypadków, które model poprawnie zidentyfikował. Odpowiada na pytanie: "Jaki procent pracowników, którzy faktycznie odeszli, udało nam się poprawnie wytypować?".
*   **F1-Score**: Średnia harmoniczna precyzji i czułości. Jest to użyteczna, zagregowana metryka, która równoważy oba te wskaźniki.

#### Metryki Biznesowe i Wrażliwe na Koszty

Sercem tej pracy jest ocena modeli z perspektywy biznesowej. W tym celu zdefiniowano kluczową metrykę: **Całkowity Koszt Błędów**, opartą na macierzy kosztów przedstawionej w sekcji 3.4.

**Całkowity Koszt Błędów = (Liczba FN × 80 000 PLN) + (Liczba FP × 3 500 PLN)**

Gdzie:
-   **FN (False Negative)**: Liczba pracowników, którzy odeszli, a model tego nie przewidział.
-   **FP (False Positive)**: Liczba pracowników, którzy nie odeszli, ale model błędnie oznaczył ich jako zagrożonych.

Ta metryka była podstawą do przeprowadzenia optymalizacji progu decyzyjnego i finalnej oceny, który model generuje największą wartość dla organizacji.

### Analiza Interpretowalności Modeli (Explainable AI - XAI)

Zrozumienie, dlaczego model podejmuje takie, a nie inne decyzje, jest równie ważne, co jego wydajność predykcyjna. W celu zapewnienia interpretowalności, zastosowano dwie techniki:

1.  **Ważność Cech (Global Feature Importance)**: Wykorzystano wbudowane w modele mechanizmy (np. współczynniki `coef_` w regresji logistycznej, atrybut `feature_importances_` w modelach drzewiastych) do stworzenia globalnego rankingu cech, które miały największy wpływ na predykcje.

2.  **Analiza z Użyciem SHAP (SHapley Additive exPlanations)**: Aby uzyskać głębszy i bardziej zunifikowany wgląd, zastosowano bibliotekę SHAP. Jest to zaawansowana technika oparta na teorii gier, która pozwala na:
    *   **Globalną interpretację**: Agregując wartości SHAP dla wszystkich obserwacji, można uzyskać spójny ranking ważności cech, który jest porównywalny między różnymi modelami.
    *   **Lokalną interpretację**: Co najważniejsze, SHAP pozwala wyjaśnić każdą pojedynczą predykcję, pokazując, które cechy i w jakim stopniu "pchnęły" prognozę w kierunku odejścia lub pozostania dla konkretnego pracownika. Jest to kluczowe dla budowania zaufania do modelu i podejmowania świadomych działań HR.

Tak skonstruowany proces modelowania i ewaluacji zapewnia nie tylko rzetelne porównanie algorytmów, ale także głęboki wgląd w ich działanie i, co najważniejsze, bezpośrednie przełożenie wyników na mierzalną wartość biznesową.