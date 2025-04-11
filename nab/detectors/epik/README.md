# nP-CLAD Detector (tested for Python 3.13.3 on a Windows 10 machine, shame on me)

# Clone the repository
```bash
git clone git@github.com:stivenschwanz/NAB4nP-CLAD.git
cd NAB4nP-CLAD
```

# Create the virtual environment
```bash
pip install virtualenv
python -m venv .venv
```

# Activate the virtual environment
```bash
source .venv/Scripts/activate
```

# Update pip and install all dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

# Add wnnlib (https://github.com/stivenschwanz/wnnlib) to the path
```bash
export PYTHONPATH=/c/.../wnnlib
```

# Run the Epik detector on all files
```bash
python run.py -d epik --detect --optimize --score --normalize --numCPUs 1 --skipConfirmation
```

# Run the Epik detector on twitter files
```bash
python run.py -d epik --detect --optimize --score --normalize --numCPUs 1 --skipConfirmation --windowsFile labels/combined_windows_twitter.json
```

# Compute the final scores
```bash
python run.py -d epik --optimize --score --normalize --numCPUs 1 --skipConfirmation --windowsFile labels/combined_windows.json
```