from src.util.format import format
from pandas import DataFrame

format_header = format['header']
format_odd = format['body']['odd']
format_even = format['body']['even']

def create_tables(dfs: list[tuple[str, DataFrame]]) -> str:
    html_content = ''
    for title, df in dfs:
        html_content += f'<h2>{title}</h2>'
        html_content += create_table(df) if not df.empty else '<p><i>Sem Ocorrência</i></p>'
    
    return html_content

def create_table(df: DataFrame):
    df.reset_index(drop=True, inplace=True)

    styled = df.style \
        .apply(style_rows, axis=1) \
        .set_table_styles([{
            'selector': 'thead th',
            'props': get_css_string(format_header)
        }]) \
        .format(get_number_format(df)) \
        .hide(names=False)

    table = styled.to_html(index=False)
    return table

def get_number_format(df: DataFrame):
    number_format = {}
    for col, dtype in df.dtypes.items():
        if "int" in str(dtype):
            number_format[col] = "{:d}"
        elif "float" in str(dtype):
            number_format[col] = "{:,.2f}"
    
    return number_format

def style_rows(row):
    f = format_even if row.name % 2 == 0 else format_odd
    return [get_css_string(f)]*len(row)

def get_css_string(format):
    return f"""
        background-color: #{format['bg_color']};
        color: #{format['font_color']};
        border: 1px solid black;
        text-align: center
    """