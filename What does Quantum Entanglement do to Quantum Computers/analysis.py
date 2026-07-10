import ast
import re
import numpy as np

def read_result_file(filename):

    datasets = {
        "Standard testing": {},
        "Quantum hardware replication testing": {}
    }

    current_section = None

    with open(filename, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            if line == "Standard testing":
                current_section = "Standard testing"
                continue

            if line == "Quantum hardware replication testing":
                current_section = "Quantum hardware replication testing"
                continue

            m = re.match(r"Result for (\d+) shots:\s*(.*)", line)

            if m:

                shots = int(m.group(1))
                counts = ast.literal_eval(m.group(2))

                if shots not in datasets[current_section]:
                    datasets[current_section][shots] = []

                datasets[current_section][shots].append(counts)

    return datasets

def analyze(dataset):

    for shots in sorted(dataset.keys()):

        trials = dataset[shots]

        bitstrings = sorted({
            bit
            for trial in trials
            for bit in trial.keys()
        })

        print("="*60)
        print(f"{shots} shots")
        print("-"*60)

        print(f"{'Bit':<5}{'Mean':>12}{'Std':>12}")

        for bit in bitstrings:

            probabilities = []

            for trial in trials:

                count = trial.get(bit, 0)
                probabilities.append(count / shots)

            mean = np.mean(probabilities)
            std = np.std(probabilities, ddof=1)

            print(f"{bit:<5}{mean:>12.6f}{std:>12.6f}")

        print()


datasets = read_result_file("results.txt")

print("\nSTANDARD TESTING\n")
analyze(datasets["Standard testing"])

print("\nQUANTUM HARDWARE REPLICATION TESTING\n")
analyze(datasets["Quantum hardware replication testing"])