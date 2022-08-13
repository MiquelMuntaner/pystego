# PySteganography
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/MiquelMuntaner/pysteganography/blob/main/LICENSE)

A Python program that allows you to save secret messages in images


## Installation

Clone the repository and go into the folder

```bash
  git clone https://github.com/MiquelMuntaner/pysteganography
  cd pysteganography
```
Download all dependencies from the requirements.txt file
```bash
  pip3 install -r requirements.txt 
```
## Usage/Examples

To use a simple interface in terminal use the following command
```bash
  python3 src/pysteganography.py interface
```

Other commands:
```bash
  python3 src/pysteganography.py encode "My secret message" your_image.png
  python3 src/pysteganography.py decode your_image.png
```
You can use -e in both commands if you want to use AES-256 bit encryption.


## Screenshots

![App Screenshot](https://images2.imgbox.com/b2/20/uF88hANk_o.png)


## Authors

- [@MiquelMuntaner](https://github.com/MiquelMuntaner)
