# 1. WPROWADZENIE

## 1.1. Uzasadnienie Wyboru Tematu i Znaczenie Problemu

### Znaczenie problemu rotacji w organizacjach współczesnych

Rotacja pracowników (employee turnover, attrition) stanowi jeden z najważniejszych wyzwań zarządzania zasobami ludzkimi w XXI wieku. Problem ten nabiera szczególnego znaczenia w kontekście współczesnego rynku pracy, charakteryzującego się wysoką mobilnością zawodową, zmianami demograficznymi oraz rosnącymi oczekiwaniami pracowników względem jakości środowiska pracy.

Badania przeprowadzone przez Society for Human Resource Management (SHRM) wskazują, że średni wskaźnik rotacji w organizacjach globalnie wynosi około 15-20% rocznie, przy czym w niektórych sektorach, takich jak retail czy hospitality, może osiągać nawet 40-60%. W kontekście analizowanych w niniejszej pracy danych z IBM HR Analytics Employee Attrition Dataset, obserwujemy **wskaźnik rotacji na poziomie 16.3%**, co plasuje badaną organizację w typowym przedziale dla współczesnych przedsiębiorstw.

Wysoki poziom rotacji pracowników nie jest jedynie statystyką HR-ową, lecz przekłada się na konkretne, wymierne konsekwencje dla funkcjonowania organizacji:

**Konsekwencje organizacyjne:**
- Utrata wiedzy instytucjonalnej i kompetencji kluczowych
- Zakłócenia w ciągłości procesów biznesowych i realizacji projektów
- Obniżenie morale i produktywności pozostałych pracowników
- Zwiększone obciążenie zespołów przez konieczność przejęcia dodatkowych obowiązków
- Deterioracja kultury organizacyjnej i atmosfery pracy

**Konsekwencje strategiczne:**
- Utrudniona realizacja długoterminowych celów biznesowych
- Osłabienie pozycji konkurencyjnej na rynku talentów
- Problemy z budowaniem i utrzymaniem zespołów ekspertów
- Ograniczona zdolność do innowacji i adaptacji do zmian rynkowych

### Wymiar ekonomiczny problemu rotacji

Koszty rotacji pracowników stanowią często niedocenianą pozycję w budżetach organizacji, głównie ze względu na ich częściowo ukryty charakter. Tradycyjne podejście do kalkulacji kosztów turnover koncentruje się zazwyczaj na bezpośrednich wydatkach związanych z rekrutacją i wdrożeniem nowego pracownika, pomijając szereg kosztów pośrednich i długoterminowych.

**Kompleksowa struktura kosztów rotacji:**

**1. Koszty bezpośrednie (Direct Costs):**
- Koszty rekrutacji: ogłoszenia, agencje HR, employer branding (średnio 3,000-5,000 PLN)
- Koszty selekcji: czas HR-owców, testy, assessment center (2,000-4,000 PLN)
- Koszty administracyjne: dokumentacja, systemy IT, infrastruktura (1,000-2,000 PLN)
- Koszty wdrożenia: onboarding, szkolenia, mentoring (5,000-15,000 PLN)

**2. Koszty pośrednie (Indirect Costs):**
- Utracona produktywność odchodzącego pracownika w okresie wypowiedzenia
- Obniżona efektywność nowego pracownika w okresie adaptacji (3-12 miesięcy)
- Dodatkowe obciążenie supervisorów i kolegów z zespołu
- Koszty nadgodzin i tymczasowego zastępstwa

**3. Koszty ukryte (Hidden Costs):**
- Utrata wiedzy organizacyjnej i relacji z klientami
- Impact na morale i engagement pozostałych pracowników
- Ryzyko "efektu domina" - kolejnych odejść w zespole
- Opóźnienia w projektach i niższa jakość usług

Zgodnie z badaniami Society for Human Resource Management, całkowite koszty zastąpienia pracownika wahają się od 50% do 200% jego rocznego wynagrodzenia, w zależności od pozioma stanowiska i specyfiki branży. W kontekście polskiego rynku pracy, dla pracownika o średnim wynagrodzeniu 8,000 PLN miesięcznie, **szacunkowy koszt rotacji wynosi około 80,000 PLN na jednego odchodzącego pracownika**.

**Kalkulacja kosztów dla analizowanej organizacji:**
- Liczba pracowników w dataset: 1,470
- Wskaźnik rotacji: 16.3%
- Liczba odejść rocznie: 1,470 × 0.163 = 240 pracowników
- Roczne koszty rotacji: 240 × 80,000 PLN = **19,200,000 PLN**

Ta astronomiczna kwota ilustruje skalę problemu i potencjał korzyści płynących z jego skutecznego adresowania.

### Potencjał rozwiązań Cost-Sensitive Machine Learning

