import qrcode

# Data to encode
data = "https://www.youtube.com/" # Example URL of a YouTube channel

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code (1 is smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,  # size of each box in the QR code
    border=4,  # thickness of the border (minimum is 4)
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qr_code.png")

print("QR code generated and saved as qr_code.png")
