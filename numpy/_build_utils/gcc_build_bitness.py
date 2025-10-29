#!/usr/bin/env python3
"""Detect the bitness (32 or 64) of the MinGW-w64 GCC build target on Windows."""

import subprocess
import sys

def main():
    try:
        result = subprocess.run(
            ["gcc", "-dumpmachine"],
            check=True,
            text=True,
            capture_output=True
        )
        target = result.stdout.strip()

        if target.startswith("i686"):
            print("32")
        elif target.startswith("x86_64"):
            print("64")
        else:
            raise ValueError(f"Unrecognized GCC target: {target}")

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
