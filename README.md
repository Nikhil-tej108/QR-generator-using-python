# QR Code Generator

This is a simple Python project that generates a QR code for any given data (such as a URL) and saves it as an image file. The project uses the popular [`qrcode`](https://pypi.org/project/qrcode/) library.

## Features

- Generate a QR code for any text or URL
- Customize QR code size, error correction, and colors
- Save the QR code as a PNG image

## Requirements

- Python 3.x
- [`qrcode`](https://pypi.org/project/qrcode/) library
- [`Pillow`](https://pypi.org/project/Pillow/) library (for image processing, usually installed automatically with `qrcode`)

## Installation

Install the required libraries using pip:

```bash
pip install qrcode[pil]
```

## Usage

1. **Clone or download** this repository.
2. Save the code in a file, for example, `code.py`.
3. Edit the `data` variable in the script to encode your own text or URL.
4. Run the script:

   ```bash
   python code.py
   ```

5. The QR code image will be saved as `qr_code.png` in the same directory.

## Example

The following code generates a QR code for the YouTube homepage:

```python
import qrcode

# Data to encode
data = "https://www.youtube.com/"

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print("QR code generated and saved as qr_code.png")
```

## Output

A file named `qr_code.png` will be created in your project directory. You can scan this QR code with any QR code reader.

## License

This project is open source and free to use.

---

Feel free to modify this README for your needs! If you want to add more details or instructions, let me know!
