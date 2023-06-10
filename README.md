# V4 List Creation Module

This project provides a module for creating a list using the V4 algorithm.

## Installation

To use this module, make sure you have Python 3.x installed. You will also need the `hashlib` and `tqdm` libraries. You can install them using pip:

```shell
pip install hashlib tqdm
```

## Usage

```python
from list_generate import v5

# Instantiate the v5 class
v4 = v5()

# Generate a list using the V4 algorithm
seed = 1234
Fin = 10
MIN = 1
MAX = 100
result = v4.generate(seed, Fin, MIN, MAX, show=True)
print(result)
```

## Documentation

### `sha256_decimal(text)`

This method calculates the SHA-256 hash of the input text and converts it to a decimal value.

- `text` (str): The input text to calculate the hash from.

Returns:
- `decimal_value` (int): The decimal representation of the SHA-256 hash.

### `calculate_large_number(seed)`

This method calculates a large number using the V4 algorithm.

- `seed` (int): The seed value to start the calculation.

Returns:
- `text` (int): The calculated large number.

### `generate(seed, Fin, MIN, MAX, show=False)`

This method generates a list of numbers using the V5 algorithm.

- `seed` (int): The seed value to start the generation.
- `Fin` (int): The number of iterations to perform.
- `MIN` (int): The minimum value for the generated numbers.
- `MAX` (int): The maximum value for the generated numbers.
- `show` (bool): Optional. If `True`, progress will be displayed using the tqdm library.

Returns:
- `liste` (list): The generated list of numbers.

## Contributing

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.