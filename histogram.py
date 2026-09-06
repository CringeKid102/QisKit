"""
Compares an ideal (noiseless) Bell-state simulation against a noisy simulation
that approximates real IBM Quantum hardware, using gate/readout error rates
typical of IBM's superconducting-qubit devices.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, ReadoutError
from qiskit.visualization import plot_histogram

# Build the Bell-state circuit
qc_bell = QuantumCircuit(2)
qc_bell.h(0)
qc_bell.cx(0, 1)

qc_bell_measured = qc_bell.copy()
qc_bell_measured.measure_all()

SHOTS = 1000

# Ideal simulation — no noise
ideal_sim = AerSimulator()
ideal_result = ideal_sim.run(qc_bell_measured, shots=SHOTS).result()
ideal_counts = ideal_result.get_counts()

# Noise model approximating typical IBM Quantum hardware error rates:
# ~0.05% error on single-qubit gates, ~1% on two-qubit gates, ~2% readout error
noise_model = NoiseModel()
noise_model.add_all_qubit_quantum_error(depolarizing_error(0.0005, 1), ["h"])
noise_model.add_all_qubit_quantum_error(depolarizing_error(0.01, 2), ["cx"])
noise_model.add_all_qubit_readout_error(
    ReadoutError([[0.98, 0.02], [0.02, 0.98]])
)

noisy_sim = AerSimulator(noise_model=noise_model)
qc_transpiled = transpile(qc_bell_measured, noisy_sim)
noisy_result = noisy_sim.run(qc_transpiled, shots=SHOTS).result()
noisy_counts = noisy_result.get_counts()

fig4 = plot_histogram(
    [ideal_counts, noisy_counts],
    legend=["Ideal simulation", "Real hardware-like simulation"],
)
fig4.savefig("bell_histogram_qiskit.png", dpi=150)
print("Saved bell_histogram_qiskit.png")