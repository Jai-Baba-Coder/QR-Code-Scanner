
# QR Code Scanner

This project is a simple QR Code Scanner using Python, OpenCV, and pyzbar. The scanner uses a webcam to capture and decode QR codes in real-time.

## Requirements

- Python 3.x
- OpenCV
- pyzbar

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/qr-code-scanner.git
   cd qr-code-scanner
   ```

2. **Install Dependencies**

   Ensure you have `pip` installed and run:

   ```sh
   pip install opencv-python pyzbar
   ```

   If you encounter issues with GUI functions in OpenCV, ensure you have the full version of OpenCV installed:

   ```sh
   pip uninstall opencv-python-headless
   pip install opencv-python
   ```

## Usage

1. **Run the QR Code Scanner**

   ```sh
   python app.py
   ```

2. **Instructions**

   - The script will activate your webcam and start scanning for QR codes.
   - Detected QR codes will be printed in the terminal.
   - To exit the scanner, press the `q` key.

## Troubleshooting

If you encounter the error:

```plaintext
cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:1301: error: (-2:Unspecified error) The function is not implemented.
```

Make sure you have installed the full version of OpenCV:

```sh
pip uninstall opencv-python-headless
pip install opencv-python
```

## License

This project is licensed under the MIT License. See the (LICENSE) file for details.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [pyzbar](https://pypi.org/project/pyzbar/)
