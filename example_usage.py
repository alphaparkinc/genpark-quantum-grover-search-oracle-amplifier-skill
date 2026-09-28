from client import GroverSearchSimulator

def run_example():
    print("=== GenPark Grover Search Example ===")
    sim = GroverSearchSimulator()
    print("Grover Search Result:", sim.benchmark_grover_search())

if __name__ == "__main__":
    run_example()
