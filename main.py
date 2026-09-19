"""
EE simulation script
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator, partial_trace, entropy, purity
from qiskit.visualization import plot_bloch_multivector, plot_state_qsphere

# Build a 1-qubit circuit and apply each gate
for gate_name, apply_gate in [("X", lambda qc: qc.x(0)),
                               ("Z", lambda qc: qc.z(0)),
                               ("H", lambda qc: qc.h(0))]:
    qc = QuantumCircuit(1)
    apply_gate(qc)
    state = Statevector.from_instruction(qc)
    print(f"{gate_name}|0> = {state}")

for gate_name, apply_gate in [("X", lambda qc: qc.x(0)),
                               ("Z", lambda qc: qc.z(0)),
                               ("H", lambda qc: qc.h(0))]:
    qc = QuantumCircuit(1)
    apply_gate(qc)
    U = Operator(qc).data
    is_unitary = np.allclose(U.conj().T @ U, np.eye(U.shape[0]))
    print(f"{gate_name} matrix:\n{U}\nUnitary? {is_unitary}\n")

qc_bell = QuantumCircuit(2)
qc_bell.h(0)
qc_bell.cx(0, 1)
bell_state = Statevector.from_instruction(qc_bell)

reduced_bell = partial_trace(bell_state, [1])
print("Reduced density matrix of qubit 0:\n", reduced_bell.data)
print("Purity:", purity(reduced_bell))
print("Von Neumann entropy (bits):", entropy(reduced_bell, base=2))

qc_sep = QuantumCircuit(2)
qc_sep.h(0)
sep_state = Statevector.from_instruction(qc_sep)
reduced_sep = partial_trace(sep_state, [1])
print("Purity of separable state:", purity(reduced_sep), " (should be 1.0)")

# Bloch sphere for a single qubit in the |+> state
qc_plus = QuantumCircuit(1)
qc_plus.h(0)
plus_state = Statevector.from_instruction(qc_plus)
fig2 = plot_bloch_multivector(plus_state)
fig2.savefig("bloch_plus_qiskit.png", dpi=150)
print("Saved bloch_plus_qiskit.png")

# Q-sphere for the Bell state
fig3 = plot_state_qsphere(bell_state)
fig3.savefig("bell_qsphere.png", dpi=150)
print("Saved bell_qsphere.png")