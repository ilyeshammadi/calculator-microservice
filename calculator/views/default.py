from pyramid.view import view_config
from pyramid.response import Response

from .. import schemas
from ..core.calculator import Calculator


@view_config(route_name='add', request_method='POST', renderer='json')
def add(request):
    data = request.json_body

    # Validate the data
    is_schema_valid = schemas.add.is_valid(data)
    if not is_schema_valid:
        return Response(json_body={"message": "Invalid arguments"}, status=400)
    validated_data = schemas.add.validate(data)

    result = Calculator.add(validated_data.get('a'), validated_data.get('b'))
    return Response(json_body={"result": result}, status=200)
