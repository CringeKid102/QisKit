# QisKit

EE simulation script using Qiskit to demonstrate core quantum computing concepts:

- Single-qubit gate action on \(|0\rangle\)
- Unitarity checks for common gates
- Bell state construction with Hadamard + CNOT
- Entanglement evidence via reduced density matrix, purity, and entropy
- Visual outputs (circuit diagram, Bloch sphere, Q-sphere)

## What This Project Covers

### Section 4.1: Gate Matrices as Operators
Applies X, Z, and H gates to a one-qubit state and prints the resulting statevectors.

### Section 4.2: Unitarity and Physical Constraint
Extracts matrix representations for X, Z, and H and verifies unitarity numerically.

### Section 5.1 and 5.2: Bell State Construction
Builds a two-qubit Bell circuit:

1. Apply Hadamard to qubit 0
2. Apply CNOT with control 0 and target 1

Expected Bell state:
\[
\frac{1}{\sqrt{2}}\left(|00\rangle + |11\rangle\right)
\]

### Section 5.3: Non-Factorizability Check
Uses partial trace to obtain the reduced state and evaluates:

- Purity
- Von Neumann entropy

For an entangled Bell state, purity drops below 1 and entropy is greater than 0.

## Requirements

- Python 3.10+
- qiskit
- qiskit-aer
- numpy
- matplotlib

## Setup

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

```bash
pip install qiskit qiskit-aer numpy matplotlib
```

## Run

```bash
python main.py
```

The script prints intermediate results and saves figures to the project root.

## Histogram Evidence

`histogram.py` compares an ideal Aer simulation with a second Aer simulation
that uses manually specified gate and readout error probabilities. It does not
submit a job to real IBM Quantum hardware or use measured device calibration
data. Describe the figure as an ideal-versus-noisy simulation comparison, not
as a comparison with real IBM quantum hardware.

## Generated Files

Running the script produces:

- `bell_circuit_qiskit.png`
- `bloch_plus_qiskit.png`
- `bell_qsphere.png`

## Notes

The script includes a comparison against a separable two-qubit state (without CNOT) to highlight the difference between entangled and non-entangled cases.
