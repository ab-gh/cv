import json
from jinja2 import Template

def main():
    with open("resume.json", 'r') as resume:
        data = json.load(resume)
    basics_raw = data["basics"]
    work_raw = data["work"]
    volunteer_raw = data["volunteer"]
    education_raw = data["education"]
    awards_raw = data["awards"]
    skills_raw = data["skills"]

    basics_arr = basics_raw
    work_arr = generate_items(work_raw)
    volunteer_arr = generate_items(volunteer_raw)
    education_arr = education_raw
    awards_arr = awards_raw
    skills_arr = skills_raw

    github = next(item["username"] for item in basics_arr["profiles"] if item["network"].lower() == "github")

    template_string = open("src/template.html", 'r').read()
    template = Template(template_string)

    render = template.render(basics_arr=basics_arr,
                             work_arr=work_arr, 
                             volun_arr=volunteer_arr,
                             edu_arr=education_arr,
                             award_arr=awards_arr,
                             skill_arr=skills_arr,
                             github=github)

    with open("index.html", 'w') as out:
        out.write(render)

def generate_items(raw):
    """
    generates a dict of items to give the template from a raw JSON Resume work/volunteer item
    """
    section_list = list()
    for raw_item in raw:
        tmp_list_item = dict()
        try:
            tmp_list_item["company"] = raw_item["company"]
        except KeyError:
            tmp_list_item["company"] = raw_item["organization"]
        tmp_list_item["startDate"] = raw_item["startDate"]
        try:
            tmp_list_item["endDate"] = raw_item["endDate"]
        except KeyError:
            tmp_list_item["endDate"] = "present"
        tmp_list_item["position"] = raw_item["position"]
        tmp_list_item["website"] = raw_item["website"]
        tmp_list_item["details"] = list()
        tmp_list_item["details"].append(raw_item["summary"])
        for highlight in raw_item["highlights"]:
            tmp_list_item["details"].append(highlight)        
        section_list.append(tmp_list_item)
    return section_list


if __name__ == "__main__":
    main()

