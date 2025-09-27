## 1.2. Problem Badawczy i Pytania Szczegółowe

### Sformułowanie problemu głównego

Pomimo rosnącego zainteresowania zastosowaniem sztucznej inteligencji w zarządzaniu zasobami ludzkimi, większość istniejących rozwiązań w obszarze predykcji rotacji pracowników koncentruje się na maksymalizacji tradycyjnych metryk klasyfikacyjnych (accuracy, precision, recall), ignorując rzeczywiste koszty biznesowe związane z błędami predykcji. Ta luka między doskonałością techniczną a wartością biznesową stanowi kluczowe wyzwanie dla praktycznego zastosowania machine learning w people analytics.

**Problem główny niniejszej pracy brzmi:**

> *"Jak skutecznie przewidywać i optymalizować koszty rotacji pracowników w oparciu o modele uczenia maszynowego z wykorzystaniem cost-sensitive optimization, aby maksymalizować rzeczywistą wartość biznesową przy zachowaniu etycznych standardów zarządzania danymi pracowniczymi?"*

Problem ten wykracza poza tradycyjne zadanie klasyfikacji binarnej i obejmuje wielowymiarowe wyzwanie optymalizacji biznesowej, które wymaga:

**1. Integracji perspektyw:**
- **Technicznej**: budowa modeli o wysokiej dokładności predykcyjnej
- **Biznesowej**: optymalizacja rzeczywistych kosztów i korzyści
- **Etycznej**: poszanowanie praw pracowników i fair treatment
- **Operacyjnej**: praktyczna implementowalność w środowisku HR

**2. Przezwyciężenia ograniczeń istniejących podejść:**
- **Accuracy bias**: koncentracja na metrykach technicznych kosztem value proposition
- **Cost blindness**: ignorowanie asymetrycznych kosztów błędów klasyfikacji
- **One-size-fits-all**: brak personalizacji strategii retention
- **Black box problem**: niewystarczająca interpretowalność dla stakeholderów HR

### Pytania szczegółowe badawcze

Realizacja głównego problemu badawczego wymaga udzielenia odpowiedzi na szereg szczegółowych pytań, które zostały sformułowane w oparciu o analizę literatury, konsultacje z praktykami HR oraz wstępną analizę dostępnych danych.

#### **RQ1: Które algorytmy machine learning osiągają najlepszą performance w predykcji employee attrition?**

**Kontekst pytania:**
Literatura przedmiotu wskazuje na różnorodność algorytmów stosowanych w predykcji rotacji - od prostych modeli logistycznych, przez ensemble methods (Random Forest, XGBoost), po zaawansowane architektury deep learning. Jednak badania często prezentują sprzeczne wyniki co do względnej skuteczności poszczególnych podejść.

**Komponenty szczegółowe:**
- Jak porównuje się performance algorytmów tree-based (Random Forest, XGBoost) z metodami liniowymi (Logistic Regression)?
- Czy złożoność modelu (liczba parametrów) przekłada się na lepszą jakość predykcji w kontekście HR data?
- Jakie są trade-offy między interpretowalnością a accuracy dla różnych rodzin algorytmów?
- Jak stabilność predykcji (robustness) różni się między algorytmami przy zmianach w danych?

**Oczekiwane wkłady:**
- Systematic comparison najważniejszych algoritów ML w kontekście HR analytics
- Identyfikacja optimal model class dla employee attrition prediction
- Analiza relationship między model complexity a practical performance

#### **RQ2: Jaki jest optymalny próg decyzyjny z perspektywy business cost optimization?**

**Kontekst pytania:**
Standardowe podejście w klasyfikacji binarnej wykorzystuje próg 0.5 dla konwersji prawdopodobieństw na decyzje. W kontekście biznesowym, gdzie koszty False Negative (przeoczona rotacja = 80,000 PLN) drastycznie przewyższają koszty False Positive (niepotrzebna interwencja = 3,500 PLN), tradycyjny próg może być suboptimalny.

**Komponenty szczegółowe:**
- Jak cost-sensitive threshold optimization wpływa na całkowite koszty biznesowe?
- Jakie są practical differences między threshold optimization opartą na Youden Index, F1-Score i cost minimization?
- Jak sensitivity analysis różnych scenariuszy kosztowych (conservative/realistic/aggressive) wpływa na optimal threshold?
- Jakie są implications różnych progów dla HR workload i resource allocation?

**Oczekiwane wkłady:**
- Metodologia cost-sensitive threshold optimization dla HR analytics
- Quantified business impact różnych strategii threshold selection
- Framework dla sensitivity analysis w cost parameter uncertainty

