import os

format = {
    'header': {
        'bg_color': os.getenv('HEADER_BG_COLOR'),
        'font_color': os.getenv('HEADER_FONT_COLOR'),
        'allign': 'center'
    },
    'body': {
        'allign': os.getenv('BODY_ALLIGN'),
        'even': {
            'bg_color': os.getenv('BODY_EVEN_BG_COLOR'),
            'font_color': os.getenv('BODY_EVEN_FONT_COLOR'),
        },
        'odd': {
            'bg_color': os.getenv('BODY_ODD_BG_COLOR'),
            'font_color': os.getenv('BODY_ODD_FONT_COLOR'),
        }
    }
}