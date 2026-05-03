def 
get_adjectival_equivalent(grade):
    if 96 <= grade <= 100:
        return "EXCELLENT"
    elif 90 <= grade < 96:
        return "VERY GOOD"
    elif 84 <= grade < 90:
        return "VERY GOOD"
    elif 78 <= grade < 84:
        return "GOOD"
    elif 72 <= grade < 78:
        return "GOOD"
    elif 66 <= grade < 72:
        return "SATISFACTORY"
    elif 60 <= grade < 66:
        return "SATISFACTORY"
    elif 55 <= grade < 60:
        return "FAIR"
    elif 50 <= grade < 55:
        return "FAIR"
    elif 40 <= grade < 50:
        return "FAILED ON CONDITION"
    else:
        return "FAILED"

print("\n--- RESULTS ---")
print(f"Q1 Grade: {Q1:.2f}")
print(f"Q2 Grade: {Q2:.2f}")
print(f"Q3 Grade: {Q3:.2f}")
print(f"Final Grade (Q4): {Q4:.2f}")
print(f"Adjectival Equivalent: {get_adjectival_equivalent(Q4)}")
