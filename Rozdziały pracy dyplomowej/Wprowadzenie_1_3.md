## 1.3. Cele Pracy i Hipotezy Badawcze

### Cel główny badania

**Celem głównym niniejszej pracy jest opracowanie production-ready framework dla cost-sensitive prediction rotacji pracowników, który łączy zaawansowane metody machine learning z rzeczywistymi potrzebami biznesowymi organizacji, zapewniając jednocześnie etyczne standardy zarządzania danymi pracowniczymi.**

Framework ten ma charakteryzować się:
- **Praktyczną implementowalnością**: gotowość do wdrożenia w rzeczywistym środowisku HR bez konieczności dodatkowych badań czy developmentu
- **Optymalizacją kosztową**: skupienie na minimalizacji rzeczywistych kosztów biznesowych, nie tylko na maksymalizacji accuracy
- **Scalability**: możliwość adaptacji do organizacji różnej wielkości i profilu działalności
- **Ethical compliance**: pełne poszanowanie praw pracowników, GDPR i emerging AI regulations
- **Business interpretability**: zapewnienie clear insights i actionable recommendations dla stakeholderów HR

Cel główny wykracza poza tradycyjne zadanie klasyfikacji binarnej i obejmuje kompleksowe rozwiązanie biznesowe, które może służyć jako template dla similar HR analytics initiatives w polskich i międzynarodowych organizacjach.

### Cele szczegółowe

#### **CS1: Porównanie skuteczności różnych algorytmów machine learning w kontekście HR analytics**

**Uzasadnienie:**
Literatura przedmiotu prezentuje fragmentaryczne i często sprzeczne wyniki dotyczące optymalnych algorytmów dla employee attrition prediction. Brakuje systematic comparison w kontekście polskich danych HR z uwzględnieniem specyficznych charakterystyk rynku pracy.

**Zakres realizacji:**
- **Comprehensive benchmarking** 6 głównych rodzin algorytmów ML: Linear Methods (Logistic Regression), Tree-based (Random Forest, XGBoost), Instance-based (k-NN), Ensemble Methods (Extra Trees), Support Vector Machines
- **Multi-metric evaluation**: AUC-ROC, Precision, Recall, F1-Score, plus cost-sensitive metrics
- **Computational efficiency analysis**: training time, prediction time, memory consumption
- **Stability assessment**: cross-validation consistency, hyperparameter sensitivity
- **Interpretability comparison**: feature importance accessibility, decision transparency

**Oczekiwane deliverables:**
- Ranking algorytmów ML dla HR analytics w kontekście polskim
- Guidelines dla algorithm selection w zależności od organizational constraints
- Performance vs interpretability trade-off analysis

#### **CS2: Optymalizacja progów decyzyjnych pod kątem minimizacji kosztów biznesowych**

**Uzasadnienie:**
Standardowe progi klasyfikacji (0.5) ignorują asymetryczne koszty błędów w kontekście biznesowym. W przypadku employee attrition, koszt False Negative (80,000 PLN) drastycznie przewyższa koszt False Positive (3,500 PLN), co wymaga dedykowanej cost-sensitive optimization.

**Zakres realizacji:**
- **Cost parameter estimation**: systematic approach do determining FN i FP costs w polskim kontekście
- **Multi-scenario analysis**: conservative (FN:FP = 15:1), realistic (FN:FP = 23:1), aggressive (FN:FP = 35:1) cost ratios
- **Threshold optimization algorithms**: porównanie Youden Index, F1-optimization, i pure cost minimization
- **Sensitivity analysis**: robustness optymalnych progów przy zmianie cost assumptions
- **Business impact quantification**: translation threshold changes na concrete business outcomes

**Oczekiwane deliverables:**
- Cost-sensitive threshold optimization methodology
- Multi-scenario business impact calculator
- Guidelines dla cost parameter estimation w różnych organizational contexts

#### **CS3: Kwantyfikacja business value i ROI wdrożenia systemu predykcyjnego**

**Uzasadnienie:**
Pomimo rosnącej popularności AI w HR, brakuje comprehensive business case analysis, które uwzględniałyby total cost of ownership i long-term value creation. Bez clear ROI demonstration, adoption pozostaje limited do early adopters.

**Zakres realizacji:**
- **Total Cost of Ownership (TCO) modeling**: technology costs, implementation effort, training, maintenance
- **Multi-dimensional benefit quantification**: 
  - Direct savings: reduced turnover costs, lower recruitment expenses
  - Indirect benefits: improved productivity, knowledge retention, team stability
  - Strategic advantages: better talent management, competitive edge, employer branding
- **Risk-adjusted ROI calculation**: uncertainty modeling, scenario planning, sensitivity testing
- **Payback period analysis**: time-to-value w different organizational contexts
- **Long-term value projection**: 3-5 year horizon z compound benefits

