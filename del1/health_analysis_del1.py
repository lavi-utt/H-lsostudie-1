"""
Del 1: Grundläggande analys och statistik
Individuell uppgift – Hälsostudie

Denna script utför grundläggande analys av hälsostudiedata inklusive:
- Beskrivande statistik
- Visualiseringar
- Simuleringar
- Konfidensintervall
- Hypotesprövning

Författare: [Ditt Namn]
Datum: 2024
Python version: 3.14.3
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Sätt seed för reproducerbarhet
np.random.seed(42)

# Läs in datasetet
file_path = '../data/health_study_dataset.csv'
df = pd.read_csv(file_path)

print("=" * 80)
print("DEL 1: GRUNDLÄGGANDE ANALYS OCH STATISTIK")
print("=" * 80)

# ============================================================================
# 1. BESKRIVANDE ANALYS (G)
# ============================================================================
print("\n" + "=" * 80)
print("1. BESKRIVANDE ANALYS (G)")
print("=" * 80)

# Räkna ut medel, median, min och max
stats_columns = ['age', 'weight', 'height', 'systolic_bp', 'cholesterol']
descriptive_stats = df[stats_columns].agg(['mean', 'median', 'min', 'max'])

print("\nBeskrivande statistik:")
print(descriptive_stats)

# Spara för senare användning
age_mean = df['age'].mean()
weight_mean = df['weight'].mean()
height_mean = df['height'].mean()
systolic_bp_mean = df['systolic_bp'].mean()
cholesterol_mean = df['cholesterol'].mean()

# Graf 1: Histogram över blodtryck
print("\n\nSkapar Graf 1: Histogram över systoliskt blodtryck...")
plt.figure(figsize=(10, 6))
plt.hist(df['systolic_bp'], bins=30, edgecolor='black', alpha=0.7, color='skyblue')
plt.title('Histogram över systoliskt blodtryck (mmHg)')
plt.xlabel('Systoliskt blodtryck (mmHg)')
plt.ylabel('Frekvens')
plt.grid(True, alpha=0.3)
plt.savefig('../output/del1_histogram_blodtryck.png')
plt.close()
print("Sparad som: ../output/del1_histogram_blodtryck.png")

# Graf 2: Boxplot över vikt per kön
print("\nSkapar Graf 2: Boxplot över vikt per kön...")
plt.figure(figsize=(10, 6))
sns.boxplot(x='sex', y='weight', data=df, palette='pastel')
plt.title('Boxplot: Vikt per kön')
plt.xlabel('Kön')
plt.ylabel('Vikt (kg)')
plt.grid(True, alpha=0.3)
plt.savefig('../output/del1_boxplot_vikt_per_kon.png')
plt.close()
print("Sparad som: ../output/del1_boxplot_vikt_per_kon.png")

# Graf 3: Stapeldiagram över andelen rökare
print("\nSkapar Graf 3: Stapeldiagram över andelen rökare...")
smoker_counts = df['smoker'].value_counts()
smoker_percentage = df['smoker'].value_counts(normalize=True) * 100

plt.figure(figsize=(8, 6))
bars = plt.bar(smoker_counts.index, smoker_counts.values, color=['lightgreen', 'lightcoral'], alpha=0.8, edgecolor='black')
plt.title('Andel rökare i datasetet')
plt.xlabel('Röker')
plt.ylabel('Antal')

# Lägg till procent på staplarna
for i, (count, pct) in enumerate(zip(smoker_counts.values, smoker_percentage.values)):
    plt.text(i, count + 5, f'{pct:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.grid(True, alpha=0.3, axis='y')
plt.savefig('../output/del1_barplot_rokare.png')
plt.close()
print("Sparad som: ../output/del1_barplot_rokare.png")

print(f"\nAndel rökare:")
print(f"  Icke-rökare: {smoker_percentage['No']:.2f}% ({smoker_counts['No']} personer)")
print(f"  Rökare: {smoker_percentage['Yes']:.2f}% ({smoker_counts['Yes']} personer)")

# ============================================================================
# 2. SIMULERING KOPPLAD TILL CASET (G)
# ============================================================================
print("\n" + "=" * 80)
print("2. SIMULERING KOPPLAD TILL CASET (G)")
print("=" * 80)

# Beräkna andelen personer i datasetet som har sjukdomen
disease_proportion = df['disease'].mean()
print(f"\nAndel personer med sjukdom i datasetet: {disease_proportion:.4f} ({disease_proportion*100:.2f}%)")
print(f"Antal med sjukdom: {df['disease'].sum()} av {len(df)} deltagare")

# Använd numpy för att simulera 1000 slumpade personer med samma sannolikhet för sjukdom
n_simulations = 1000
simulated_disease = np.random.binomial(n=1, p=disease_proportion, size=n_simulations)
simulated_proportion = simulated_disease.mean()

print(f"\nSimulerad andel med sjukdom (1000 personer): {simulated_proportion:.4f} ({simulated_proportion*100:.2f}%)")
print(f"Skillnad från verklig andel: {abs(simulated_proportion - disease_proportion):.4f}")

# Jämför den simulerade andelen med den verkliga andelen
print("\nSkapar jämförelse: Verklig vs Simulerad andel sjukdom...")
plt.figure(figsize=(10, 6))

# Verklig andel
plt.axhline(y=disease_proportion, color='red', linestyle='--', linewidth=2, label=f'Verklig andel: {disease_proportion:.4f}')

# Simulerade proportioner (upprepade simuleringar för att visa variation)
n_repeats = 100
simulated_proportions = [np.random.binomial(n=1, p=disease_proportion, size=n_simulations).mean() for _ in range(n_repeats)]
plt.hist(simulated_proportions, bins=20, alpha=0.7, color='lightblue', edgecolor='black', label='Simulerade andelar')

plt.title('Jämförelse: Verklig vs Simulerad andel sjukdom')
plt.xlabel('Andel med sjukdom')
plt.ylabel('Frekvens')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('../output/del1_simulering_sjukdom.png')
plt.close()
print("Sparad som: ../output/del1_simulering_sjukdom.png")

# ============================================================================
# 3. KONFIDENSINTERVALL (G)
# ============================================================================
print("\n" + "=" * 80)
print("3. KONFIDENSINTERVALL (G)")
print("=" * 80)

# Beräkna ett konfidensintervall för medelvärdet av systolic_bp
systolic_bp_mean = df['systolic_bp'].mean()
systolic_bp_std = df['systolic_bp'].std()
n = len(df)

# 95% konfidensintervall
confidence_level = 0.95
z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)
margin_of_error = z_score * (systolic_bp_std / np.sqrt(n))
ci_lower = systolic_bp_mean - margin_of_error
ci_upper = systolic_bp_mean + margin_of_error

print(f"\nNormalapproximation - 95% Konfidensintervall för systolic_bp:")
print(f"  Medelvärde: {systolic_bp_mean:.2f} mmHg")
print(f"  Standardavvikelse: {systolic_bp_std:.2f} mmHg")
print(f"  Z-score: {z_score:.4f}")
print(f"  Marginal av fel: {margin_of_error:.4f} mmHg")
print(f"  95% CI: [{ci_lower:.2f}, {ci_upper:.2f}] mmHg")

# ============================================================================
# VG: KONFIDENSINTERVALL MED TVÅ OLIKA METODER
# ============================================================================
print("\n" + "=" * 80)
print("VG: KONFIDENSINTERVALL MED TVÅ OLIKA METODER")
print("=" * 80)

# Bootstrap-metod för konfidensintervall
n_bootstrap = 10000
bootstrap_means = []

for _ in range(n_bootstrap):
    sample = np.random.choice(df['systolic_bp'], size=n, replace=True)
    bootstrap_means.append(sample.mean())

bootstrap_means = np.array(bootstrap_means)

# Beräkna percentiler
ci_lower_bootstrap = np.percentile(bootstrap_means, 2.5)
ci_upper_bootstrap = np.percentile(bootstrap_means, 97.5)

print(f"\nBootstrap - 95% Konfidensintervall för systolic_bp:")
print(f"  Medelvärde av bootstrap-medel: {bootstrap_means.mean():.2f} mmHg")
print(f"  Standardavvikelse av bootstrap-medel: {bootstrap_means.std():.4f} mmHg")
print(f"  95% CI: [{ci_lower_bootstrap:.2f}, {ci_upper_bootstrap:.2f}] mmHg")

# Jämför resultaten
print(f"\n=== Jämförelse av metoder ===")
print(f"Normalapproximation: [{ci_lower:.2f}, {ci_upper:.2f}]")
print(f"Bootstrap:           [{ci_lower_bootstrap:.2f}, {ci_upper_bootstrap:.2f}]")
print(f"Skillnad i intervallbredd: {abs((ci_upper - ci_lower) - (ci_upper_bootstrap - ci_lower_bootstrap)):.4f} mmHg")

# Visualisera bootstrap-fördelningen
print("\nSkapar visualisering av bootstrap-fördelning...")
plt.figure(figsize=(12, 6))
plt.hist(bootstrap_means, bins=50, alpha=0.7, color='lightgreen', edgecolor='black', density=True)

# Lägg till normalapproximationen
x = np.linspace(bootstrap_means.min(), bootstrap_means.max(), 100)
pdf = stats.norm.pdf(x, bootstrap_means.mean(), bootstrap_means.std())
plt.plot(x, pdf, 'r-', linewidth=2, label='Normalfördelning')

# Märk ut konfidensintervall
plt.axvline(ci_lower_bootstrap, color='blue', linestyle='--', label='95% CI (Bootstrap)')
plt.axvline(ci_upper_bootstrap, color='blue', linestyle='--')
plt.axvline(systolic_bp_mean, color='black', linestyle='-', label='Sannt medelvärde')

plt.title('Bootstrap-fördelning av medelvärde för systolic_bp')
plt.xlabel('Medelvärde (mmHg)')
plt.ylabel('Densitet')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('../output/del1_bootstrap_forelning.png')
plt.close()
print("Sparad som: ../output/del1_bootstrap_forelning.png")

# ============================================================================
# 4. HYPOTESPROVNING (G)
# ============================================================================
print("\n" + "=" * 80)
print("4. HYPOTESPROVNING (G)")
print("=" * 80)

# Hypotes: "Rökare har högre medel-blodtryck än icke-rökare."
# H0: μ_rökare = μ_icke_rökare
# H1: μ_rökare > μ_icke_rökare (en-sidig test)

# Dela in data
smokers = df[df['smoker'] == 'Yes']['systolic_bp']
non_smokers = df[df['smoker'] == 'No']['systolic_bp']

print(f"\nAntal rökare: {len(smokers)}")
print(f"Antal icke-rökare: {len(non_smokers)}")
print(f"\nMedel-blodtryck:")
print(f"  Rökare: {smokers.mean():.2f} mmHg (std: {smokers.std():.2f})")
print(f"  Icke-rökare: {non_smokers.mean():.2f} mmHg (std: {non_smokers.std():.2f})")

# T-test
t_stat, p_val_one_tailed = stats.ttest_ind(smokers, non_smokers, equal_var=True, alternative='greater')

print(f"\n=== T-test (en-sidig) ===")
print(f"T-statistik: {t_stat:.4f}")
print(f"p-värde: {p_val_one_tailed:.4f}")

# Tolkning
alpha = 0.05
if p_val_one_tailed < alpha:
    print(f"Resultat: Förkasta H0 vid α={alpha}. Det finns signifikant bevis för att rökare har högre medel-blodtryck.")
else:
    print(f"Resultat: Kan inte förkasta H0 vid α={alpha}. Inget signifikant bevis för skillnad.")

# ============================================================================
# VG: PERMUTATIONSTEST OCH POWER-ANALYS
# ============================================================================
print("\n" + "=" * 80)
print("VG: PERMUTATIONSTEST OCH POWER-ANALYS")
print("=" * 80)

# Permutationstest (Bootstrap-metod)
observed_diff = smokers.mean() - non_smokers.mean()
n_permutations = 10000

# Kombinera all data
all_bp = np.concatenate([smokers, non_smokers])
n_smokers_obs = len(smokers)

# Permutationstest
permutation_diffs = []

for _ in range(n_permutations):
    # Slumpa om märkningen
    np.random.shuffle(all_bp)
    perm_smokers = all_bp[:n_smokers_obs]
    perm_non_smokers = all_bp[n_smokers_obs:]
    permutation_diffs.append(perm_smokers.mean() - perm_non_smokers.mean())

permutation_diffs = np.array(permutation_diffs)

# Beräkna p-värde (en-sidig: observerad skillnad > permutation)
p_val_perm = (permutation_diffs >= observed_diff).mean()

print(f"\n=== Permutationstest (Bootstrap) ===")
print(f"Observerad skillnad: {observed_diff:.4f} mmHg")
print(f"p-värde: {p_val_perm:.4f}")

# Tolkning
if p_val_perm < alpha:
    print(f"Resultat: Förkasta H0 vid α={alpha}. Det finns signifikant bevis för att rökare har högre medel-blodtryck.")
else:
    print(f"Resultat: Kan inte förkasta H0 vid α={alpha}. Inget signifikant bevis för skillnad.")

# Visualisera permutationstestet
print("\nSkapar visualisering av permutationstest...")
plt.figure(figsize=(12, 6))
plt.hist(permutation_diffs, bins=50, alpha=0.7, color='lightblue', edgecolor='black', density=True)

# Märk ut observerad skillnad
plt.axvline(observed_diff, color='red', linestyle='--', label=f'Observerad skillnad: {observed_diff:.2f}')

plt.title('Permutationsfördelning av skillnad i medel-blodtryck')
plt.xlabel('Skillnad i medel-blodtryck (Rökare - Icke-rökare) mmHg')
plt.ylabel('Densitet')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('../output/del1_permutationstest.png')
plt.close()
print("Sparad som: ../output/del1_permutationstest.png")

# Power-analysis
print(f"\n=== Power-Analys ===")
true_diff = observed_diff
n_sim = 1000
power_count = 0

# Standardavvikelse för pooling
pooled_std = np.sqrt(((len(smokers) - 1) * smokers.var() + 
                       (len(non_smokers) - 1) * non_smokers.var()) / 
                       (len(df) - 2))

power_results = []

for _ in range(n_sim):
    # Simulera data med verklig skillnad
    n_smokers_sim = len(smokers)
    n_non_smokers_sim = len(non_smokers)
    
    # Lägg till verklig skillnad till rökare
    smokers_sample = np.random.normal(non_smokers.mean() + true_diff, pooled_std, n_smokers_sim)
    non_smokers_sample = np.random.normal(non_smokers.mean(), pooled_std, n_non_smokers_sim)
    
    # T-test
    t_stat_sim, p_val_sim = stats.ttest_ind(smokers_sample, non_smokers_sample, equal_var=True)
    power_results.append(p_val_sim)
    if p_val_sim < alpha:
        power_count += 1

power = power_count / n_sim
print(f"Verklig skillnad: {true_diff:.2f} mmHg")
print(f"Power (sannolikhet att upptäcka skillnad): {power:.4f} ({power*100:.2f}%)")

# Visualisera p-värden från power-analysen
print("\nSkapar visualisering av power-analys...")
plt.figure(figsize=(10, 6))
plt.hist(power_results, bins=50, alpha=0.7, color='lightcoral', edgecolor='black')
plt.axvline(alpha, color='red', linestyle='--', label=f'Signifikansnivå (α={alpha})')
plt.title('Fördelning av p-värden i power-analys')
plt.xlabel('p-värde')
plt.ylabel('Frekvens')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('../output/del1_power_analys.png')
plt.close()
print("Sparad som: ../output/del1_power_analys.png")

# ============================================================================
# METODVAL OCH MOTIVERING (VG)
# ============================================================================
print("\n" + "=" * 80)
print("VG: METODVAL OCH MOTIVERING")
print("=" * 80)

print("""
### Konfidensintervall

