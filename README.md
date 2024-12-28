# AutoBabft


## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Packaging

To package the project as a standalone executable, use PyInstaller with the following command:

```
pyinstaller --onefile --windowed autobabft.py
```

Ensure that `pyinstaller` is available in your `PATH`. If you cannot add `pyinstaller` to your `PATH`, you can use this alternative command:

```
python -m PyInstaller --onefile --windowed autobabft.py
```

