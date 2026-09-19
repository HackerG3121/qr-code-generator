import qrcode
from pathlib import Path

BANNER = """
========================================
          QR CODE GENERATOR
========================================
"""


def get_int(prompt, default, minimum=1):
    value = input(f"{prompt} [default: {default}]: ").strip()

    if not value:
        return default

    try:
        number = int(value)
        if number < minimum:
            print(f"Value must be at least {minimum}. Using {default}.")
            return default
        return number
    except ValueError:
        print(f"Invalid number. Using {default}.")
        return default


def get_filename():
    filename = input(
        "Output filename (default: QR-Code.png): "
    ).strip()

    if not filename:
        filename = "QR-Code.png"

    if not filename.lower().endswith(".png"):
        filename += ".png"

    return filename


def choose_error_correction():
    print("""
Error correction:
L = 7%
M = 15%
Q = 25%
H = 30%
""")

    choice = input("Choose [default: M]: ").strip().upper() or "M"

    levels = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }

    if choice not in levels:
        print("Invalid choice. Using M.")
        choice = "M"

    return levels[choice]


def main():
    print(BANNER)

    data = input("Enter text/URL: ").strip()

    if not data:
        print("Error: Text or URL cannot be empty.")
        return

    filename = get_filename()
    box_size = get_int("QR size", 10, 1)
    border = get_int("Border", 4, 0)

    fill_color = input(
        "Foreground color [default: black]: "
    ).strip() or "black"

    back_color = input(
        "Background color [default: white]: "
    ).strip() or "white"

    error_correction = choose_error_correction()

    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color=fill_color,
        back_color=back_color,
    )

    output_path = Path(filename)
    image.save(output_path)

    print("\nQR Code saved successfully!")
    print(f"File: {output_path.resolve()}")


if __name__ == "__main__":
    main()
