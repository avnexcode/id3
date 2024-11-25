import numpy as np
from math import log2


def calculate_entropy(pos_count, neg_count):
    total = pos_count + neg_count
    p_pos = pos_count / total if total > 0 else 0
    p_neg = neg_count / total if total > 0 else 0

    entropy = 0
    if p_pos > 0:
        entropy -= p_pos * log2(p_pos)
    if p_neg > 0:
        entropy -= p_neg * log2(p_neg)
    return entropy


def calculate_gain(total_entropy, split_counts):
    total_samples = sum(sum(counts) for counts in split_counts.values())
    weighted_entropy = 0

    for counts in split_counts.values():
        subset_samples = sum(counts)
        subset_entropy = calculate_entropy(counts[0], counts[1])
        weighted_entropy += (subset_samples / total_samples) * subset_entropy

    return total_entropy - weighted_entropy


# Data yang diberikan
total_samples = 10
cheat_yes = 3
cheat_no = 7

# Menghitung Entropy total dataset
total_entropy = calculate_entropy(cheat_yes, cheat_no)
print(f"\nTotal Entropy: {total_entropy:.6f}")

# Menghitung entropy untuk masing-masing atribut
print("\nEntropy untuk setiap kategori:")

# REFUND
p_refund_yes = 3 / 10  # P(Yes)
p_refund_no = 7 / 10  # P(No)
entropy_refund = calculate_entropy(3, 7)
print(f"Entropy REFUND: {entropy_refund:.6f}")

# MARITAL STATUS
p_single = 6 / 10  # P(Single)
p_married = 4 / 10  # P(Married)
entropy_marital = calculate_entropy(6, 4)
print(f"Entropy MARITAL STATUS: {entropy_marital:.6f}")

# TAXABLE INCOME
p_income_low = 3 / 10  # P(<80K)
p_income_high = 7 / 10  # P(>=80K)
entropy_income = calculate_entropy(3, 7)
print(f"Entropy TAXABLE INCOME: {entropy_income:.6f}")


# Menghitung gain untuk masing-masing atribut
print("\nGain untuk setiap kategori:")

# REFUND
refund_splits = {
    "Yes": [0, 3],  # [cheat_yes, cheat_no] untuk REFUND=Yes
    "No": [3, 4],  # [cheat_yes, cheat_no] untuk REFUND=No
}
gain_refund = calculate_gain(total_entropy, refund_splits)
print(f"Gain REFUND: {gain_refund:.6f}")

# MARITAL STATUS
marital_splits = {
    "Single": [3, 3],  # [cheat_yes, cheat_no] untuk Single
    "Married": [0, 4],  # [cheat_yes, cheat_no] untuk Married
}
gain_marital = calculate_gain(total_entropy, marital_splits)
print(f"Gain MARITAL STATUS: {gain_marital:.6f}")

# TAXABLE INCOME
taxable_splits = {
    "<80": [3, 0],  # [cheat_yes, cheat_no] untuk <80
    ">=80": [0, 7],  # [cheat_yes, cheat_no] untuk >=80
}
gain_taxable = calculate_gain(total_entropy, taxable_splits)
print(f"Gain TAXABLE INCOME: {gain_taxable:.6f}")
