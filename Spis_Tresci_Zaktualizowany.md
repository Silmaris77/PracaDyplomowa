# 📋 **SPIS TREŚCI PRACY DYPLOMOWEJ**
# **Predykcja Rotacji Pracowników z wykorzystaniem Machine Learning**

---

## **ABSTRACT / STRESZCZENIE**

## **1. WPROWADZENIE**
- **1.1** Uzasadnienie wyboru tematu
  - 1.1.1 Znaczenie problemu rotacji pracowników w współczesnych organizacjach
  - 1.1.2 Koszty rotacji pracowników - analiza ekonomiczna  
  - 1.1.3 Potencjał technologii i machine learning w HR
  - 1.1.4 Innowacyjne podejście do feature engineering w HR Analytics
  - 1.1.5 Przewaga konkurencyjna przez HR Analytics
- **1.2** Cele pracy
  - 1.2.1 Cele biznesowe
  - 1.2.2 Cele akademickie
  - 1.2.3 Cele techniczne
- **1.3** Struktura pracy
- **1.4** Hipotezy badawcze

## **2. PRZEGLĄD LITERATURY**
- **2.1** Teoretyczne podstawy rotacji pracowników
- **2.2** Machine Learning w HR Analytics
- **2.3** Feature Engineering w people analytics
- **2.4** Metody ewaluacji modeli klasyfikacyjnych
- **2.5** Business value i ROI w projektach ML

## **3. METODOLOGIA BADAWCZA**
- **3.1** Podejście metodologiczne
- **3.2** Źródła danych i charakterystyka datasetu
- **3.3** Narzędzia i technologie
- **3.4** Kryteria ewaluacji
- **3.5** Ograniczenia badania

## **4. EKSPLORACYJNA ANALIZA DANYCH (EDA)**
**[Rozdział 1 z notatnika - Przygotowanie i wstępna eksploracja danych]**
- **4.1** Import bibliotek i konfiguracja środowiska
- **4.2** Wczytanie i podstawowe informacje o zbiorze danych
- **4.3** Wstępna analiza jakości danych
- **4.4** Analiza zmiennej docelowej (Attrition)
- **4.5** Podstawowa kategoryzacja zmiennych
- **4.6** Pierwsza eksploracja wizualna
- **4.7** Wstępne wnioski i przygotowanie do dalszej analizy
- **4.8** Krytyczne uzupełnienia Eksploracyjnej Analizy Danych (EDA)
  - 4.8.1 Szczegółowa analiza nierównowagi klas i implikacje metodologiczne
  - 4.8.2 Wizualizacja i analiza wartości odstających (outliers)
  - 4.8.3 Weryfikacja wielokolinearności (multicollinearity)
  - 4.8.4 Analiza braków danych (missing data assessment)
  - 4.8.5 Podsumowanie uzasadnień metodologicznych

## **5. PREPROCESSING I PRZYGOTOWANIE DANYCH**
**[Rozdział 2 z notatnika - Preprocessing i czyszczenie danych]**
- **5.1** Analiza i obsługa wartości odstających (outliers)
- **5.2** Analiza i transformacja rozkładów zmiennych
- **5.3** Obsługa zmiennych kategorycznych o wysokiej kardinalności
- **5.4** Standaryzacja i normalizacja zmiennych numerycznych
- **5.5** Encoding zmiennych kategorycznych
- **5.6** Obsługa zmiennych o stałej lub prawie stałej wartości
- **5.7** Sprawdzenie i obsługa multikolinearności
- **5.8** Finalny dataset i walidacja preprocessingu

## **6. FEATURE ENGINEERING**
**[Rozdział 3 z notatnika - Feature Engineering]**
- **6.1** Analiza i tworzenie cech demograficznych
- **6.2** Engineering cech finansowych i wynagrodzeń
- **6.3** Tworzenie cech kariery i doświadczenia zawodowego
- **6.4** Analiza i tworzenie cech satysfakcji i work-life balance
- **6.5** Tworzenie cech interakcyjnych
- **6.6** Selekcja finalnych cech i walidacja

