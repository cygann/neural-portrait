import csv

links_file = open("image_links.txt","w+")

with open('catalog.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    written_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
        elif (row[7] == 'painting' and row[8] == 'portrait'):
            html_link = row[6]
            unique_index = len('https://www.wga.hu/html/')
            unique_substr = html_link[unique_index : -5]
            image_link = 'https://www.wga.hu/detail/' + unique_substr + '.jpg'
            links_file.write(image_link + '\n')
            written_count += 1

           
        line_count += 1
    print(f'Processed {line_count} lines.')
    print(f'Wrote {written_count} lines.')

links_file.close()
