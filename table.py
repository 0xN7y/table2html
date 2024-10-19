import pandas as pd


def excel_to_html(excel_file):
    df = pd.read_excel(excel_file)


    html_table = df.to_html(index=False, classes='fancy-table', border=0)


    html_content = f'''
    <html>
    <head>
        <style>
            .fancy-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 18px;
                text-align: left;
                border: 1px solid #ddd;
            }}
            .fancy-table th, .fancy-table td {{
                padding: 12px 15px;
                border: 1px solid #ddd;
            }}
            .fancy-table th {{
                background-color: #f4b084;
                color: white;
            }}
            .fancy-table tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            section {{
                padding: 20px;
                border: 2px solid #4CAF50;
                background-color: #f9f9f9;
            }}
        </style>
    </head>
    <body>
        <section>
            {html_table}
        </section>
    </body>
    </html>
    '''
    return html_content



html_output = excel_to_html('./Desktop/BOQ.xls')


with open('Done.html', 'w') as file:
    file.write(html_output)

print(f"HTML table has been generated and saved as 'Done.html'.")
