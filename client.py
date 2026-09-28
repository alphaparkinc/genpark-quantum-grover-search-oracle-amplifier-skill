from typing import Dict, Any

class GroverSearchSimulator:
    @staticmethod
    def search_2qubit(target_item: str = "11") -> Dict[str, Any]:
        target_idx = int(target_item, 2)
        state = [complex(0.5, 0.0)] * 4
        state[target_idx] = -state[target_idx]
        mean_amp = sum(state) / 4.0
        state = [2.0 * mean_amp - amp for amp in state]
        probs = {format(i, '02b'): round(abs(c) ** 2, 4) for i, c in enumerate(state)}
        return {"target": target_item, "final_probabilities": probs, "success_rate": probs.get(target_item, 0.0)}

    def benchmark_grover_search(self) -> Dict[str, Any]:
        return self.search_2qubit("10")
