from json import load
from math import sqrt


def load_journal(file):
    with open(file) as f:
        data = load(f)
    return list(data)


def compute_phi(file, event):
    n_11 = 0
    n_00 = 0
    n_10 = 0
    n_01 = 0
    n_1_plus = 0
    n_0_plus = 0
    n_plus_1 = 0
    n_plus_0 = 0
    for f in file:
        if event in f["events"] and f["squirrel"]:
            n_11 += 1
        elif event not in f["events"] and not f["squirrel"]:
            n_00 += 1
        elif event in f["events"] and not f["squirrel"]:
            n_10 += 1
        elif event not in f["events"] and f["squirrel"]:
            n_01 += 1
        if event in f["events"]:
            n_1_plus += 1
        if event not in f["events"]:
            n_0_plus += 1
        if f["squirrel"]:
            n_plus_1 += 1
        if not f["squirrel"]:
            n_plus_0 += 1
    phi = (n_11 * n_00 - n_10 * n_01) / sqrt(n_1_plus * n_0_plus * n_plus_1 * n_plus_0)
    return phi


def compute_correlations(file):
    event_correlation = {}
    journal = load_journal(file)
    for j in journal:
        for event in j["events"]:
            phi = compute_phi(journal, event)
            event_correlation[event] = phi

    return event_correlation


def diagnose():
    file = "journal.json"
    corr = compute_correlations(file)
    dilemma = max(zip(corr.values(), corr.keys()))[1]
    solution = min(zip(corr.values(), corr.keys()))[1]
    print(
        f"""Scott, you should avoid {dilemma}
and you should {solution} everyday.
"""
    )


def main():
    diagnose()


if __name__ == "__main__":
    main()
