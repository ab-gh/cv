import json
from jinja2 import Template

def main():
    with open("resume.json", 'r') as resume:
        data = json.load(resume)
        print(data["basics"])
    template_string = open("src/template.html", 'r').read()
    template = Template(template_string)
    render = template.render(work_str="FOOBAR")
    print(render)

if __name__ == "__main__":
    main()