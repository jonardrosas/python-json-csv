from argparse import ArgumentParser
from converter.app import AppConverter
from converter.enums import FormatEnums

source = 'https://api.slingacademy.com/v1/sample-data/products?limit=100'

def main():
    parser = ArgumentParser(prog="Converter", description='Utility use to convert json')
    parser.add_argument('source', type=str, help='Source data to convert')
    parser.add_argument('dest', choices=[choice.value for choice in FormatEnums], help=' data to convert')
    parser.add_argument('-key', '--key', type=str, help='The key in a json file or dict where the list of data is located')
    args = parser.parse_args()
    app = AppConverter(args.source, args.dest, key=args.key)
    app.convert()
    print(args.key)

if __name__ == '__main__':
    main()