#!/usr/bin/env python3

import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self._storage: list[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("Data is missing.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if not data:
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._rank_counter, str(item)))
                self._rank_counter += 1
        else:
            self._storage.append((self._rank_counter, str(data)))
            self._rank_counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if not data:
            return False
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._rank_counter, str(item)))
                self._rank_counter += 1
        else:
            self._storage.append((self._rank_counter, str(data)))
            self._rank_counter += 1


class LogProcessor(DataProcessor):
    def _is_valid_log_entry(self, item: typing.Any) -> bool:
        if not isinstance(item, dict):
            return False
        for k, v in item.items():
            if not (isinstance(k, str) and isinstance(v, str)):
                return False
        return True

    def validate(self, data: typing.Any) -> bool:
        if not data:
            return False
        if isinstance(data, dict):
            return self._is_valid_log_entry(data)
        if isinstance(data, list):
            return all(self._is_valid_log_entry(item) for item in data)
        return False

    def _format_log(self, item: dict[str, str]) -> str:
        if "log_level" in item:
            return (
                f"{item.get('log_level', '')}:"
                f" {item.get('log_message', '')}"
            )
        return str(item)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for item in items:
            log_str: str = self._format_log(item)
            self._storage.append((self._rank_counter, log_str))
            self._rank_counter += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    num_pro: NumericProcessor = NumericProcessor()
    txt_pro: TextProcessor = TextProcessor()
    log_pro: LogProcessor = LogProcessor()

    print("\nTesting Numeric Processor...")
    print(f"Trying to validate input '42': {num_pro.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_pro.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_pro.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    num_pro.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_pro.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {txt_pro.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    txt_pro.ingest(["Hello", "Nexus", "World"])
    rank, val = txt_pro.output()
    print("Extracting 1 values...")
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    print(f"Trying to validate input 'Hello': {log_pro.validate('Hello')}")
    logs: list[dict[str, str]] = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {logs}")
    log_pro.ingest(logs)
    for _ in range(2):
        rank, val = log_pro.output()
        print(f"Log entry {rank}: {val}")
