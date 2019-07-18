import xlsxwriter

workbook = xlsxwriter.Workbook('new_excel.xlsx') 

worksheet = workbook.add_worksheet('sheet1')

headings = ['Number','testA','testB']         

data = [
    ['2017-9-1','2017-9-2','2017-9-3','2017-9-4','2017-9-5','2017-9-6'],
    [10,40,50,20,10,50],
    [30,60,70,50,40,30],
]                                                       

worksheet.write_row('A1',headings)

worksheet.write_column('A2',data[0])
worksheet.write_column('B2',data[1])
worksheet.write_column('C2',data[2])                  

chart_col = workbook.add_chart({'type':'line'})      
chart_col.add_series(                                  
    {
        'name':'=sheet1!$B$1',
        'categories':'=sheet1!$A$2:$A$7',
        'values':   '=sheet1!$B$2:$B$7',
        'line': {'color': 'red'},
    }
)

chart_col.set_title({'name':'Beautiful Chart'})
chart_col.set_x_axis({'name':"X"})
chart_col.set_y_axis({'name':'Y'})        

chart_col.set_style(1)

worksheet.insert_chart('A10',chart_col,{'x_offset':25,'y_offset':10}) 

workbook.close()
