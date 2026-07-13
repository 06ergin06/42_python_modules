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
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
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
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
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
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                for k, v in item.items():
                    if not (isinstance(k, str) and isinstance(v, str)):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                if "log_level" in item:
                    level = item.get("log_level", "")
                    msg = item.get("log_message", "")
                    log_str = f"{level}: {msg}"
                else:
                    log_str = str(item)

                self._storage.append((self._rank_counter, log_str))
                self._rank_counter += 1
        else:
            if "log_level" in data:
                level = data.get("log_level", "")
                msg = data.get("log_message", "")
                log_str = f"{level}: {msg}"
            else:
                log_str = str(data)
            self._storage.append((self._rank_counter, log_str))
            self._rank_counter += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed: bool = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error: Can't process "
                    f"element in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            name: str = processor.__class__.__name__
            name = name.replace("Processor", " Processor")
            total: int = processor._rank_counter
            remain: int = len(processor._storage)
            print(
                f"{name}: total {total} processed, "
                f"remaining {remain} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    stream: DataStream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num_pro: NumericProcessor = NumericProcessor()
    stream.register_processor(num_pro)
    batch = [
            "Hello world",
            [3.14, 1, 2.71],
            [
                {"log_level": "WARNING", "log_message":
                    "Telnet access! Use ssh instead"},
                {"log_level": "INFO", "log_message": "User wil is connected"},
            ],
            42,
            ["Hi", "five"],
        ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    print("Send the same batch again")
    txt_pro: TextProcessor = TextProcessor()
    log_pro: LogProcessor = LogProcessor()
    stream.register_processor(txt_pro)
    stream.register_processor(log_pro)
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors:"
        " Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        num_pro.output()
    for _ in range(2):
        txt_pro.output()
    for _ in range(1):
        log_pro.output()
    stream.print_processors_stats()
