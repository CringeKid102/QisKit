"""
HCNOT (Hadamard + CNOT) circuit for creating a Bell state
"""

from qiskit import QuantumCircuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
fig = qc.draw(output='mpl')
fig.savefig('bell_state_circuit.png', bbox_inches='tight', dpi=300)
