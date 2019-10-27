from pptx_templater.text_parser import render


def test_render():
    assert render('Hello {{ name }}!', name='John Connor') == 'Hello John Connor!'
    assert render('Hello Arnold!', name='Connor') == 'Hello Arnold!'
    assert render(
        'Hello {{ nested.name }}!',
        nested={'name': 'Sarah Connor'}
    ) == 'Hello Sarah Connor!'
    assert render(
        'Hello {{ nested.name }}!',
        **{
            'nested': {
                'name': 'T101'
            }
        }) == 'Hello T101!'
