HERRAMIENTA_NOTA = {
    'name': 'calcular_nota',
    'description': (
        'Convierte un puntaje numérico entre 0.0 y 1.0 en una calificación '
        'en letra (A, B, C, D o F), o indica Bad score si está fuera de rango.'
    ),
    'input_schema': {
        'type': 'object',
        'properties': {
            'puntaje': {
                'type': 'number',
                'description': 'Puntaje decimal entre 0.0 y 1.0 inclusive',
                'minimum': 0,
                'maximum': 1,
            },
        },
        'required': ['puntaje'],
    },
}

if __name__ == '__main__':
    assert HERRAMIENTA_NOTA['name'] == 'calcular_nota'
    assert HERRAMIENTA_NOTA['input_schema']['required'] == ['puntaje']
    tipo = HERRAMIENTA_NOTA['input_schema']['properties']['puntaje']['type']
    assert tipo == 'number'
    assert len(HERRAMIENTA_NOTA['description']) > 20
    print('Todas las pruebas pasan')
