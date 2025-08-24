from datetime import datetime

from src.pipelines import df_cost, df_resume
from src.util import smtp, excel, html

now = datetime.now().strftime('%Y-%m-%d %Hh%M')

def handler(event, context):

    html_content = html.create_tables([
        ('Cost Explorer', df_resume)
    ])
    
    sheetname = f'Cloud Saver {now}.xlsx'
    sheet = excel.create_file(
        [('Cost Explorer', df_cost)]
    )

    smtp.send(
        html_content,
        'Cloud Saver',
        [(sheetname, sheet)]
    )

    return {
        'statusCode': 200,
        'attach': sheetname
    }