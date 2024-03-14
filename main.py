from converter.app import AppConverter

source = 'https://api.slingacademy.com/v1/sample-data/products?limit=10'

if __name__ == '__main__':
    app = AppConverter(source, 'json', 'csv')
    app.convert()