import random

# Step 1: Alice generates random bits and random bases
def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]

# Step 2: Bob measures the qubits
def measure_qubits(alice_bits, alice_bases, bob_bases):
    measured_bits = []
    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            measured_bits.append(alice_bits[i])
        else:
            measured_bits.append(random.randint(0, 1))
    return measured_bits

# Step 3: Sift the key (keep only matching bases)
def sift_key(bits, alice_bases, bob_bases):
    return [bits[i] for i in range(len(bits)) if alice_bases[i] == bob_bases[i]]

# Step 4: Calculate QBER
def calculate_qber(alice_key, bob_key):
    errors = sum(1 for i in range(len(alice_key)) if alice_key[i] != bob_key[i])
    return errors / len(alice_key) if len(alice_key) > 0 else 0

# Simulation
def bb84_simulation(n=20):
    print("---- BB84 Quantum Key Distribution Simulation ----\n")

    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)
    bob_bases = generate_bases(n)

    bob_measured = measure_qubits(alice_bits, alice_bases, bob_bases)

    alice_key = sift_key(alice_bits, alice_bases, bob_bases)
    bob_key = sift_key(bob_measured, alice_bases, bob_bases)

    qber = calculate_qber(alice_key, bob_key)

    print("Alice Bits      :", alice_bits)
    print("Alice Bases     :", alice_bases)
    print("Bob Bases       :", bob_bases)
    print("Bob Measured    :", bob_measured)
    print("\nSifted Key (Alice):", alice_key)
    print("Sifted Key (Bob)  :", bob_key)
    print("\nQBER:", qber)

    if qber > 0.2:
        print("⚠️ Possible Eavesdropping Detected!")
    else:
        print("✅ Secure Key Established Successfully!")

# Run the simulation
if __name__ == "__main__":
    bb84_simulation(30)