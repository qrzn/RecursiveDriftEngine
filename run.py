#!/usr/bin/env python3
"""
Recursive Drift Engine Launcher
Simple launcher that runs the working terminal version
"""

import subprocess
import sys
import os

def main():
    """Launch the Recursive Drift Engine terminal interface"""
    try:
        # Run the simple terminal version
        subprocess.run([sys.executable, "simple_main.py"], check=True)
    except FileNotFoundError:
        print("Error: simple_main.py not found in current directory")
        print("Make sure you're running this from the project root directory")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDrift field interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Error launching Recursive Drift Engine: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()