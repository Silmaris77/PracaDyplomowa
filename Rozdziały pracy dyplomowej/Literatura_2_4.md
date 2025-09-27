## 2.4. Przegląd i Benchmark Algorytmów ML w Klasyfikacji HR

Wybór odpowiednich algorytmów uczenia maszynowego jest kluczowym etapem w procesie budowy skutecznego modelu predykcyjnego. W kontekście predykcji rotacji pracowników, gdzie celem jest nie tylko dokładność, ale przede wszystkim wartość biznesowa, selekcja modeli musi być podyktowana ich charakterystyką, zdolnością do adaptacji do problemów biznesowych oraz pozycją w branżowych i akademickich benchmarkach. Niniejszy rozdział przedstawia przegląd wybranych algorytmów, uzasadnia ich dobór do analizy w tej pracy oraz omawia standardy rynkowe i metodologiczne w podejściach zorientowanych na koszt.

### Uzasadnienie Doboru Algorytmów

Selekcja algorytmów do niniejszej pracy nie była przypadkowa. Opierała się na strategii mającej na celu pokrycie szerokiego spektrum metodologicznego, od prostych i interpretowalnych modeli stanowiących punkt odniesienia, po złożone, najnowocześniejsze algorytmy znane z wysokiej skuteczności na danych tabelarycznych. Taki dobór pozwala na kompleksowe porównanie i weryfikację hipotez badawczych.

**Kryteria doboru algorytmów:**

1.  **Interpretowalność vs. Wydajność (Interpretability vs. Performance Trade-off)**: Zestawiono modele transparentne, których działanie jest łatwe do zrozumienia dla interesariuszy biznesowych (np. Regresja Logistyczna), z modelami typu "czarna skrzynka", które oferują najwyższą moc predykcyjną (np. XGBoost). Pozwala to na ocenę, jaki jest "koszt" utraty interpretowalności w zamian za wzrost wydajności.

2.  **Różnorodność Metodologiczna**: Wybrano algorytmy reprezentujące różne rodziny modeli, aby uniknąć ograniczenia do jednej klasy rozwiązań:
    *   **Modele Liniowe** (Regresja Logistyczna): Zakładają liniową zależność między cechami a logarytmem szansy wystąpienia zdarzenia.
    *   **Modele Oparte na Odległości/Marginesie** (Maszyny Wektorów Nośnych - SVM): Poszukują hiperpłaszczyzny optymalnie separującej klasy.
    *   **Modele Drzewiaste i Zespołowe (Ensemble)**:
        *   **Bagging** (Random Forest): Budują wiele modeli równolegle na losowych podpróbkach danych i cech, a następnie uśredniają ich wyniki, co redukuje wariancję i overfitting.
        *   **Boosting** (XGBoost): Budują modele sekwencyjnie, gdzie każdy kolejny model koryguje błędy poprzednika, co prowadzi do wysokiej skuteczności.

3.  **Zdolność do Adaptacji Kosztowej**: Kluczowym kryterium była możliwość łatwej adaptacji algorytmu do uczenia wrażliwego na koszty. Wybrane modele (np. z biblioteki `scikit-learn`) często posiadają wbudowane parametry, takie jak `class_weight`, lub mogą być łatwo zintegrowane z podejściami modyfikującymi próg decyzyjny.

4.  **Standardy Branżowe i Akademickie**: Selekcja objęła algorytmy, które są powszechnie uznawane za "złoty standard" w problemach klasyfikacyjnych na danych tabelarycznych i często pojawiają się w literaturze naukowej dotyczącej people analytics.

Dzięki takiemu podejściu, analiza porównawcza w tej pracy nie jest jedynie rankingiem algorytmów, ale strategicznym badaniem, który rodzaj modelu najlepiej odpowiada na specyficzne wyzwania predykcji rotacji w kontekście optymalizacji biznesowej.

### Omówienie Wybranych Modeli

#### **1. Regresja Logistyczna (Logistic Regression)**