**Oczekiwane deliverables:**
- Comprehensive ROI model z customizable parameters
- Business case template dla HR analytics initiatives
- Risk assessment framework dla AI adoption w people management

#### **CS4: Stworzenie comprehensive methodology dla feature engineering w people analytics**

**Uzasadnienie:**
Większość badań w obszarze employee attrition prediction operuje na raw HR data, pomijając potencjał business-context feature engineering. Hipoteza zakłada, że domain-informed feature creation może significantly improve zarówno predictive performance, jak i business interpretability.

**Zakres realizacji:**
- **Domain expertise integration**: collaboration z HR practitioners dla identifying meaningful feature combinations
- **Business-context feature creation**: 
  - Career progression indicators (promotion velocity, role transitions)
  - Satisfaction composites (work-life balance scores, engagement indices)
  - Interaction terms (age × tenure, salary × performance combinations)
  - Temporal features (seasonality, tenure milestones)
- **Feature selection optimization**: balancing predictive power z interpretability i computational efficiency
- **Cross-validation stability**: ensuring engineered features generalize across different data samples
- **Interpretability enhancement**: creating features that translate directly do actionable HR insights

**Oczekiwane deliverables:**
- Business-integrated feature engineering methodology
- Feature library dla HR analytics applications
- Best practices guide dla balancing complexity z interpretability

### Hipotezy badawcze

Na podstawie przeglądu literatury, preliminary data analysis oraz konsultacji z praktykami HR, sformułowano następujące hipotezy badawcze, które będą poddane empirycznej weryfikacji:

#### **H1: Czynniki związane z przeciążeniem pracą i wynagrodzeniem są kluczowymi predyktorami rotacji pracowników**

**Theoretical foundation:**
Teoria Herzberga i model Job Demands-Resources wskazują, że nadmierne obciążenie pracą (job demands) bez odpowiednich zasobów (job resources) prowadzi do wypalenia zawodowego i zwiększonej skłonności do odejścia. Jednocześnie, teoria sprawiedliwości organizacyjnej podkreśla znaczenie adekwatnej kompensacji jako fundamentalnego czynnika retencyjnego.

**Operational hypothesis:**
> *Zmienne związane z przeciążeniem pracą (`OverTime`, `WorkLifeBalance`) oraz czynniki finansowe (`MonthlyIncome`, `PercentSalaryHike`) będą wykazywały najsilniejsze i statystycznie istotne związki ze zmienną `Attrition` w eksploracyjnej analizie danych.*

**Measurement approach:**
- Analiza dwuzmiennowa dla każdego predyktora vs `Attrition`
- Testy chi-kwadrat dla zmiennych kategorycznych, t-testy dla zmiennych ciągłych
- Obliczenie wielkości efektu (Cohen's d, Cramer's V)
- Ranking predyktorów według siły związku ze zmienną celu
- Analiza wzorców biznesowych i identyfikacja grup wysokiego ryzyka

**Research prediction:**
Teoria organizacyjna i badania empiryczne sugerują, że czynniki związane z równowagą praca-życie oraz sprawiedliwością kompensacyjną będą dominującymi predyktorami decyzji o odejściu z organizacji.

#### **H2: Regresja Logistyczna osiągnie wydajność porównywalną lub lepszą od złożonych algorytmów drzewiastych po zastosowaniu zaawansowanej inżynierii cech**

**Theoretical foundation:**
Advanced feature engineering może skutecznie "linearyzować" złożone, nieliniowe relacje przez tworzenie odpowiednich terminów interakcji i transformacji. Gdy domain knowledge zostaje zintegrowane z danymi przez thoughtful feature construction, prostsze modele liniowe mogą dorównać lub przewyższać complex algorithms przy jednoczesnym zachowaniu interpretability advantages.

**Operational hypothesis:**
> *Po zastosowaniu comprehensive feature engineering (rozszerzenie z 35 do ~42 zmiennych), Regresja Logistyczna osiągnie AUC-ROC performance porównywalną lub wyższą od Random Forest i XGBoost, przy jednoczesnym zachowaniu superior interpretability i computational efficiency.*

**Measurement approach:**
- Systematic comparison 4 głównych algorytmów: Logistic Regression, Random Forest, XGBoost, SVM
- Cross-validated AUC performance z statistical significance testing (DeLong tests)
- Comprehensive hyperparameter optimization dla fair comparison
- Feature importance analysis i model interpretability assessment
- Computational efficiency comparison (training time, prediction time, memory usage)

**Research prediction:**
Hypothesis challenges conventional wisdom o algorithmic complexity requirements, suggesting że strategic feature engineering może enable simple models do achieve competitive performance z significant practical advantages w production deployment.

#### **H3: Cost-sensitive optimization znacząco poprawia business value w porównaniu do standardowych metryk accuracy-focused**

