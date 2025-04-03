# Makefile for Inventory Management System
# Usage:
#   make console    - Run the console version (Stock.py)
#   make gui        - Run the GUI version (UI2.py)
#   make clean      - Clean up generated files
#   make help       - Show this help

.PHONY: console gui clean help

PYTHON = python

console:
	@echo "Starting Console Version..."
	@$(PYTHON) Stock.py

gui:
	@echo "Starting GUI Version..."
	@$(PYTHON) UI2.py

clean:
	@echo "Cleaning up..."
	@if exist exported_inventory.csv del exported_inventory.csv
	@echo "Original data files (Estock.csv, data.csv) are preserved"

help:
	@echo "Inventory Management System Makefile"
	@echo "Available targets:"
	@echo "  console    - Run the console version (Stock.py)"
	@echo "  gui        - Run the GUI version (UI2.py)"
	@echo "  clean      - Clean up generated files"
	@echo "  help       - Show this help message"