#### **RQ3: Jakie jest potencjalne ROI implementacji predykcyjnego systemu HR analytics?**

**Kontekst pytania:**
Mimo rosnącej popularności AI w HR, brakuje comprehensive business case analysis, które uwzględniałyby zarówno direct costs (technologia, implementacja), jak i indirect benefits (improved retention, productivity gains, knowledge preservation).

**Komponenty szczegółowe:**
- Jakie są total cost of ownership (TCO) dla production-ready systemu predykcji rotacji?
- Jak quantify korzyści typu knowledge retention, team stability, reduced emergency hiring?
- Jakie są payback period i long-term ROI projections dla różnych organization sizes?
- Jak risk-adjusted ROI consideration wpływa na business case viability?

**Oczekiwane wkłady:**
- Comprehensive ROI model dla HR predictive analytics
- Multi-scenario business case analysis (conservative/realistic/aggressive)
- Template dla economic evaluation podobnych HR AI initiatives

#### **RQ4: Jak feature engineering wpływa na accuracy i business value modeli predykcyjnych?**

**Kontekst pytania:**
Większość badań w obszarze employee attrition prediction operuje na raw HR data lub podstawowych transformacjach. Hipoteza badawcza zakłada, że business-context feature engineering może znacząco poprawić zarówno predictive performance, jak i business interpretability.

**Komponenty szczegółowe:**
- Jaki jest impact interaction terms (np. Age × YearsAtCompany) na model performance?
- Czy domain-specific feature creation (satisfaction composites, career progression indicators) poprawia predictive power?
- Jak feature engineering wpływa na model interpretability i actionable insights dla HR?
- Jakie są trade-offy między feature complexity a model stability/generalizability?

**Oczekiwane wkłady:**
- Business-integrated feature engineering methodology dla HR analytics
- Comparative analysis impact różnych feature creation strategies
- Best practices dla balansowania predictive power z interpretability

### Dodatkowe pytania eksploracyjne

Poza głównymi pytaniami badawczymi, praca będzie również eksplorować następujące zagadnienia o charakterze uzupełniającym:

**EQ1: Ethical considerations**
- Jak zapewnić fairness i avoid bias w algorytmach predykcji rotacji?
- Jakie są privacy implications i GDPR compliance requirements?

**EQ2: Implementation challenges**
- Jakie są key success factors dla successful deployment HR AI systems?
- Jak address change management i user adoption challenges?

**EQ3: Generalizability**
- Jak findings translate do różnych industries i organization sizes?
- Jakie są adaptation requirements dla cross-cultural contexts?

### Oczekiwane oryginalne wkłady

Realizacja sformułowanych pytań badawczych ma na celu wypracowanie następujących oryginalnych wkładów do wiedzy:

**1. Metodologiczny wkład:**
- **Cost-sensitive optimization framework** specjalnie dostosowany do HR analytics
- **Business-integrated feature engineering methodology** łącząca domain expertise z data science
- **Comprehensive evaluation protocol** uwzględniający zarówno technical performance, jak i business value

**2. Empiryczny wkład:**
- **Systematic comparison** algoritów ML w kontekście polskich danych HR
- **Quantified business case** z real-world ROI calculations i risk assessment
- **Practical insights** dotyczące optimal threshold selection i cost scenarios

**3. Praktyczny wkład:**
- **Production-ready framework** gotowy do implementacji w organizacjach
- **Decision support tools** dla HR professionals i business stakeholders
- **Ethical guidelines** dla responsible AI adoption w people management

### Scope i ograniczenia badania

**W zakresie badania:**
- Analiza 6 głównych rodzin algorytmów machine learning
- Cost-sensitive optimization w 3 scenariuszach biznesowych
- Comprehensive feature engineering z business context
- End-to-end evaluation od technical metrics do business ROI

**Poza zakresem badania:**
- Deep learning architectures (ze względu na sample size limitations)
- Real-time streaming analytics (focus na batch prediction)
- Multi-organizational validation (single dataset constraint)
- Causal inference i intervention effectiveness measurement

**Założenia metodologiczne:**
- Historical data adequately represents future patterns
- Cost parameters można reasonable estimate na podstawie industry benchmarks
- Model predictions będą wykorzystywane jako decision support, nie automatic decisions
- Ethical guidelines i privacy protection zostają maintained throughout

Sformułowane pytania badawcze stanowią fundament dla systematic investigation problemu cost-sensitive employee attrition prediction, oferując balance między academic rigor a practical applicability. Oczekuje się, że answers to these questions będą contribute zarówno do theoretical understanding HR analytics, jak i do practical toolkit dostępnego dla organizacji dążących do data-driven people management.