**Theoretical foundation:**
W business context employee attrition prediction, asymmetric costs błędów klasyfikacji (False Negative cost ~80,000 PLN vs False Positive cost ~3,500 PLN) oznaczają, że traditional accuracy metrics są suboptimal dla business value maximization. Cost-sensitive learning theory suggests że optimization pod kątem rzeczywistych business costs generate superior ROI.

**Operational hypothesis:**
> *Cost-sensitive threshold optimization będzie generate co najmniej 50% wyższą business value (measured w PLN savings) w porównaniu do standard 0.5 classification threshold, przy jednoczesnym achievement positive ROI exceeding 300% w pierwszym roku implementation.*

**Measurement approach:**
- Business value calculation: (True Positives × 80,000 PLN) - (False Positives × 3,500 PLN) - Implementation costs
- Optimal threshold determination through cost minimization algorithms
- ROI analysis: (Annual Savings - Implementation Costs) / Implementation Costs × 100%
- Multi-scenario sensitivity analysis z conservative/realistic/aggressive cost assumptions
- Payback period calculation i long-term value projection

**Research prediction:**
Given dramatic cost asymmetry (FN:FP cost ratio ~23:1) i proven model effectiveness, cost-sensitive optimization should generate substantial business value improvement, potentially achieving exceptional ROI przez strategic threshold adjustment aligned z business economics rather than statistical conventions.

### Metodologia weryfikacji hipotez

#### **Statistical approach:**
- **Confidence level**: 95% dla wszystkich statistical tests
- **Cross-validation**: 5-fold stratified CV dla model performance assessment
- **Significance testing**: paired t-tests dla algorithm comparisons, McNemar's test dla classification improvements
- **Effect size measurement**: Cohen's d dla practical significance assessment
- **Multiple testing correction**: Bonferroni adjustment gdzie applicable

#### **Business validation:**
- **Conservative assumptions**: underestimating benefits, overestimating costs
- **Sensitivity analysis**: testing hypothesis robustness przy różnych parameter assumptions
- **Stakeholder validation**: HR practitioner review of business metrics i interpretability
- **External benchmarking**: porównanie results z published industry standards

#### **Ethical considerations:**
- **Data privacy**: full GDPR compliance w hypothesis testing
- **Bias assessment**: fairness metrics across demographic groups
- **Transparency**: explainable models dla hypothesis validation
- **Stakeholder consent**: clear communication of research purposes i outcomes

### Expected contributions and implications

**W przypadku potwierdzenia hipotez:**
- **H1 confirmation**: Validates theoretical frameworks (Herzberg, JD-R model) w practical HR context, establishing workload i compensation jako primary intervention targets
- **H2 validation**: Demonstrates że feature engineering + simple models może outperform complex algorithms, providing cost-effective alternative do sophisticated ML approaches
- **H3 verification**: Establishes cost-sensitive optimization jako essential practice w HR analytics, creating compelling business case dla data-driven retention strategies

**W przypadku falsyfikacji:**
- **H1 rejection**: Would challenge established organizational psychology theories, suggesting other factors (culture, leadership, development opportunities) may be more critical than workload/compensation
- **H2 rejection**: Would confirm conventional ML wisdom about algorithmic complexity requirements, validating investment w sophisticated tree-based approaches dla HR analytics
- **H3 rejection**: Would indicate that traditional accuracy metrics są sufficient dla HR decision-making, questioning value proposition cost-sensitive optimization w people analytics

**Alternative findings exploration:**
- **Learning opportunities**: Understanding limitations i boundary conditions of each approach
- **Methodological insights**: Identification of superior or alternative analytical pathways
- **Context dependency**: Determining organizational or data contexts where hypotheses may/may not hold
- **Future research directions**: Areas requiring further investigation based on empirical findings

**Broader implications:**
- **Academic contribution**: Integration organizational psychology theory z advanced ML methodology, providing empirical validation key retention theories
- **Industry impact**: Practical, implementable framework dla cost-effective HR analytics adoption z clear ROI demonstration
- **Methodological innovation**: Demonstrates power feature engineering + simple models jako alternative do algorithmic complexity w people analytics
- **Policy considerations**: Guidelines dla ethical, cost-sensitive AI adoption w employment contexts z regulatory compliance
- **International relevance**: Methodology applicable across cultural i regulatory environments, scalable dla organizations różnej wielkości

**Research Integration:**
Te trzy hipotezy together form **comprehensive research framework** that tests:
1. **Theoretical foundations** (H1): Which employee factors truly drive turnover decisions
2. **Methodological approaches** (H2): Optimal balance między model complexity a practical effectiveness  
3. **Business value creation** (H3): Translation technical capabilities into measurable organizational benefits

Sformułowane cele i hipotezy stanowią fundament dla systematic investigation cost-sensitive employee attrition prediction, łącząc **rigorous theoretical testing** z **practical business application**, ensuring contribution zarówno do **academic knowledge advancement** jak i **industry practice transformation** w obszarze people analytics.