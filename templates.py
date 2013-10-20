'''templates.py

CS 257 Python Web App, Fall 2013, Jeff Ondich
Jiatao Cheng, Erin Wilson, and Adam Canady

This file defines the HTML used in this project.
'''

class Templates():

    def __init__(self):
        self.start_page = open('templates/front_page.html')
        self.results_template = open('templates/results.html')
        self.error_page = open('templates/error.html')

    def make_results_page(self, title, content):
        results_template = self.results_template.read()

        return results_template % (title, content)

    def get_start_page(self):
        return self.start_page.read()

    def get_error_page(self):
        return self.error_page.read()

    def make_table(self, list_of_tuples, headers = []):
        generated_table = '<table class="results_table">\n'

        if headers:
            generated_table += '  <tr class="headers">\n'
            for header in headers:
                generated_table += '    <td class="header">'+str(header)+"</td>\n"
            generated_table += "  </tr>\n"

        for tuple in list_of_tuples:
            generated_table += '  <tr class="row">\n'
            for item in tuple:
                generated_table += '    <td class="cell">'+str(item)+"</td>\n"
            generated_table += "  </tr>\n"

        generated_table += "</table>\n"

        return generated_table

''' Tests '''
if __name__ == "__main__":
    templates = Templates()
    print templates.get_start_page()
    print templates.get_results_page(1)