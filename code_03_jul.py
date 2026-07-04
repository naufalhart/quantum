from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime.fake_provider import FakeBrisbane
from qiskit_aer import AerSimulator


# Bell State Circuit
circuit = QuantumCircuit(2, 2)

circuit.h(0)
circuit.cx(0, 1)

circuit.measure([0, 1], [0, 1])

with open("results.txt", "w") as f:

    # Standard Simulator
    f.write("Standard testing\n")

    sim = AerSimulator()

    for _ in range(20):
        circuitSim1 = sim.run(circuit, shots=1024).result()
        circuitSim2 = sim.run(circuit, shots=4096).result()
        circuitSim3 = sim.run(circuit, shots=8192).result()

        result1 = circuitSim1.get_counts()
        result2 = circuitSim2.get_counts()
        result3 = circuitSim3.get_counts()

        f.write(f"Result for 1024 shots: {result1}\n")
        f.write(f"Result for 4096 shots: {result2}\n")
        f.write(f"Result for 8192 shots: {result3}\n")

        f.write("\n")


    # Fake IBM Quantum Backend
    f.write("Quantum hardware replication testing\n")

    fake_backend = FakeBrisbane()

    simulator = AerSimulator.from_backend(fake_backend)

    compiled = transpile(circuit, simulator)

    for _ in range(20):
        job1 = simulator.run(compiled, shots=1024)
        job2 = simulator.run(compiled, shots=4096)
        job3 = simulator.run(compiled, shots=8192)

        result1 = job1.result()
        result2 = job2.result()
        result3 = job3.result()

        counts1 = result1.get_counts()
        counts2 = result2.get_counts()
        counts3 = result3.get_counts()
        
        f.write(f"Result for 1024 shots: {counts1}\n")
        f.write(f"Result for 4096 shots: {counts2}\n")
        f.write(f"Result for 8192 shots: {counts3}\n")
        f.write("\n")