from qiskit import QuantumCircuit

# 1. Create a circuit with 2 qubits
qc = QuantumCircuit(2)

# 2. Add a Hadamard gate to qubit 0
qc.h(0)

# 3. Add a CNOT gate (control=0, target=1)
qc.cx(0, 1)

# 4. Draw and save the figure as an image
# (Requires 'pylatexenc' installed for the clean 'mpl' style)
fig = qc.draw(output='mpl')
fig.savefig('bell_state_circuit.png', bbox_inches='tight', dpi=300)
