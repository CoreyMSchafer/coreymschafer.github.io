import json
from datetime import datetime

from jinja2 import Environment, FileSystemLoader

# Load JSON data
with open("resume-corey.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data["base_url"] = "127.0.0.1:5500"

# Add any extra context if needed
data["current_year"] = datetime.now().year

if "social_links" in data:
    for link in data["social_links"]:
        if "svg_path" in link and link["svg_path"]:
            with open(link["svg_path"], "r", encoding="utf-8") as svg_file:
                link["svg_data"] = svg_file.read()

# Set up Jinja environment
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("index_template.html")


# Render the template with the data
html_output = template.render(**data)

# Write the output to an HTML file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("HTML file generated successfully!")
