param (
    [string]$Command = "help"
)

function Show-Help {
    Write-Host "Inventory Management System"
    Write-Host ""
    Write-Host "Usage:"
    Write-Host "  .\run.ps1 console    - Run the console version (Stock.py)"
    Write-Host "  .\run.ps1 gui        - Run the GUI version (UI2.py)"
    Write-Host "  .\run.ps1 clean      - Clean up generated files"
    Write-Host "  .\run.ps1 help       - Show this help"
    Write-Host ""
}

switch ($Command) {
    "console" {
        Write-Host "Starting Console Version..."
        python Stock.py
    }
    "gui" {
        Write-Host "Starting GUI Version..."
        python UI2.py
    }
    "clean" {
        Write-Host "Cleaning up..."
        if (Test-Path "exported_inventory.csv") {
            Remove-Item "exported_inventory.csv"
        }
        Write-Host "Original data files (Estock.csv, data.csv) are preserved"
    }
    "help" {
        Show-Help
    }
    default {
        Show-Help
    }
}
