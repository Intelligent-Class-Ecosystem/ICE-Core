import os
import json

from app import create_app
from app.models import *

app = create_app()

if __name__ == '__main__':
    """
    if os.path.exists("data/organization.json"):
        org = import_data_from_file("data/organization.json")
    else:
        name = ""
        while name == "": name = str(input("请输入新组织的名字 >> ")) 
        description = str(input("请输入新组织的描述 (可留空) >> "))
        org = organization(name, description)
        with open("data/organization.json", "w", encoding = "UTF-8") as f:
            json.dump(org.export_data(), f, ensure_ascii = False)
    """
    app.run(host = "0.0.0.0", port = 28582)
