import re
import shutil

html_footer = '</body>\n</html>'

if __name__ == '__main__':
    with open('./index.html', 'r') as f:
        start_new_file = False
        is_writing = False
        current_write_file = ''
        for line in f.readlines():
            start_new_file = 'name-link' in line
            if start_new_file:
                result = re.search(r'.+href=\"(.+)\">(.+)<.+', line)
                current_write_file = result.group(1)
                with open(current_write_file, 'w+') as person_file:
                    html_head = f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width">\n<title>{result.group(2)}</title>\n<link href="style.css" rel="stylesheet" type="text/css" />\n<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato"/>\n</head>\n<body>\n'
                    person_file.write(html_head)
                    person_file.write(f'<h3>{result.group(2)}</h3>\n')
                    is_writing = True
            if is_writing:
                with open(current_write_file, 'a') as person_file:
                    if not start_new_file:
                        person_file.write(line)
            if '</table>' in line: # stop writing at end of table
                is_writing = False

    shutil.copy('./style.css', './person') # loading css from a lower path is difficult - just duplicate the stylesheet in the persons/ dir