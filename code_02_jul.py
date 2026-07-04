from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

circuit = QuantumCircuit(2, 2)

circuit.h(0)
circuit.cx(0, 1)

circuit.measure([0, 1], [0, 1])

sim = AerSimulator()
circuitSim1 = sim.run(circuit, shots=1024).result()
circuitSim2 = sim.run(circuit, shots=4096).result()
circuitSim3 = sim.run(circuit, shots=8192).result()

result1 = circuitSim1.get_counts()
result2 = circuitSim2.get_counts()
result3 = circuitSim3.get_counts()

print("Result for 1024 shots: ", result1)
print("Result for 4096 shots: ", result2)
print("Result for 8192 shots: ", result3)

# circuit.draw("mpl")
# plt.show()