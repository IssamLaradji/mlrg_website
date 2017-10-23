
import os
import pandas as pd
import numpy as np
import os.path
import time

import datetime
import pandas as pd



# def get_email_template(name, day, topic):
#     fname = "backup/email_template"
#     file_content = open(fname).read() % (name, topic, topic, name, day)
#     f = open("backup/email", 'w')

#     f.write(file_content)
#     f.flush()
#     f.close()

#     return file_content


def create_HTMLTable(name):
    # CREATE HTML TABLE FOR ONE SCHEDULE
    table = np.array(pd.read_csv(str(name) + ".csv",sep=';'))
    term_year = int(name.split("_")[1])

    next_flag = False
    current_set = False
    apply_strike = False
    html_file = ""
    html_file += '<table style="width:100%;border: 2px solid #bbb; text-align:left;">\n'

    for i, row in enumerate(table):


        # if main header
        if i == 0:
            html_file += "<tr>\n"
            html_file += '<td style="text-align:left;background: #36546F;font-size:17px;color:#FDF5E6;" colspan="3">\n'
            html_file += row[0]

            html_file += '<span style="float:right;padding-right:15px">'

            html_file += str(row[-1])
            html_file +=  '</span>'
            html_file += "</td>\n"
            html_file += "</tr>\n"
            continue

        if i ==1:
            html_file += "<tr>\n"
        if i > 1:
            # get date

            date = time.strptime(row[0], "%b %d")

            current = datetime.datetime.now()
            current_year, current_month, current_day = current.year, current.month, current.day
            if ((current_year > term_year) or
               (current_month == date.tm_mon and current_day > date.tm_mday) or
               (current_month > date.tm_mon)):
                html_file += '<tr style="background-color:#E6E9EC">\n'
                apply_strike = True
            else:
                next_flag = True
                html_file += "<tr>\n"

        day = row[0]
        presenter = row[1]
        topic = row[2]
        


        for j, element in enumerate(row):
            # sub header
            if i == 1:
                html_file += '<td style="text-align:left;background: #36546F;font-size:17px;color:#FDF5E6;">'
                html_file += str(element)
                html_file += "</td>\n"
            else:
                if next_flag and not current_set:
                    current_set = True
                    html_file += '<td   style="border-width: thick;      border-color: #36546F;">'
                    #get_email_template(presenter, day, topic)
                elif apply_strike:
                    apply_strike=False
                    html_file += '<td style="text-decoration: line-through;">'
                else:
                    html_file += "<td>"

                if "- " in str(element) and "http" in str(element):
                    start_index = str(element).index("- ") + 2
                    html_file += str(element)[:start_index]
                    html_file += '<a href=' + str(element)[start_index:] +'> [website link] </a>'


                if "- " in str(element) and ".pdf" in str(element):
                    start_index = str(element).index("- ") + 2
                    html_file += str(element)[:start_index]
                    html_file += '<a href=' + slides_folder + str(element)[start_index:] +'> [pdf slides] </a>'



                elif "http" in str(element):
                    print
                elif str(element) == "nan":
                    html_file += ""
                else:
                    html_file += str(element)
                html_file += "</td>\n"
        html_file += "</tr>\n"

    html_file += "</table>"

    return html_file

def group_HTMLTables(table_list):
    # CREATE HTML FOR ALL THE TABLES AS ONE STRING
    HTMLTables = "\n<br>\n"

    for table in table_list:
        HTMLTables += table 
        HTMLTables += "\n<br>\n<br>\n"
    
    return HTMLTables    

def create_index_file(filename, mlrg_topic, HTMLTables):
    # USE template.html TO CREATE index.html 
    template = open(filename).read()
    assert "mlrg_tables" in template

    template = template.replace("mlrg_topic", mlrg_topic)
    template = template.replace("mlrg_tables", HTMLTables)
    f = open("index.html", 'w')

    f.write(template)
    f.flush()
    f.close()

    print "done! saved in index.html"


if __name__ == "__main__":
    table_names = ["winter_2017_term_1",
               "summer_2017",
               "winter_2017_term_2",
               "winter_2016_term_1",
               "summer_2016",
               "winter_2015_term_2",
               "winter_2015_term_1",
               "summer_2015_term_2"]

    schedules_folder = "schedules/"
    slides_folder = "slides/"

    table_list = []

    for tname in table_names:
       table_list +=  [create_HTMLTable(name=schedules_folder+
                                              tname)]

    mlrg_topic = "Winter term 1 2017 - Deep Learning Meets Graphical Models"
    HTMLTables = group_HTMLTables(table_list)
    create_index_file("template.html", mlrg_topic, HTMLTables)
