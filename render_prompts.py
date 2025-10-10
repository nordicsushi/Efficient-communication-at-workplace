#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random
import re
from pathlib import Path

from pydantic import BaseModel, field_validator

COORDINATOR_TEMPLATE = "coordinator-template.md"
COORDINATOR_OUTPUT = "coordinator.md"
PLACEHOLDER_RE = re.compile(r"{{\s*([A-Za-z_][A-Za-z0-9_]*)\s*}}")


def render_template(template_text: str, ctx: dict[str, str | float]) -> str:
    def repl(match: re.Match) -> str:
        key = match.group(1)
        if key in ctx:
            return str(ctx[key])
        return match.group(0)

    return PLACEHOLDER_RE.sub(repl, template_text)


def validate_input(ctx: dict[str, str | float]) -> None:
    class ContextModel(BaseModel):
        job: str
        yoe: float
        company: str
        jr: str

        @field_validator("yoe", mode="after")
        @classmethod
        def validate(cls, v) -> None:
            if v < 0:
                raise ValueError("Years of experience must be a positive number.")
            return v

    return ContextModel(**ctx)


def main():
    parser = argparse.ArgumentParser(
        description="Render command-line/JSON provided values into {{PLACEHOLDER}} placeholders in Markdown templates."
    )

    parser.add_argument(
        "--job",
        default="Machine Learning Engineer",
        help="Example field: Machine Learning Engineer",
    )
    parser.add_argument("--jr", default="", help="Example field: job responsibilities")
    ## meeting_ids
    parser.add_argument(
        "--meeting_ids",
        help="Example field: meeting ids the user will attend",
    )

    args = parser.parse_args()

    # Collect context
    ctx: dict[str, str | float] = {}

    if args.jr == "":
        with open("job_responsibilities.txt") as f:
            ctx["jr"] = f.read()

    # Then override with example fields
    if args.job is not None:
        ctx["job"] = args.job
    if args.jr is not None:
        ctx["jr"] = args.jr
    if args.meeting_ids is not None:
        ctx["meeting_ids"] = args.meeting_ids

    if "senior" in args.job.lower():
        ctx["yoe"] = random.uniform(4, 8)
    elif "lead" in args.job.lower() or "principal" in args.job.lower():
        ctx["yoe"] = random.uniform(8, 15)
    else:
        ctx["yoe"] = random.uniform(1, 4)

    ctx["company"] = "A tech company based in Silicon Valley"

    ctx_validated = validate_input(ctx)
    # Read template
    template_text = Path(COORDINATOR_TEMPLATE).read_text(encoding="utf-8")

    # Render
    rendered = render_template(template_text, ctx_validated.model_dump())

    # Write output
    Path(COORDINATOR_OUTPUT).write_text(rendered, encoding="utf-8")
    print(f"✅ Generated: {COORDINATOR_OUTPUT}")


if __name__ == "__main__":
    main()
