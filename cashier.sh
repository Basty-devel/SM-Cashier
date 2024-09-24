#!/bin/bash

# Function to activate the virtual environment
activate_venv() {
    echo "Activating virtual environment..."
    source venv/bin/activate
}

# Function to deactivate the virtual environment
deactivate_venv() {
    echo "Deactivating virtual environment..."
    deactivate
}

# Function to check if tkinter is installed (specifically for Linux)
check_tkinter() {
    python -c "import tkinter" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "Tkinter is not installed. Installing Tkinter..."
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            # On Linux, we need to install Tkinter via package manager
            sudo apt-get install python3-tk -y
        else
            echo "Tkinter should be installed by default on MacOS and Windows."
        fi
    else
        echo "Tkinter is already installed."
    fi
}

# Interactive prompt to proceed
echo "Welcome to the Cashier System setup!"
read -p "Do you want to set up the virtual environment and run the application? (y/n): " choice

if [[ "$choice" != "y" && "$choice" != "Y" ]]; then
    echo "Exiting the setup. Goodbye!"
    exit 0
fi

# Step 1: Check for cashier.py script
if [ ! -f "cashier.py" ]; then
    echo "Error: cashier.py not found in the current directory."
    echo "Please ensure cashier.py is in the same directory as this script."
    exit 1
fi

# Step 2: Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating a new virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment."
        exit 1
    fi
    echo "Virtual environment created successfully."
else
    echo "Virtual environment already exists."
fi

# Step 3: Activate the virtual environment
activate_venv

# Step 4: Upgrade pip and install dependencies
echo "Upgrading pip..."
pip install --upgrade pip

# Step 5: Check and install Tkinter if necessary
check_tkinter

# Step 6: Run cashier.py
echo "Running cashier.py..."
python cashier.py
if [ $? -ne 0 ]; then
    echo "Error: Failed to run cashier.py."
    deactivate_venv
    exit 1
fi

# Step 7: Deactivate virtual environment after closing the GUI
deactivate_venv

echo "Thank you for using the Cashier System!"

