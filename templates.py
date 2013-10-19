'''templates.py

CS 257 Python Web App, Fall 2013, Jeff Ondich
Jiatao Cheng, Erin Wilson, and Adam Canady

This file defines the HTML used in this project.
'''

class Templates():

    def __init__(self):
        self.start_page = open('templates/front_page.html')
        self.results_template = open('templates/results.html')

    def get_results_page(self, title, content):
        results_template = self.results_template.read()

        return results_template % (title, content)

    def get_start_page(self):
        return self.start_page.read()

    def make_table(list_of_tuples, headers = []):
        print '<table class=".table">\n'

        if headers:
            print '  <tr class=".headers">\n'
            for header in headers:
                print '    <td class=".header">'+header+"</td>\n"
            print "  </tr>"

        for tuple in list_of_tuples:
            print '  <tr class=".row">\n'
            for item in tuple:
                print '    <td class=".cell">'+item+"</td>\n"
            print "  </tr>"

        print "</table>"

''' Tests '''
if __name__ == "__main__":
    templates = Templates()
    print templates.get_start_page()
    print templates.get_results_page(1)