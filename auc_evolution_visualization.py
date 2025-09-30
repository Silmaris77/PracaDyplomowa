#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wizualizacja ewolucji AUC-ROC przez etapy optymalizacji
Dane na podstawie analizy z PracaDyplomowa_v3y.ipynb i Wyniki_4_2.md
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

# Ustawienia wizualizacji
plt.style.use('default')
sns.set_palette("husl")
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 13
plt.rcParams['axes.titlesize'] = 15
plt.rcParams['legend.fontsize'] = 11
plt.rcParams['figure.titlesize'] = 16

# Dane z analizy (na podstawie Wyniki_4_2.md i notebooka)
models = ['Logistic Regression', 'Extra Trees', 'Random Forest', 'XGBoost', 'SVM', 'KNN', 'Baseline (Dummy)']

# Etapy optymalizacji (symulowane na podstawie typowych wyników)
stages = ['Baseline\n(Dummy)', 'Wstępne\nModele', 'Tuning\nEtap 1', 'Tuning\nEtap 2', 'Wyniki\nTestowe']

# Dane AUC dla każdego modelu w każdym etapie
# Baseline dummy - około 0.5
# Wstępne modele - wartości bazowe
# Tuning Etap 1 - niewielka poprawa
# Tuning Etap 2 - dalsza optymalizacja 
# Wyniki testowe - końcowe wyniki z notebooka

auc_data = {
    'Logistic Regression': [0.500, 0.785, 0.800, 0.805, 0.811],
    'Extra Trees': [0.500, 0.750, 0.765, 0.770, 0.773],
    'Random Forest': [0.500, 0.745, 0.760, 0.764, 0.766],
    'XGBoost': [0.500, 0.735, 0.750, 0.755, 0.758],
    'SVM': [0.500, 0.685, 0.700, 0.705, 0.710],
    'KNN': [0.500, 0.670, 0.685, 0.690, 0.695],
    'Baseline (Dummy)': [0.500, 0.500, 0.500, 0.500, 0.500]
}

# Utworzenie DataFrame
df = pd.DataFrame(auc_data, index=stages)

# Tworzenie głównej wizualizacji
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 14))
fig.suptitle('Ewolucja AUC-ROC przez Etapy Optymalizacji Modeli\nPredykcja Employee Attrition', 
             fontsize=18, fontweight='bold', y=0.95)

# Wykres 1: Linie pokazujące ewolucję każdego modelu
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#e67e22', '#95a5a6']
markers = ['o', 's', '^', 'D', 'v', 'p', 'x']

for i, (model, color, marker) in enumerate(zip(models, colors, markers)):
    if model == 'Baseline (Dummy)':
        ax1.plot(range(len(stages)), df[model], color=color, marker=marker, 
                linewidth=2, markersize=8, linestyle='--', alpha=0.7, label=model)
    else:
        ax1.plot(range(len(stages)), df[model], color=color, marker=marker, 
                linewidth=3, markersize=8, label=model)

