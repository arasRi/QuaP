import sys

def check(name, version_expected):
    try:
        mod = __import__(name)
        version = getattr(mod, '__version__', 'unknown')
        status = "✅" if version == version_expected else "⚠️"
        print(f"{status} {name:25s} {version:15s} (expected: {version_expected})")
        return True
    except ImportError as e:
        print(f"❌ {name:25s} FAILED: {e}")
        return False

print(f"Python: {sys.version}\n")
print("=" * 60)

check('numpy', '1.26.4')
check('scipy', '1.11.4')
check('pandas', '2.2.2')
check('sklearn', '1.5.2')
check('matplotlib', '3.9.2')
check('qiskit', '1.2.4')
check('qiskit_aer', '0.15.1')
check('qiskit_machine_learning', '0.8.1')
check('qiskit_algorithms', '0.3.1')
check('pennylane', '0.44.1')
check('autoray', '0.8.2')
check('autograd', '1.8.0')

print("=" * 60)

# Test import kritis
try:
    from qiskit_machine_learning.algorithms import VQC, QSVC
    from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
    from qiskit.primitives import StatevectorSampler
    print("\n✅ Qiskit ML imports OK")
except Exception as e:
    print(f"\n❌ Qiskit ML import FAILED: {e}")

try:
    import pennylane as qml
    dev = qml.device("default.qubit", wires=2)
    @qml.qnode(dev)
    def test():
        qml.Hadamard(0)
        return qml.expval(qml.PauliZ(0))
    print(f"✅ PennyLane OK (test result: {test():.4f})")
except Exception as e:
    print(f"❌ PennyLane FAILED: {e}")

print("\n🎉 Verifikasi selesai!")