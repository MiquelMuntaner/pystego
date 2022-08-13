# PySteganography
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/MiquelMuntaner/pysteganography/blob/main/LICENSE)

A Python program that allows you to save secret messages in images
## Installation
```python
  pip install pystego
```
## Usage/Examples

To use a simple interface in terminal use the following command
```bash
  pystego interface
```

Other CLI commands:
```bash
  pystego encode "My secret message" your_image.png
  pystego decode your_image.png
```
You can use -e in both commands if you want to use AES-256 bit encryption.
## Documentation

To encode a message in an image use the encode_img function as in the example:
```python
    from pysteganography import encode_img
    
    img_path = 'test_image.png'
    secret_message = 'Example secret message'
    encode_img(img_path, secret_message)
```

To extract a message from an image use the decode_img function as in this example:
```python
    from pysteganography import decode_img

    img_path = 'test_image.png'
    secret_message = decode_img(img_path, secret_message)
    print(secret_message)
```
## Screenshots

![App Screenshot](https://images2.imgbox.com/b2/20/uF88hANk_o.png)


## Authors

- [@MiquelMuntaner](https://github.com/MiquelMuntaner)