**Normalapproximation:**
- Fördelar: Snabb och analytisk lösning. Kräver bara medelvärde, standardavvikelse och stickprovsstorlek.
- Nackdelar: Förutsätter normalfördelning av stickprovsmedelvärdet, vilket kräver tillräckligt stor stickprovsstorlek (n > 30).
- Motivering: Med n=800 är centrala gränsvärdessatsen tillämpbar, så normalapproximationen är rimlig.
- Källa: Central Limit Theorem (CLT) - se scipy.stats.norm dokumentation.

**Bootstrap:**
- Fördelar: Icke-parametrisk metod som inte kräver antaganden om underliggande fördelning. fungerar bra för mindre stickprov.
- Nackdelar: Beräkningsmässigt intensiv. Resultatet kan variera beroende på antalet bootstrap-iterationer.
- Motivering: Ger en empirisk fördelning av stickprovsstatistikan och är robust mot icke-normala data.
- Källa: Efron, B. (1979). "Bootstrap Methods: Another Look at the Jackknife". Annals of Statistics.

### Hypotesprövning

**T-test:**
- Fördelar: Standardmetod för jämförelse av medelvärden. Effektiv när antagandena (normalfördelning, lika varianser) är uppfyllda.
- Nackdelar: Känslig för avvikelser från normalfördelning och olika varianser.
- Motivering: Med stora stickprov (n_rökare > 100, n_icke_rökare > 500) är t-testet robust.
- Källa: Student's t-test - scipy.stats.ttest_ind

**Permutationstest:**
- Fördelar: Icke-parametrisk, kräver inga antaganden om fördelning. Exakt test för små stickprov.
- Nackdelar: Beräkningsmässigt intensiv för stora stickprov.
- Motivering: Ger en empirisk p-värdesberäkning genom att slumpa om märkningen, vilket är särskilt användbart när fördelningsantaganden är tveksamma.
- Källa: Fisher, R.A. (1935). "The Design of Experiments".

### Power-analys

Motivering: Power-analysen visar hur stor sannolikhet vi har att upptäcka en verklig skillnad. Med den observerade skillnaden har vi en power som visar vår förmåga att upptäcka denna effektstorlek med vårt stickprov.
Källa: Cohen, J. (1988). "Statistical Power Analysis for the Behavioral Sciences".
""")

print("\n" + "=" * 80)
print("DEL 1 SLUTFÖR")
print("=" * 80)
