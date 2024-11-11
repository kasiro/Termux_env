import dload
from sys import argv

if len(argv) >= 3:
    method_name = argv[1]
    url = argv[2]

    methods_ = [
        'down_speed',
        'save',
    ]

    if method_name in methods_:
        match method_name:
            case 'save':
                dload.save(url)

            case 'down_speed':
                dload.down_speed()

