

def hill_climbing(signal):
    """Hill climbing to find strongest signal"""
    current = 0
    print(f"Starting at Tower {current} with signal {signal[current]}")

    while current < len(signal) - 1:
        # Compare current with adjacent tower
        if signal[current + 1] > signal[current]:
            print(f"Moving Tower {current} ({signal[current]}) -> Tower {current+1} ({signal[current+1]})")
            current += 1
        else:
            print(f"No better neighbour than Tower {current}")
            break

    return current, signal[current]

# Step 1: Define a list of tower signals
signals = [3, 5, 8, 12, 15, 10, 6]
# You can also take input: signals = list(map(int, input("Enter signals: ").split()))

# Step 2: Start from the first tower
# Step 3 & 4: Compare and repeat until no higher signal
index, strength = hill_climbing(signals)

# Step 5: Display the strongest signal and its position
print("\n--- Result ---")
print(f"Signal strengths: {signals}")
print(f"Best Tower Index: {index}")
print(f"Strongest Signal: {strength}")
