"""
Problem 1 — Accumulator (stateful counter for AI pipelines)
- Track a running sum without global variables.
- Educate: @property (read-only) + guarded setter that blocks misuse.
"""

class Accumulator:
    def __init__(self, start: float = 0.0) -> None:
        """
        누산기를 초기화합니다.
        """
        self._total = float(start)  # 내부 상태 저장

    @property
    def total(self) -> float:
        """
        현재 누적값 (읽기 전용)
        """
        return self._total

    @total.setter
    def total(self, value: float) -> None:
        """
        직접 할당을 막는 가드
        """
        raise AssertionError("Direct assignment to 'total' is not allowed. Use add() or reset().")

    def add(self, x: float) -> float:
        """
        x를 더한 후 현재 합계를 반환
        """
        self._total += float(x)
        return self._total

    def reset(self) -> None:
        """
        합계를 0.0으로 리셋
        """
        self._total = 0.0


if __name__ == "__main__":
    def run_tests():
        acc = Accumulator()
        assert acc.add(3) == 3.0
        assert acc.add(4.5) == 7.5
        assert acc.total == 7.5
        acc.reset()
        assert acc.total == 0.0

        # 새로운 객체 테스트
        acc2 = Accumulator(start=10)
        assert acc2.total == 10.0
        assert acc2.add(5) == 15.0

        print("✅ All tests passed!")

    run_tests()