*   **Charakterystyka**: Jest to fundamentalny algorym klasyfikacyjny, który modeluje prawdopodobieństwo przynależności do danej klasy za pomocą funkcji logistycznej. Mimo swojej prostoty, jest niezwykle użyteczny.
*   **Uzasadnienie wyboru**:
    *   **Doskonały model bazowy (Baseline)**: Stanowi punkt odniesienia, z którym porównywane są bardziej złożone modele. Jeśli zaawansowane algorytmy nie są w stanie znacząco pobić regresji logistycznej, ich wdrożenie może być nieuzasadnione.
    *   **Wysoka interpretowalność**: Współczynniki modelu bezpośrednio wskazują na siłę i kierunek wpływu każdej cechy na prawdopodobieństwo rotacji, co jest niezwykle cenne dla interesariuszy biznesowych.
    *   **Niski koszt obliczeniowy**: Jest szybka w treningu i predykcji.
    *   **Odporność na przeuczenie**: Dzięki technikom regularyzacji (L1, L2) jest mniej podatna na overfitting niż złożone modele.

#### **2. Maszyny Wektorów Nośnych (Support Vector Machines - SVM)**

*   **Charakterystyka**: SVM to algorytm, który dąży do znalezienia optymalnej hiperpłaszczyzny separującej punkty danych należące do różnych klas w wielowymiarowej przestrzeni. Dzięki "sztuczce z jądrem" (kernel trick), potrafi efektywnie modelować nieliniowe zależności.
*   **Uzasadnienie wyboru**:
    *   **Zdolność do modelowania nieliniowości**: W przeciwieństwie do regresji logistycznej, SVM z jądrem (np. RBF) może uchwycić skomplikowane, nieliniowe wzorce w danych.
    *   **Efektywność w przestrzeniach wysokowymiarowych**: Dobrze radzi sobie w sytuacji, gdy liczba cech jest duża, co często ma miejsce po procesie *feature engineering*.
    *   **Inne podejście do separacji klas**: Reprezentuje klasę modeli opartych na marginesie, co stanowi cenne uzupełnienie dla modeli probabilistycznych i drzewiastych.

#### **3. Lasy Losowe (Random Forest)**

*   **Charakterystyka**: Jest to algorytm zespołowy (ensemble) typu *bagging*. Trenuje dużą liczbę drzew decyzyjnych na losowych podpróbkach danych i cech, a następnie agreguje ich predykcje (przez głosowanie).
*   **Uzasadnienie wyboru**:
    *   **Wysoka wydajność i odporność**: Jest to jeden z najbardziej niezawodnych i uniwersalnych algorytmów. Zazwyczaj osiąga wysoką skuteczność bez potrzeby intensywnego strojenia hiperparametrów.
    *   **Redukcja overfittingu**: Dzięki agregacji wielu drzew, lasy losowe są znacznie bardziej odporne na przeuczenie niż pojedyncze drzewo decyzyjne.
    *   **Wbudowana ważność cech**: Algorytm naturalnie dostarcza metryki ważności cech, co wspiera interpretowalność.
    *   **Obsługa różnych typów danych**: Dobrze radzi sobie zarówno ze zmiennymi numerycznymi, jak i kategorycznymi, i nie wymaga skalowania cech.

#### **4. XGBoost (Extreme Gradient Boosting)**

*   **Charakterystyka**: Jest to zaawansowana implementacja algorytmu *gradient boosting*. Buduje drzewa decyzyjne w sposób sekwencyjny – każde kolejne drzewo jest trenowane tak, aby korygować błędy popełnione przez poprzednie.
*   **Uzasadnienie wyboru**:
    *   **Najwyższa wydajność (State-of-the-Art)**: XGBoost jest powszechnie uznawany za jeden z najskuteczniejszych algorytmów dla danych tabelarycznych, regularnie wygrywając zawody na platformach takich jak Kaggle.
    *   **Zoptymalizowana implementacja**: Zawiera wbudowaną regularyzację, obsługę brakujących danych i techniki optymalizacyjne (np. przetwarzanie równoległe), co czyni go szybkim i skutecznym.
    *   **Reprezentacja metodyki boostingowej**: Uzupełnia lasy losowe (bagging) o przedstawiciela drugiej głównej rodziny modeli zespołowych (boosting), co pozwala na pełne porównanie tych dwóch podejść.

### Standardy Rynkowe i Międzynarodowe Benchmarki

