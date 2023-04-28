import os

import torch


if __name__ == '__main__':
    # Test the version
    print(f'- PyTorch version: {torch.__version__}')

    # Test the device
    device = torch.device('cpu') \
        if torch.cuda.is_available() \
        else torch.device('cpu')
    print(f'- Detected device: {device}')

    # Test tensor operations
    my_tensor = torch.rand(3, 4, device=device)
    print(
        f'- Test tensor matmul: {(my_tensor @ my_tensor.t()).shape == (3, 3)}',
    )

    # Test loading environment variables
    data_home = os.environ.get('DATA_HOME', None)
    print(
        f'- environment variable "DATA_HOME": {data_home if data_home else "Not Found"}')

    # Test data loading
    if data_home:
        if os.path.exists(data_home):
            print(f'- volume "DATA_HOME": Exists ({os.stat(data_home)})')
        else:
            print('- volume "DATA_HOME": Not Found')
