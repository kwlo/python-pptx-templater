import os

from pptx_templater.core import convert


def test_conversion():
    currpwd = os.path.dirname(os.path.abspath(__file__))
    srcpath = f'{currpwd}/fixtures/test_presentation_layout.pptx'
    destpath = f'{currpwd}/test_outputs/updated.pptx'

    j = {
        'slides': [
            {
                'layoutSlideNum': 0,
                'text': {
                    'name': 'Paul'
                }
            },
            {
                'layoutSlideNum': 0,
                'text': {
                    'name': 'Joe'
                }
            },
            {
                'layoutSlideNum': 1,
                'text': {
                    'dog': {
                        'name': 'John Cena'
                    }
                }
            },
        ]
    }

    convert(srcpath, destpath, j)
