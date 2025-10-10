## Task
Here are the requirements for completing this task: 
- Your goal is to create one Mermaid diagram demonstrating the speaking flow for each type of meeting that I can apply.  
- Important: in the Mermaid diagram, always use blue nodes to represent action steps where the speaker needs to communicate, and also use `<div align="center"></div>` to center the diagrams.
- You don't need to specify the exact words I should say, but rather provide a workflow format that I can use every time I speak, which also clearly conveys what I need to express to others.  
- You should create the mind flow based on the meeting type and the speaker's role (presenter, attendee, facilitator, one-on-one, etc.) 
- The mind flow you create should be as natural as how a person who is excellent at communication and speaking would handle it. 
- The context is a tech company, so adapt the workflow to this scenario.

## Input
You will see the role information in the coordinator.md file, formatted as follows:
  - My job: [job name]
  - Year of experience: X years
  - Company I work at: [Company name]
  - Job responsibilities: [a list of job responsibilities]
  - Meeting to attends: [meeting_ids]

Below, you will see a json block where the meeting id(case), type_of_meeting, speaker role, scenario, and tasks to be completed are given below. 
You need to generate a mind flow diagram using Mermaid for each case ONLY OF the `case` is included in the "Meeting to attends" of a given role.

```json
[
  {
    "case": 1,
    "type_of_meeting": "Daily Stand-up meeting",
    "speaker_role": "Attendee",
    "scenario": "The speaker needs to join this meeting every morning to catch up with the team.",
    "tasks": [
      "Share current progress with the rest of the team",
      "Listen to other teammates and follow up with them if necessary",
      "Talk about future work",
      "Share blockers if needed"
    ]
  },
  {
    "case": 2,
    "type_of_meeting": "Weekly Stand-up meeting",
    "speaker_role": "Attendee",
    "scenario": "The speaker needs to join this meeting every week to catch up with the team.",
    "tasks": [
      "Share highlights and lowlights of the week",
      "Summarize completed work and planned items for next week",
      "Coordinate cross-team dependencies",
      "Raise risks or blockers that need broader attention"
    ]
  },
  {
    "case": 3,
    "type_of_meeting": "Knowledge sharing meeting",
    "speaker_role": "Facilitator",
    "scenario": "A knowledge sharing meeting is held every week where a presenter comes to share a topic with the rest of the team. The speaker needs to chair the meeting.",
    "tasks": [
      "Greet the audience and outline the agenda and timing",
      "Provide opening remarks to set context and expectations",
      "Introduce the presenter and the topic to be presented",
      "Manage Q&A and timekeeping",
      "Close the meeting with key takeaways and links to resources"
    ]
  },
  {
    "case": 4,
    "type_of_meeting": "Technical meeting / Code review",
    "speaker_role": "Communicator/Presenter",
    "scenario": "The speaker needs to follow up with their colleagues to discuss a technical issue they found.",
    "tasks": [
      "Introduce the context, scope, and goals of the review",
      "Present the solution, design choices, and trade-offs",
      "Walk through the code diffs and tests",
      "Ask for feedback and clarify suggestions",
      "Agree on changes, owners, and deadlines",
      "Plan the next steps and merge/release criteria"
    ]
  },
  {
    "case": 5,
    "type_of_meeting": "Sprint Planning",
    "speaker_role": "Product Owner/Facilitator",
    "scenario": "The team plans work for the upcoming sprint.",
    "tasks": [
      "State the sprint goal and success criteria",
      "Review and clarify top backlog items and acceptance criteria",
      "Facilitate estimation and capacity checks",
      "Prioritize scope to fit capacity and dependencies",
      "Identify risks and add mitigation tasks",
      "Confirm Definition of Done and handoff plan",
      "Record the committed sprint backlog"
    ]
  },
  {
    "case": 6,
    "type_of_meeting": "Sprint Review / Demo",
    "speaker_role": "Presenter",
    "scenario": "The team demonstrates completed work to stakeholders.",
    "tasks": [
      "Introduce the sprint goal and context",
      "Demo completed features and show metrics",
      "Highlight customer impact and limitations",
      "Capture stakeholder feedback and approvals",
      "Note follow-ups and defects discovered during demo",
      "Outline next sprint direction briefly"
    ]
  },
  {
    "case": 7,
    "type_of_meeting": "Retrospective",
    "speaker_role": "Facilitator",
    "scenario": "The team reflects on the last sprint to improve.",
    "tasks": [
      "Set the stage and establish psychological safety",
      "Review data (lead time, quality, incidents, goals)",
      "Generate insights (what went well, what to change)",
      "Prioritize the most impactful improvements",
      "Define concrete action items with owners and due dates",
      "Close with appreciations and a quick confidence vote"
    ]
  },
  {
    "case": 8,
    "type_of_meeting": "Project Kickoff",
    "speaker_role": "Project Lead/Facilitator",
    "scenario": "A new project is starting with cross-functional participants.",
    "tasks": [
      "Introduce team members, roles, and RACI",
      "Define scope, deliverables, and success metrics",
      "Present the timeline, milestones, and dependencies",
      "Review constraints, assumptions, and known risks",
      "Agree on ways of working (tools, cadence, comms)",
      "Capture decisions and immediate next steps"
    ]
  },
  {
    "case": 9,
    "type_of_meeting": "Stakeholder Update / Steering Committee",
    "speaker_role": "Project Lead",
    "scenario": "Regular governance check-in with sponsors.",
    "tasks": [
      "Summarize status vs plan (scope, schedule, budget)",
      "Escalate key risks, issues, and decision requests",
      "Show trend metrics and forecast (burn-up/burn-down)",
      "Propose options with pros/cons for approvals",
      "Confirm decisions, funding, or resource changes",
      "Document actions and owners"
    ]
  },
  {
    "case": 10,
    "type_of_meeting": "Architecture Design Review",
    "speaker_role": "Tech Lead/Architect",
    "scenario": "A significant design requires peer and governance review.",
    "tasks": [
      "Present business context, NFRs, and constraints",
      "Walk through architecture diagrams and data flows",
      "Explain trade-offs, alternatives, and rationale",
      "Review standards, security, and compliance alignment",
      "Discuss risks, performance, and scalability plans",
      "Capture feedback and record decisions (ADR)"
    ]
  },
  {
    "case": 11,
    "type_of_meeting": "Incident Postmortem / Root Cause Analysis (RCA)",
    "speaker_role": "Incident Lead",
    "scenario": "After a major incident, the team analyzes causes and fixes.",
    "tasks": [
      "Reconstruct the incident timeline and impact",
      "Present root cause analysis (e.g., 5 Whys/fishbone)",
      "Review what worked and what failed in response",
      "Propose corrective and preventive actions (CAPA)",
      "Assign owners and target dates; define success metrics",
      "Share learnings and plan communications"
    ]
  },
  {
    "case": 12,
    "type_of_meeting": "One-on-One (Manager ↔ Direct Report)",
    "speaker_role": "Manager",
    "scenario": "Regular 1:1 to align on goals, growth, and well-being.",
    "tasks": [
      "Check in on workload, priorities, and morale",
      "Review progress on goals/OKRs and feedback",
      "Unblock challenges and escalate where needed",
      "Discuss career development and learning plans",
      "Agree on focus areas and concrete next steps",
      "Summarize commitments and follow-up dates"
    ]
  },
  {
    "case": 13,
    "type_of_meeting": "Hiring Interview (Technical)",
    "speaker_role": "Interviewer",
    "scenario": "Assess a candidate’s technical and behavioral fit.",
    "tasks": [
      "Set expectations, structure, and timing",
      "Ask technical questions and evaluate problem-solving",
      "Probe on collaboration, ownership, and communication",
      "Clarify role context and answer candidate questions",
      "Take structured notes and score against rubric",
      "Debrief with panel and submit recommendation"
    ]
  },
  {
    "case": 14,
    "type_of_meeting": "Onboarding Orientation",
    "speaker_role": "Facilitator/HR",
    "scenario": "Welcome new hires and enable a smooth start.",
    "tasks": [
      "Introduce company mission, values, and org map",
      "Review policies, tools, and required trainings",
      "Set first-week goals and success criteria",
      "Assign a buddy/mentor and support channels",
      "Guide access/setup checklist completion",
      "Share resources and Q&A"
    ]
  },
  {
    "case": 15,
    "type_of_meeting": "Cross-Team Sync / Alignment",
    "speaker_role": "Coordinator",
    "scenario": "Multiple teams align on dependencies and plans.",
    "tasks": [
      "State shared objectives and desired outcomes",
      "Review dependency map and interface contracts",
      "Resolve ownership, sequencing, and timelines",
      "Surface risks, constraints, and capacity changes",
      "Confirm shared milestones and comms plan",
      "Record decisions and integration test dates"
    ]
  },
  {
    "case": 16,
    "type_of_meeting": "Vendor / Partner Quarterly Business Review (QBR)",
    "speaker_role": "Account Owner",
    "scenario": "Assess vendor performance and plan next quarter.",
    "tasks": [
      "Review SLA/KPI performance and incidents",
      "Discuss roadmap alignment and upcoming changes",
      "Address issues, escalations, and improvement plans",
      "Evaluate commercials, renewals, and savings options",
      "Agree on joint initiatives and success metrics",
      "Set next check-in and action owners"
    ]
  },
  {
    "case": 17,
    "type_of_meeting": "Budget & Resource Planning",
    "speaker_role": "Manager/Finance Partner",
    "scenario": "Plan spend, headcount, and prioritization.",
    "tasks": [
      "Present targets, constraints, and scenarios",
      "Review actuals vs budget and forecast",
      "Prioritize initiatives against ROI and risk",
      "Propose staffing plan and hiring/backfill needs",
      "Decide trade-offs and contingency buffers",
      "Document allocations and approval steps"
    ]
  },
  {
    "case": 18,
    "type_of_meeting": "Marketing Campaign Planning",
    "speaker_role": "Marketing Lead",
    "scenario": "Plan an upcoming multi-channel campaign.",
    "tasks": [
      "Define objective, audience, and messaging",
      "Align on channels, creative, and content calendar",
      "Set KPIs, tracking, and attribution plan",
      "Coordinate with product, sales, and legal/compliance",
      "Map timeline, dependencies, and launch checklist",
      "Assign owners and review cadence"
    ]
  },
  {
    "case": 19,
    "type_of_meeting": "Sales Pipeline Review",
    "speaker_role": "Sales Lead",
    "scenario": "Inspect pipeline health and improve conversion.",
    "tasks": [
      "Review pipeline by stage and conversion rates",
      "Deep-dive top deals: next steps, blockers, help needed",
      "Calibrate forecasts and commit",
      "Share competitive insights and win/loss learnings",
      "Coach on messaging, objection handling, and tools",
      "Assign actions and follow-up dates"
    ]
  },
  {
    "case": 20,
    "type_of_meeting": "Customer Discovery / User Interview",
    "speaker_role": "Researcher/Product Manager",
    "scenario": "Understand user needs, pain points, and workflows.",
    "tasks": [
      "Build rapport and explain purpose/consent",
      "Ask open-ended questions and probe for examples",
      "Test assumptions or prototypes; observe behavior",
      "Note quotes, emotions, and workarounds",
      "Summarize insights and validate understanding",
      "Share next steps and appreciation"
    ]
  },
  {
    "case": 21,
    "type_of_meeting": "Training Workshop / Enablement",
    "speaker_role": "Trainer/Facilitator",
    "scenario": "Upskill the team on a tool, process, or skill.",
    "tasks": [
      "Share agenda, objectives, and prerequisites",
      "Deliver concepts with live demos and exercises",
      "Monitor participation and check understanding",
      "Provide practice scenarios and feedback",
      "Offer resources, cheat sheets, and recordings",
      "Collect feedback and set follow-up practice"
    ]
  },
  {
    "case": 22,
    "type_of_meeting": "Town Hall / All-Hands",
    "speaker_role": "Host/Executive",
    "scenario": "Company-wide updates and Q&A.",
    "tasks": [
      "Welcome, outline agenda, and norms",
      "Share business updates (product, customers, finance)",
      "Celebrate wins, recognitions, and new joins",
      "Address questions (live and pre-submitted)",
      "Reiterate priorities and calls to action",
      "Provide links to recording and follow-ups"
    ]
  },
  {
    "case": 23,
    "type_of_meeting": "Compliance & Security Review",
    "speaker_role": "Security/Compliance Lead",
    "scenario": "Review a change/product for regulatory and security fit.",
    "tasks": [
      "Present data classification and threat model",
      "Map controls to standards (e.g., ISO, SOC, GDPR)",
      "Review privacy, access, logging, and retention",
      "Plan testing (pen test, DAST/SAST) and remediation",
      "Assess residual risk and obtain approvals",
      "Record exceptions and audit trail"
    ]
  },
  {
    "case": 24,
    "type_of_meeting": "UX Design Critique",
    "speaker_role": "Designer/Facilitator",
    "scenario": "Gather structured feedback on a design.",
    "tasks": [
      "State user goals, constraints, and success metrics",
      "Walk through flows, components, and rationale",
      "Facilitate feedback using a structured method",
      "Check accessibility, localization, and responsiveness",
      "Decide changes, priorities, and experiments",
      "Log action items and update design docs"
    ]
  },
  {
    "case": 25,
    "type_of_meeting": "Brainstorming / Ideation Session",
    "speaker_role": "Facilitator",
    "scenario": "Generate diverse ideas to solve a defined problem.",
    "tasks": [
      "Define the problem statement and success criteria",
      "Set rules (defer judgment, build on ideas, quantity first)",
      "Run divergent ideation (silent + round-robin)",
      "Cluster themes and conduct dot-voting",
      "Develop top ideas into quick concepts",
      "Assign owners for experiments and next steps"
    ]
  },
  {
    "case": 26,
    "type_of_meeting": "Go/No-Go Release Readiness",
    "speaker_role": "Release Manager",
    "scenario": "Decide whether to proceed with a launch/deployment.",
    "tasks": [
      "Review readiness checklist (tests, docs, training)",
      "Confirm cutover, rollback, and comms plans",
      "Verify monitoring, on-call, and capacity",
      "Evaluate open risks and mitigations",
      "Record decision, sign-offs, and contingencies",
      "Schedule post-release validation"
    ]
  },
  {
    "case": 27,
    "type_of_meeting": "Change Advisory Board (CAB)",
    "speaker_role": "Change Manager",
    "scenario": "Approve or reject high-impact changes.",
    "tasks": [
      "Present change description, scope, and impact assessment",
      "Review risk rating, dependencies, and blackout windows",
      "Confirm backout plan and validation steps",
      "Capture questions, conditions, or deferrals",
      "Record approve/reject decisions and owners",
      "Publish change schedule and notifications"
    ]
  },
  {
    "case": 28,
    "type_of_meeting": "Casual Coffee Chat / Small Talk (Informal)",
    "speaker_role": "Host/Peer",
    "scenario": "Informal catch-up to build rapport and team cohesion.",
    "tasks": [
      "Greet warmly and check in on well-being",
      "Share light non-work updates and interests",
      "Celebrate recent wins and acknowledge efforts",
      "Swap tips (tools, remote setup, local events)",
      "Identify any low-friction ways to help each other",
      "Wrap with appreciation and optional follow-up"
    ]
  }
]
```