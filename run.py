import json
import os
from pathlib import Path

from render_prompts import COORDINATOR_OUTPUT, COORDINATOR_TEMPLATE, render_template

template_text = Path(COORDINATOR_TEMPLATE).read_text(encoding="utf-8")
MODEL = "claude-sonnet-4.5"

with open("data/role_meeting_type.json") as f:
    role_meeting_type = json.load(f)

for role in role_meeting_type:
    role_details = {
        "job": role["role"],
        "yoe": 3.5,
        "company": "A tech company based in Silicon Valley",
        "meeting_ids": role["meeting_ids"],
        "jr": role["job responsibility"],
    }

    rendered = render_template(template_text, role_details)
    Path(COORDINATOR_OUTPUT).write_text(rendered, encoding="utf-8")
    print(f"✅ Generated: {COORDINATOR_OUTPUT}")

    os.system(
        f'copilot --model {MODEL} --allow-all-tools -p "Complete the task in the coordinator.md."'
    )