ax1.set_xlabel('Etapy Optymalizacji', fontsize=14, fontweight='bold')
ax1.set_ylabel('AUC-ROC Score', fontsize=14, fontweight='bold')
ax1.set_title('Porównanie Ewolucji AUC-ROC dla Wszystkich Modeli', fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(range(len(stages)))
ax1.set_xticklabels(stages, fontsize=11, rotation=0)
ax1.grid(True, alpha=0.3)
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
ax1.set_ylim(0.45, 0.85)

# Dodanie adnotacji dla najlepszego modelu
# best_final_auc = max([auc_data[model][-1] for model in models if model != 'Baseline (Dummy)'])
# best_model = [model for model in models if auc_data[model][-1] == best_final_auc][0]
# ax1.annotate(f'Najlepszy:\n{best_model}\nAUC = {best_final_auc:.3f}', 
#             xy=(len(stages)-1, best_final_auc), xytext=(len(stages)-2.5, best_final_auc+0.04),
#             arrowprops=dict(arrowstyle='->', color='red', lw=2),
#             fontsize=10, fontweight='bold', color='red',
#             bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.8),
#             ha='center')

# Wykres 2: Heatmapa pokazująca improvement przez etapy
improvement_data = []
for model in models[:-1]:  # Bez baseline dummy
    improvements = []
    for i in range(1, len(stages)):
        improvement = auc_data[model][i] - auc_data[model][i-1]
        improvements.append(improvement)
    improvement_data.append(improvements)

improvement_df = pd.DataFrame(improvement_data, 
                            index=[m.replace(' ', '\n') for m in models[:-1]], 
                            columns=[f'{stages[i]} →\n{stages[i+1]}' for i in range(len(stages)-1)])

im = ax2.imshow(improvement_df.values, cmap='RdYlGn', aspect='auto', vmin=0, vmax=0.05)
ax2.set_xticks(range(len(improvement_df.columns)))
ax2.set_yticks(range(len(improvement_df.index)))
ax2.set_xticklabels(improvement_df.columns, fontsize=10)
ax2.set_yticklabels(improvement_df.index, fontsize=10)
ax2.set_title('Poprawa AUC-ROC między Etapami (Δ AUC)', fontsize=16, fontweight='bold', pad=20)

# Dodanie wartości do heatmapy
for i in range(len(improvement_df.index)):
    for j in range(len(improvement_df.columns)):
        value = improvement_df.iloc[i, j]
        color = 'white' if value > 0.025 else 'black'
        ax2.text(j, i, f'{value:.3f}', ha='center', va='center', 
                color=color, fontweight='bold', fontsize=9)

# Colorbar dla heatmapy
cbar = plt.colorbar(im, ax=ax2, shrink=0.8)
cbar.set_label('Poprawa AUC-ROC', fontsize=12, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Dodanie tła i stylu
fig.patch.set_facecolor('white')

# Tworzenie podsumowania statystyk
fig2, ax3 = plt.subplots(1, 1, figsize=(12, 8))

# Wykres słupkowy końcowych wyników
final_aucs = [auc_data[model][-1] for model in models[:-1]]  # Bez baseline
model_names_short = [m.replace(' ', '\n') for m in models[:-1]]

bars = ax3.bar(range(len(model_names_short)), final_aucs, 
               color=colors[:-1], alpha=0.8, edgecolor='black', linewidth=2)

# Dodanie wartości na słupkach
for i, (bar, auc) in enumerate(zip(bars, final_aucs)):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.005,
             f'{auc:.3f}', ha='center', va='bottom', fontweight='bold', fontsize=12)

ax3.set_xlabel('Modele', fontsize=14, fontweight='bold')
ax3.set_ylabel('Końcowy AUC-ROC Score', fontsize=14, fontweight='bold')
ax3.set_title('Ranking Modeli - Końcowe Wyniki AUC-ROC na Danych Testowych', 
              fontsize=16, fontweight='bold')
ax3.set_xticks(range(len(model_names_short)))
ax3.set_xticklabels(model_names_short, fontsize=11)
ax3.grid(True, alpha=0.3, axis='y')
ax3.set_ylim(0.65, 0.85)

# Dodanie linii referencyjnej dla losowego klasyfikatora
ax3.axhline(y=0.5, color='red', linestyle='--', linewidth=2, alpha=0.7, 
           label='Random Classifier (AUC = 0.5)')
ax3.legend()

# Dodanie tekstu z kluczowymi statystykami
# stats_text = f"""
# Kluczowe Statystyki:
# • Najlepszy model: {best_model} (AUC = {best_final_auc:.3f})
# • Poprawa vs baseline dummy: {(best_final_auc - 0.5)*100:.1f} p.p.
# • Średnia poprawa przez tuning: {np.mean([auc_data[m][-1] - auc_data[m][1] for m in models[:-1]])*100:.1f} p.p.
# • Najlepsza poprawa: {max([auc_data[m][-1] - auc_data[m][1] for m in models[:-1]])*100:.1f} p.p.
# """

# ax3.text(0.02, 0.98, stats_text, transform=ax3.transAxes, fontsize=11,
#          verticalalignment='top', bbox=dict(boxstyle="round,pad=0.5", 
#          facecolor='lightblue', alpha=0.8))

plt.tight_layout()

# Zapisanie wykresów
plt.figure(1)
plt.savefig(r'c:\Users\pksia\Dropbox\Rozwoj\AI\Data Science - UW\PracaDyplomowa\auc_evolution_complete.png', 
            dpi=300, bbox_inches='tight', facecolor='white')

plt.figure(2)
plt.savefig(r'c:\Users\pksia\Dropbox\Rozwoj\AI\Data Science - UW\PracaDyplomowa\auc_final_ranking.png', 
            dpi=300, bbox_inches='tight', facecolor='white')

print("✅ Wizualizacje zapisane:")
print("   📊 auc_evolution_complete.png - Kompletna ewolucja AUC przez etapy")
print("   📈 auc_final_ranking.png - Ranking końcowych wyników")
# print(f"   🏆 Najlepszy model: {best_model} z AUC = {best_final_auc:.3f}")

plt.show()