Analiza literatury naukowej i raportów branżowych dotyczących predykcji rotacji pracowników pozwala na ustalenie pewnych standardów wydajności.
- **Typowa wydajność modeli**: W większości publikacji, dobrze zaimplementowane modele predykcyjne osiągają wartość metryki **AUC (Area Under the ROC Curve) w przedziale 0.75 - 0.85**. Wyniki poniżej 0.75 są często uznawane za niewystarczające, a wyniki powyżej 0.85 za bardzo dobre. W kontekście niniejszej pracy, osiągnięcie przez najlepszy model (Regresja Logistyczna) **AUC na poziomie 0.8275** plasuje uzyskane wyniki w górnej części typowego zakresu, co świadczy o wysokiej jakości modelu.
- **Kluczowe predyktory**: Międzynarodowe badania konsekwentnie wskazują na podobne grupy czynników jako kluczowe predyktory rotacji. Należą do nich m.in. satysfakcja z pracy, poziom wynagrodzenia, liczba nadgodzin, staż pracy w firmie oraz wiek. Zgodność najważniejszych cech zidentyfikowanych w tej pracy z literaturą światową dodatkowo waliduje uzyskane wyniki.

### Podejścia Wrażliwe na Koszty (Cost-Sensitive) vs. Zorientowane na Dokładność (Accuracy-Oriented)

Tradycyjne podejście do klasyfikacji koncentruje się na maksymalizacji metryk takich jak dokładność (accuracy), precyzja czy F1-score. Takie podejście jest "ślepe" na koszty biznesowe i zakłada, że wszystkie błędy są tak samo kosztowne. W problemie predykcji rotacji jest to fundamentalnie błędne założenie:
- **Błąd Fałszywie Negatywny (FN)**: Model nie przewidział odejścia pracownika, który faktycznie odszedł. **Koszt jest bardzo wysoki** (koszty rekrutacji, wdrożenia nowego pracownika, utraconej produktywności, etc. – w tej pracy przyjęto **80 000 PLN**).
- **Błąd Fałszywie Pozytywny (FP)**: Model błędnie oznaczył lojalnego pracownika jako zagrożonego odejściem, co uruchomiło niepotrzebną interwencję retencyjną. **Koszt jest relatywnie niski** (czas menedżera, ewentualny mały bonus – w tej pracy przyjęto **3 500 PLN**).

Ze względu na tę asymetrię kosztów, podejścia zorientowane na dokładność są suboptymalne. Literatura przedmiotu i praktyka biznesowa coraz częściej skłaniają się ku metodom wrażliwym na koszty.

**Techniki wprowadzania wrażliwości na koszty:**

1.  **Na poziomie danych (Data-level approach)**:
    *   **Próbkowanie (Sampling)**: Modyfikacja zbioru treningowego w celu zrównoważenia klas.
        *   *Oversampling* (np. algorytm SMOTE): Syntetyczne tworzenie nowych przykładów klasy mniejszościowej (odchodzących).
        *   *Undersampling*: Losowe usuwanie przykładów z klasy większościowej (pozostających).
    *   **Ważenie przykładów (Instance Weighting)**: Przypisanie większej wagi do obserwacji z klasy mniejszościowej podczas treningu modelu.

2.  **Na poziomie algorytmu (Algorithm-level approach)**:
    *   **Modyfikacja funkcji kosztu**: Wiele algorytmów (w tym te używane w `scikit-learn`) pozwala na bezpośrednie zdefiniowanie wag dla klas (parametr `class_weight='balanced'`), co powoduje, że błędy na klasie mniejszościowej są "karane" mocniej.
    *   **Specjalistyczne algorytmy**: Istnieją algorytmy zaprojektowane od podstaw z myślą o nierównych kosztach (np. Cost-Sensitive Decision Trees).

3.  **Na poziomie progu decyzyjnego (Threshold-level approach)**:
    *   **Optymalizacja progu (Threshold Moving)**: Jest to najbardziej elastyczna i interpretowalna metoda, zastosowana jako główna w tej pracy. Zamiast używać domyślnego progu 0.5, model zwraca prawdopodobieństwo przynależności do klasy, a następnie analitycznie wyszukiwany jest taki próg, który minimalizuje całkowity koszt biznesowy. Ta technika pozwala na bezpośrednie włączenie macierzy kosztów do procesu decyzyjnego bez modyfikacji samego algorytmu.

Badania porównawcze (np. Martens & Provost, 2014) dowodzą, że zastosowanie metod wrażliwych na koszty, a w szczególności optymalizacji progu decyzyjnego, prowadzi do znacznej redukcji całkowitych kosztów biznesowych, nawet jeśli metryki takie jak dokładność (accuracy) ulegają nieznacznemu pogorszeniu. Potwierdza to główną hipotezę niniejszej pracy i uzasadnia wybór tej metodologii jako centralnego punktu analizy.