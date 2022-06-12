def classmatesData():
    return [
      [
        {
          'component': 'LineCard',
          'title': 'График',
          'item': {
            'series': [{ 'data': [{ 'x': 100, 'y': 0}, { 'x': 50, 'y': 50 }, { 'x': 0, 'y': 100 }], 'yName': 'Hello' }],
            'xKey': 'x',
            'yKey': 'y',
          }
        },
      ]
    ]


def telegrammData():
  return [
    [
      {
        'component': 'LineCard',
        'title': 'График',
        'item': {
          'series': [{'data': [{'x': 100, 'y': 0}, {'x': 50, 'y': 50}, {'x': 0, 'y': 100}], 'yName': 'Hello'}],
          'xKey': 'x',
          'yKey': 'y',
        }
      },
    ]
  ]

def vkData():
  return [
      [
        {
          'component': 'LineCard',
          'title': 'График',
          'item': {
            'series': [{ 'data': [{ 'x': 100, 'y': 0}, { 'x': 50, 'y': 50 }, { 'x': 0, 'y': 100 }], 'yName': 'Hello' }],
            'xKey': 'x',
            'yKey': 'y',
          }
        },
        {
          'component': 'ScatterCard',
          'title': 'Точечный График',
          'item': {
            'series': [{ 'data': [{ 'x': 100, 'y': 0}, { 'x': 50, 'y': 50 }, { 'x': 0, 'y': 100 }], 'yName': 'Hello' }],
            'xKey': 'x',
            'yKey': 'y',
          }
        },
      ],
        [
          {
            'component': 'PieCard',
            'title': 'Пирожок',
            'item': {
              'data': [{ 'angle': 100, 'label': 'fgeafg'}, { 'angle': 50, 'label': 'label21' }, { 'angle': 100, 'label': 'eg3' }, { 'angle': 100, 'label': '123' }, { 'angle': 100, 'label': 'eg3' }, { 'angle': 100, 'label': 'eg3' }, { 'angle': 100, 'label': 'eg3' }, { 'angle': 100, 'label': 'eg3' }],
              'angleKey': 'angle',
              'labelKey': 'label',
            }
          },
          {
            'component': 'HistogramCard',
            'title': 'Гистограмма',
            'item': {
              'series': [{ 'data': [{ 'x': 100, 'y': 10}], 'yName': 'Hello' }, { 'data': [{ 'x': 0, 'y': 100 }], 'yName': 'Hello2' }],
              'angleKey': 'angle',
              'labelKey': 'label',
            }
          },
          {
            'component': 'HistogramCard',
            'title': 'Гистограмма 2',
            'item': {
              'series': [{ 'data': [{ 'x': 100, 'y': 10}], 'yName': 'Hello' }, { 'data': [{ 'x': 0, 'y': 100 }], 'yName': 'Hello3' }],
              'angleKey': 'angle',
              'labelKey': 'label',
            }
          },
        ]
    ]

def userData():
  return [
    [
      {
        'component': 'LineCard',
        'title': 'График',
        'item': {
          'series': [{'data': [{'x': 100, 'y': 0}, {'x': 50, 'y': 50}, {'x': 0, 'y': 100}], 'yName': 'Hello'}],
          'xKey': 'x',
          'yKey': 'y',
        }
      },
    ]
  ]