# QR Code Generator

A customizable QR Code Generator written in Python.

## Features

- Generate QR codes from text or URLs
- Custom output filename
- PNG output
- Custom QR size
- Custom border size
- Custom foreground/background colors
- Error-correction selection
- Input validation
- Works on Windows, Linux, macOS, and Termux

## Structure

```text
qr-code-generator/
├── qr_generator.py
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.9+
- qrcode
- Pillow

## Installation

```bash
git clone https://github.com/HackerG3121/qr-code-generator.git
cd qr-code-generator
python -m pip install -r requirements.txt
```

## Run

```bash
python qr_generator.py
```

### Termux

```bash
pkg update
pkg install python
pip install -r requirements.txt
python qr_generator.py
```

## Example

```text
========================================
          QR CODE GENERATOR
========================================

Enter text/URL: https://github.com/

Output filename (default: QR-Code.png): github

QR size [default: 10]: 10
Border [default: 4]: 4

Foreground color [default: black]: black
Background color [default: white]: white

Error correction:
L = 7%
M = 15%
Q = 25%
H = 30%

Choose [default: M]: M

QR Code saved successfully!
File: github.png
```

## Error Correction

| Level | Recovery |
| ----- | -------: |
| L     |      ~7% |
| M     |     ~15% |
| Q     |     ~25% |
| H     |     ~30% |

## Security Note

The program generates QR images locally and does not upload entered data to a server.

Do not put passwords, private keys, API secrets, or other sensitive information into QR codes unless you understand the risks.

## License

MIT License.