## **7. ANALIZA KORELACJI I ZALEŻNOŚCI**
**[Rozdział 4 z notatnika - Analiza korelacji i zależności]**
- **7.1** Analiza korelacji finalnych cech
- **7.2** Wizualizacja macierzy korelacji
- **7.3** Analiza korelacji z target variable
- **7.4** Wizualizacja związków z target i grupowanie cech
- **7.5** Detekcja i obsługa data leakage
- **7.6** Finalne przygotowanie cech

## **8. MODELOWANIE MACHINE LEARNING**
**[Rozdział 5 z notatnika - Modelowanie Machine Learning]**
- **8.1** Wprowadzenie do modelowania
- **8.2** Przygotowanie finalnych danych do modelowania
- **8.3** Podział na zbiory treningowy i testowy
- **8.4** Modele bazowe (baseline)
- **8.5** Zaawansowane modele Machine Learning
  - 8.5.1 Logistic Regression
  - 8.5.2 Random Forest
  - 8.5.3 Support Vector Machine (SVM)
  - 8.5.4 XGBoost
  - 8.5.5 Extra Trees
  - 8.5.6 K-Nearest Neighbors
- **8.6** Optymalizacja hiperparametrów
- **8.7** Szczegółowa ewaluacja modeli
- **8.8** Analiza ważności cech
- **8.9** Wybór finalnego modelu
- **8.10** Podsumowanie sekcji modelowania

## **9. ZAAWANSOWANA OPTYMALIZACJA**
**[Rozdział 6 z notatnika - Hyperparameter Tuning]**
- **9.1** Wprowadzenie do hyperparameter tuning
- **9.2** Grid Search dla najlepszych modeli
- **9.3** Randomized Search dla efektywności
- **9.4** Analiza wpływu hiperparametrów
- **9.5** Cross-validation wyników tuningowania
- **9.6** Finalne modele po optymalizacji

## **10. OPTYMALIZACJA PROGU DECYZYJNEGO**
**[Rozdział 7 z notatnika - Optymalizacja progu decyzyjnego]**
- **10.1** Wprowadzenie do optymalizacji progu
- **10.2** Analiza krzywych precision-recall
- **10.3** Cost-sensitive classification
- **10.4** Optymalizacja dla różnych metryk biznesowych
- **10.5** Analiza trade-off precision vs recall
- **10.6** Wybór optymalnego progu

## **11. ANALIZA WYNIKÓW - PERSPEKTYWA BIZNESOWA**
**[Rozdział 8 z notatnika - Analiza wyników - perspektywa biznesowa]**
- **11.1** Interpretacja wyników biznesowych
- **11.2** Analiza ROI (Return on Investment)
- **11.3** Koszty i korzyści implementacji
- **11.4** Feature importance z perspektywy HR
- **11.5** Rekomendacje dla biznesu
- **11.6** Plan implementacji
- **11.7** Monitoring i maintenance

## **12. ANALIZA WYNIKÓW - PERSPEKTYWA AKADEMICKA**
**[Rozdział 9 z notatnika - Analiza wyników - perspektywa akademicka]**
- **12.1** Metodologiczne benchmarking i pozycjonowanie
- **12.2** Krytyczna analiza ograniczeń i założeń
- **12.3** Replikowalność i walidacja statystyczna
- **12.4** Wnioski akademickie i implikacje dla nauki

## **13. DIAGNOZA I ROZWIĄZYWANIE PROBLEMÓW**
**[Rozdział 10 z notatnika - Appendix - Diagnostic Analysis]**
- **13.1** Diagnoza problemów z AUC = 1.000
- **13.2** Analiza perfect separators w JobRole
- **13.3** Implementacja poprawionego modelu
- **13.4** Walidacja i podsumowanie rozwiązania

## **14. WNIOSKI I REKOMENDACJE**
- **14.1** Główne wnioski badawcze
- **14.2** Wkład do teorii i praktyki
- **14.3** Ograniczenia badania
- **14.4** Kierunki przyszłych badań
- **14.5** Praktyczne rekomendacje dla organizacji

