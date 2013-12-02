SECTIONS = ["inputs", "inspectors", "transformers", "outputs", "pipes"]

# components

INPUTS = {'dummy source': {'description': 'a dummy source', 'use': 'tests.components.Input'}}

INSPECTORS = {'dummy validator': {'description': 'a dummy validator', 'use': 'tests.components.Validator'}}

TRANSFORMERS = {
   'dummy mapper': {'description': 'a basic dummy mapper', 'use': 'tests.components.FieldMapper',
                     'map': [{'number': 'Numero'}, {'description': 'Selite'}, {'amount': 'Summa'}]
                   },
   'dummy constructor': {'description': 'a simple object constructor', 'use': 'tests.components.KlassConstructor'}
}

SUBSCRIBERS = {'dummy subscriber': {'description': 'a dummy subscriber', 'use': 'tests.components.Subscriber'}}

PIPES = {'dummy pipe': [{'description': 'a dummy source',
                  'use': 'tests.components.Input'},
                 {'description': 'a basic dummy mapper',
                  'map': [{'number': 'Numero'},
                          {'description': 'Selite'},
                          {'amount': 'Summa'}],
                  'use': 'tests.components.FieldMapper'},
                 {'description': 'a dummy validator',
                  'use': 'tests.components.Validator'}]}
