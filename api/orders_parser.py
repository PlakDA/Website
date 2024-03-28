from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('status', required=True)
parser.add_argument('menus', required=True)
parser.add_argument('total', required=True, type=float)
parser.add_argument('client_info', required=True)

put_parser = reqparse.RequestParser()
put_parser.add_argument('status')
put_parser.add_argument('menus')
put_parser.add_argument('total', type=float)
put_parser.add_argument('client_info')