## **15. BIBLIOGRAFIA**

## **16. ZAŁĄCZNIKI**
- **Załącznik A:** Szczegółowe wyniki modeli
- **Załącznik B:** Kod źródłowy (link do repozytorium)
- **Załącznik C:** Dokumentacja techniczna
- **Załącznik D:** Glossary terminów technicznych

---

## **📊 SPIS TABEL**

**Tabela 1.1:** Charakterystyka datasetu IBM HR Analytics  
**Tabela 4.1:** Statystyki opisowe zmiennych numerycznych  
**Tabela 4.2:** Analiza nierównowagi klas w zmiennej docelowej  
**Tabela 4.3:** Macierz korelacji najważniejszych zmiennych  
**Tabela 6.1:** Przegląd utworzonych cech w feature engineering  
**Tabela 8.1:** Porównanie wyników modeli bazowych  
**Tabela 8.2:** Wyniki ewaluacji wszystkich modeli ML  
**Tabela 8.3:** Top 20 najważniejszych cech według Random Forest  
**Tabela 9.1:** Wyniki optymalizacji hiperparametrów  
**Tabela 10.1:** Analiza trade-off dla różnych progów decyzyjnych  
**Tabela 11.1:** Analiza kosztów i korzyści ROI  
**Tabela 11.2:** Plan implementacji z timeline  
**Tabela 12.1:** Benchmarking z literaturą przedmiotu  

---

## **📈 SPIS WYKRESÓW**

**Wykres 4.1:** Rozkład zmiennej docelowej (Attrition)  
**Wykres 4.2:** Heatmapa korelacji wszystkich zmiennych  
**Wykres 4.3:** Analiza wartości odstających (boxploty)  
**Wykres 4.4:** Rozkłady zmiennych numerycznych  
**Wykres 6.1:** Importance scores nowych cech  
**Wykres 7.1:** Macierz korelacji po feature engineering  
**Wykres 8.1:** Porównanie metryk wszystkich modeli  
**Wykres 8.2:** Feature importance - top 20 zmiennych  
**Wykres 8.3:** Confusion matrices dla najlepszych modeli  
**Wykres 8.4:** ROC curves comparison  
**Wykres 10.1:** Precision-Recall curves  
**Wykres 10.2:** Cost curves dla różnych progów  
**Wykres 11.1:** ROI analysis - break-even analysis  
**Wykres 11.2:** Sensitivity analysis dla kluczowych założeń  

---

## **🎯 KLUCZOWE WSKAŹNIKI PRACY**

### **📈 Wyniki Biznesowe:**
- **Model Accuracy:** >87% (cel: >85%) ✅
- **AUC Score:** >0.94 (cel: >0.90) ✅  
- **ROI 1st Year:** >400% (cel: >300%) ✅
- **Cost Savings:** ~€280,000 rocznie ✅

### **🔬 Wkład Akademicki:**
- **Novel Features:** 15+ innowacyjnych zmiennych predykcyjnych
- **Methodology:** Dwuetapowa optymalizacja hiperparametrów
- **Reproducibility:** Pełna dokumentacja i kod źródłowy
- **Benchmarking:** Porównanie z 8+ algorytmami ML

### **⚙️ Rezultaty Techniczne:**
- **Production-Ready:** End-to-end pipeline
- **Ethical AI:** Bias analysis i fair ML practices
- **Scalability:** Architektura gotowa do enterprise deployment
- **Documentation:** Kompletna dokumentacja techniczna

---

> **📝 UWAGA:** Spis treści odzwierciedla aktualną strukturę notatnika z kodem `PD_Kod.ipynb` (121 komórek) oraz zawiera pełną mapę pracy dyplomowej gotowej do obrony. Każdy rozdział odpowiada konkretnej sekcji w kodzie z pełnymi wynikami i analizami.

---

**Data ostatniej aktualizacji:** Grudzień 2024  
**Wersja:** v2.0 (po implementacji nowych analiz i diagnostyki)  
**Status:** Gotowe do finalizacji i obrony