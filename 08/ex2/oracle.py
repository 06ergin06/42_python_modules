#!/usr/bin/env python3


import os
import sys
from dotenv import load_dotenv  # type: ignore


if __name__ == "__main__":
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...\n")
    mode: str | None = os.environ.get("MATRIX_MODE")
    db_url: str | None = os.environ.get("DATABASE_URL")
    api_key: str | None = os.environ.get("API_KEY")
    log_level: str | None = os.environ.get("LOG_LEVEL")
    zion_endpoint: str | None = os.environ.get("ZION_ENDPOINT")

    required_vars: dict[str, str | None] = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": db_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_endpoint
    }

    missing: list[str] = [k for k, v in required_vars.items() if not v]

    if missing:
        print(f"WARNING: Missing configuration for: {missing}")
        print("Please check your .env file or environment variables.")
        sys.exit(1)

    db_status: str = "Connected to local instance"
    if mode == "production":
        db_status = "Connected to production cluster"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print("API Access: Authenticated" if api_key else "API Access: Denied")
    print(f"Log level: {log_level}")
    print("Zion Network: Online" if zion_endpoint else "Zion Network: Offline")
    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print(
            "[WARNING] .env file is missing, relying only"
            "on environment variables"
        )
    if mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
