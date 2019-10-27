python-pptx-templater
=====================

python-pptx-templater is a tool to create highly customizable PowerPoint presentation using the jinja template languages.
User specifies the layouts and placeholders and the template will render the presentation.

Example
-------

Input

.. image:: https://raw.githubusercontent.com/kwlo/python-pptx-templater/master/docs/static/images/sample_input.png

Using Template JSON:

.. code-block:: text

    {
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

Output

.. image:: https://raw.githubusercontent.com/kwlo/python-pptx-templater/master/docs/static/images/sample_output.png

Install
-------

.. code-block:: text

    pip install python-pptx-templater


Usage
-----

.. code-block:: text

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
