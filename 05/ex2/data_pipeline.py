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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = [val for _, val in data]
        print(", ".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_parts = [f'"{f"item_{rank}"}": "{val}"' for rank, val in data]
        print("{" + ", ".join(json_parts) + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            ext_data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    ext_data.append(processor.output())
                except IndexError:
                    break

            if ext_data:
                plugin.process_output(ext_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...\n")
    stream: DataStream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    batch: list[typing.Any] = [
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

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plug: CSVExportPlugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plug)
    stream.print_processors_stats()
    batch_2: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch_2}")
    stream.process_stream(batch_2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plug: JSONExportPlugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plug)
    stream.print_processors_stats()
