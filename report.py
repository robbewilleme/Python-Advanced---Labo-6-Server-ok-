import jinja2
from jsonhandler import read_json

def generate_html_report(template_file):
    results = read_results()
    template_loader = jinja2.FileSystemLoader(searchpath=".")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template_file)
    report =  template.render(results=results)
    write_html(report)

def read_results():
    results = read_json("results.json")
    return results

def write_html(report):
    with open("report.html", "w") as report_file:
        report_file.write(report)