Tradycyjne podejścia do zarządzania rotacją pracowników opierają się głównie na:
- Reaktywnych działaniach post-factum (exit interviews, analiza przyczyn odejść)
- Intuicyjnych ocenach ryzyka przez menedżerów HR
- Standardowych programach retention o charakterze "one-size-fits-all"
- Okresowych badaniach satysfakcji i zaangażowania

Podejście to, choć wartościowe, charakteryzuje się istotnymi limitacjami:
- **Reaktywność**: działania podejmowane są dopiero po wystąpieniu problemu
- **Subiektywność**: oceny opierają się na intuicji i doświadczeniu, nie na danych
- **Nieefektywność**: brak personalizacji interwencji do specyficznych profili ryzyka
- **Brak kwantyfikacji**: trudność w ocenie ROI podejmowanych działań

**Przewaga predykcyjnego podejścia opartego na Machine Learning:**

Cost-Sensitive Machine Learning stanowi paradigmat, który wykracza poza tradycyjne metryki accuracy czy precision, koncentrując się na optymalizacji rzeczywistych kosztów biznesowych związanych z błędami klasyfikacji. W kontekście predykcji rotacji pracowników oznacza to:

**1. Asymetryczne koszty błędów:**
- **False Negative (FN)**: Przeoczenie pracownika, który rzeczywiście odejdzie
  - Koszt: pełne 80,000 PLN kosztów rotacji
- **False Positive (FP)**: Niepotrzebna interwencja wobec pracownika, który nie planuje odejścia
  - Koszt: 3,500 PLN (czas HR, coaching, dodatkowe benefity)

**2. Optymalizacja progów decyzyjnych:**
Zamiast standardowego progu 0.5, algorytm określa optymalny próg minimalizujący całkowite koszty biznesowe, uwzględniając asymetrię kosztów FN vs FP.

**3. Personalizowane strategie interwencji:**
Model umożliwia identyfikację nie tylko pracowników wysokiego ryzyka, ale także kluczowych czynników wpływających na ich decyzję o odejściu, co pozwala na targeted retention actions.

**Udowodniony potencjał oszczędności:**

Analiza przeprowadzona w ramach niniejszej pracy wykazała, że implementacja systemu predykcyjnego opartego na cost-sensitive optimization może generować **roczne oszczędności na poziomie 47,600 PLN** przy koszcie implementacji około 3,000 PLN, co przekłada się na **return on investment (ROI) na poziomie 15.9x**.

**Mechanizm generowania oszczędności:**
- **Wczesna identyfikacja**: pracownicy wysokiego ryzyka identyfikowani średnio 3-6 miesięcy przed planowanym odejściem
- **Targeted interventions**: personalizowane programy retention zamiast kosztownych, szerokich inicjatyw
- **Redukcja emergency hiring**: mniej rekrutacji "pod presją czasu" o wyższych kosztach
- **Preserve institutional knowledge**: zachowanie kluczowych kompetencji i relacji

**Szerszy kontekst People Analytics:**

Implementacja cost-sensitive ML w predykcji rotacji stanowi element szerszej transformacji cyfrowej funkcji HR, określanej mianem People Analytics 2.0. Ten paradygmat charakteryzuje się:
- **Data-driven decision making**: decyzje oparte na analizie danych, nie intuicji
- **Predictive capabilities**: przejście od raportowania historycznego do przewidywania przyszłości
- **Business value focus**: koncentracja na wymiernych korzyściach biznesowych
- **Ethical AI adoption**: odpowiedzialne wykorzystanie technologii z poszanowaniem praw pracowników

W kontekście polskiego rynku pracy, gdzie średnie koszty rekrutacji rosną o 8-12% rocznie, a wojna o talenty nasila się w kluczowych sektorach (IT, finanse, produkcja), rozwiązania predykcyjne przestają być "nice-to-have" i stają się **competitive necessity**.

**Podsumowanie znaczenia problemu:**

Problem rotacji pracowników stanowi jedno z kluczowych wyzwań współczesnego zarządzania zasobami ludzkimi, generując koszty sięgające w badanej organizacji blisko 20 milionów PLN rocznie. Tradycyjne, reaktywne podejścia do jego adresowania okazują się niewystarczające w obliczu dynamiki współczesnego rynku pracy.

Cost-sensitive machine learning oferuje innowacyjne rozwiązanie, które nie tylko umożliwia predykcję rotacji z wysoką dokładnością (AUC = 0.8275), ale przede wszystkim optymalizuje rzeczywiste koszty biznesowe, generując udowodnione oszczędności na poziomie 47,600 PLN rocznie przy ROI 15.9x.

Niniejsza praca stanowi próbę wypełnienia luki między zaawansowanymi metodami machine learning a praktycznymi potrzebami biznesowymi w obszarze people analytics, oferując comprehensive framework gotowy do implementacji produkcyjnej w polskich organizacjach.