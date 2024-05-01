def create_table(data):
    headers = ['Name', 'Ort', 'Land']
    header_row = '|'.join([header.center(10).replace(' ', '_') for header in headers])
    print(header_row)
    
    for record in data:
        formatted_record = '|'.join([str(field).ljust(10) for field in record])
        print(formatted_record)

data = [
    ['Thomas', 'Berlin', 'Germany'],
    ['Britney', 'Sydney', 'Australia']
]

create_table(data)
