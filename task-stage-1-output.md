# Stage 1 Output: Mermaid Diagrams for Speaking Flow

This document contains Mermaid diagrams demonstrating the speaking flow for each type of meeting.

**Legend:**
- 🔵 Blue nodes = Action steps where the speaker needs to communicate
- ⚪ Other nodes = Internal thoughts, decisions, or passive actions

---

## Case 1: Daily Stand-up Meeting
**Role:** Attendee  
**Scenario:** Join every morning to catch up with the team

<div align="center">

```mermaid
graph TD
    Start([Join Meeting]) --> Listen1[Listen to agenda/intro]
    Listen1 --> Prepare{My turn?}
    Prepare -->|Yes| Share1[Share yesterday's progress]
    Share1 --> Share2[Share today's plan]
    Share2 --> Blockers{Any blockers?}
    Blockers -->|Yes| Share3[Explain blockers clearly]
    Blockers -->|No| Listen2[Continue to next topic]
    Share3 --> Listen2
    Listen2 --> OthersSpeak[Listen to teammates]
    OthersSpeak --> FollowUp{Need to follow up?}
    FollowUp -->|Yes| Respond[Ask clarifying questions or offer help]
    FollowUp -->|No| Wait[Wait for others]
    Respond --> Wait
    Wait --> End([Meeting ends])
    
    style Share1 fill:#4A90E2,color:#fff
    style Share2 fill:#4A90E2,color:#fff
    style Share3 fill:#4A90E2,color:#fff
    style Respond fill:#4A90E2,color:#fff
```

</div>

---

## Case 2: Weekly Stand-up Meeting
**Role:** Attendee  
**Scenario:** Join every week to catch up with the team

<div align="center">

```mermaid
graph TD
    Start([Join Meeting]) --> Listen1[Listen to intro]
    Listen1 --> YourTurn{My turn?}
    YourTurn -->|Yes| Highlights[Share highlights of the week]
    Highlights --> Lowlights[Share lowlights/challenges]
    Lowlights --> Summary[Summarize completed work]
    Summary --> NextWeek[Share planned work for next week]
    NextWeek --> Dependencies{Cross-team dependencies?}
    Dependencies -->|Yes| Coordinate[Mention dependencies and coordinate]
    Dependencies -->|No| Risks{Risks or blockers?}
    Coordinate --> Risks
    Risks -->|Yes| Raise[Raise risks that need attention]
    Risks -->|No| Listen2[Listen to others]
    Raise --> Listen2
    Listen2 --> Questions{Questions/Comments?}
    Questions -->|Yes| Engage[Ask questions or provide input]
    Questions -->|No| End([Meeting ends])
    Engage --> End
    
    style Highlights fill:#4A90E2,color:#fff
    style Lowlights fill:#4A90E2,color:#fff
    style Summary fill:#4A90E2,color:#fff
    style NextWeek fill:#4A90E2,color:#fff
    style Coordinate fill:#4A90E2,color:#fff
    style Raise fill:#4A90E2,color:#fff
    style Engage fill:#4A90E2,color:#fff
```

</div>

---

## Case 3: Knowledge Sharing Meeting
**Role:** Facilitator  
**Scenario:** Chair the meeting where a presenter shares a topic

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Welcome[Welcome everyone and greet]
    Welcome --> Agenda[Outline agenda and timing]
    Agenda --> Context[Provide opening remarks for context]
    Context --> Introduce[Introduce presenter and topic]
    Introduce --> Handoff[Hand over to presenter]
    Handoff --> Monitor[Monitor time during presentation]
    Monitor --> QA{Q&A time?}
    QA -->|Yes| FacilitateQA[Facilitate Q&A session]
    FacilitateQA --> Manage[Manage time and questions]
    Manage --> Closing[Summarize key takeaways]
    Closing --> Resources[Share links to resources]
    Resources --> Thanks[Thank presenter and attendees]
    Thanks --> End([Meeting ends])
    
    style Welcome fill:#4A90E2,color:#fff
    style Agenda fill:#4A90E2,color:#fff
    style Context fill:#4A90E2,color:#fff
    style Introduce fill:#4A90E2,color:#fff
    style Handoff fill:#4A90E2,color:#fff
    style FacilitateQA fill:#4A90E2,color:#fff
    style Manage fill:#4A90E2,color:#fff
    style Closing fill:#4A90E2,color:#fff
    style Resources fill:#4A90E2,color:#fff
    style Thanks fill:#4A90E2,color:#fff
```

</div>

---

## Case 4: Technical Meeting / Code Review
**Role:** Communicator/Presenter  
**Scenario:** Discuss technical issue or present code for review

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Intro[Introduce context and scope]
    Intro --> Goals[State goals of the review]
    Goals --> Present[Present solution and design choices]
    Present --> Tradeoffs[Explain trade-offs made]
    Tradeoffs --> Walkthrough[Walk through code diffs]
    Walkthrough --> Tests[Demonstrate tests]
    Tests --> Ask[Ask for feedback and questions]
    Ask --> Listen[Listen to suggestions]
    Listen --> Clarify{Need clarification?}
    Clarify -->|Yes| Discuss[Discuss and clarify points]
    Clarify -->|No| Agreement[Agree on changes and owners]
    Discuss --> Agreement
    Agreement --> NextSteps[Plan next steps and timeline]
    NextSteps --> End([Meeting ends])
    
    style Intro fill:#4A90E2,color:#fff
    style Goals fill:#4A90E2,color:#fff
    style Present fill:#4A90E2,color:#fff
    style Tradeoffs fill:#4A90E2,color:#fff
    style Walkthrough fill:#4A90E2,color:#fff
    style Tests fill:#4A90E2,color:#fff
    style Ask fill:#4A90E2,color:#fff
    style Discuss fill:#4A90E2,color:#fff
    style Agreement fill:#4A90E2,color:#fff
    style NextSteps fill:#4A90E2,color:#fff
```

</div>

---

## Case 5: Sprint Planning
**Role:** Product Owner/Facilitator  
**Scenario:** Plan work for the upcoming sprint

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Goal[State sprint goal and success criteria]
    Goal --> Review[Review top backlog items]
    Review --> Clarify[Clarify acceptance criteria]
    Clarify --> Estimate[Facilitate estimation discussion]
    Estimate --> Capacity[Check capacity constraints]
    Capacity --> Prioritize[Prioritize scope to fit capacity]
    Prioritize --> Dependencies{Dependencies identified?}
    Dependencies -->|Yes| Discuss[Discuss dependencies]
    Dependencies -->|No| Risks
    Discuss --> Risks{Risks identified?}
    Risks -->|Yes| Mitigation[Identify mitigation tasks]
    Risks -->|No| DoD[Confirm Definition of Done]
    Mitigation --> DoD
    DoD --> Record[Record committed sprint backlog]
    Record --> End([Meeting ends])
    
    style Goal fill:#4A90E2,color:#fff
    style Review fill:#4A90E2,color:#fff
    style Clarify fill:#4A90E2,color:#fff
    style Estimate fill:#4A90E2,color:#fff
    style Capacity fill:#4A90E2,color:#fff
    style Prioritize fill:#4A90E2,color:#fff
    style Discuss fill:#4A90E2,color:#fff
    style Mitigation fill:#4A90E2,color:#fff
    style DoD fill:#4A90E2,color:#fff
    style Record fill:#4A90E2,color:#fff
```

</div>

---

## Case 6: Sprint Review / Demo
**Role:** Presenter  
**Scenario:** Demonstrate completed work to stakeholders

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> IntroGoal[Introduce sprint goal and context]
    IntroGoal --> Demo[Demo completed features]
    Demo --> Metrics[Show relevant metrics]
    Metrics --> Impact[Highlight customer impact]
    Impact --> Limitations{Any limitations?}
    Limitations -->|Yes| Explain[Explain limitations]
    Limitations -->|No| Feedback
    Explain --> Feedback[Capture stakeholder feedback]
    Feedback --> Approvals[Note approvals received]
    Approvals --> FollowUps{Follow-ups needed?}
    FollowUps -->|Yes| Document[Note follow-ups and defects]
    FollowUps -->|No| NextSprint
    Document --> NextSprint[Outline next sprint direction]
    NextSprint --> End([Meeting ends])
    
    style IntroGoal fill:#4A90E2,color:#fff
    style Demo fill:#4A90E2,color:#fff
    style Metrics fill:#4A90E2,color:#fff
    style Impact fill:#4A90E2,color:#fff
    style Explain fill:#4A90E2,color:#fff
    style Feedback fill:#4A90E2,color:#fff
    style Approvals fill:#4A90E2,color:#fff
    style Document fill:#4A90E2,color:#fff
    style NextSprint fill:#4A90E2,color:#fff
```

</div>

---

## Case 7: Retrospective
**Role:** Facilitator  
**Scenario:** Team reflects on the last sprint to improve

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> SetStage[Set the stage and establish safety]
    SetStage --> ReviewData[Review data: lead time, quality, incidents]
    ReviewData --> WentWell[Generate insights: what went well]
    WentWell --> ToChange[Generate insights: what to change]
    ToChange --> Prioritize[Prioritize most impactful improvements]
    Prioritize --> Actions[Define concrete action items]
    Actions --> Owners[Assign owners and due dates]
    Owners --> Appreciations[Close with appreciations]
    Appreciations --> Vote[Quick confidence vote]
    Vote --> End([Meeting ends])
    
    style SetStage fill:#4A90E2,color:#fff
    style ReviewData fill:#4A90E2,color:#fff
    style WentWell fill:#4A90E2,color:#fff
    style ToChange fill:#4A90E2,color:#fff
    style Prioritize fill:#4A90E2,color:#fff
    style Actions fill:#4A90E2,color:#fff
    style Owners fill:#4A90E2,color:#fff
    style Appreciations fill:#4A90E2,color:#fff
    style Vote fill:#4A90E2,color:#fff
```

</div>

---

## Case 8: Project Kickoff
**Role:** Project Lead/Facilitator  
**Scenario:** Starting a new project with cross-functional team

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Intros[Introduce team members and roles]
    Intros --> RACI[Clarify RACI matrix]
    RACI --> Scope[Define scope and deliverables]
    Scope --> Metrics[Define success metrics]
    Metrics --> Timeline[Present timeline and milestones]
    Timeline --> Dependencies[Review dependencies]
    Dependencies --> Constraints[Review constraints and assumptions]
    Constraints --> Risks[Discuss known risks]
    Risks --> Ways[Agree on ways of working]
    Ways --> Tools[Agree on tools and communication]
    Tools --> Decisions[Capture decisions]
    Decisions --> Next[Outline immediate next steps]
    Next --> End([Meeting ends])
    
    style Intros fill:#4A90E2,color:#fff
    style RACI fill:#4A90E2,color:#fff
    style Scope fill:#4A90E2,color:#fff
    style Metrics fill:#4A90E2,color:#fff
    style Timeline fill:#4A90E2,color:#fff
    style Dependencies fill:#4A90E2,color:#fff
    style Constraints fill:#4A90E2,color:#fff
    style Risks fill:#4A90E2,color:#fff
    style Ways fill:#4A90E2,color:#fff
    style Tools fill:#4A90E2,color:#fff
    style Decisions fill:#4A90E2,color:#fff
    style Next fill:#4A90E2,color:#fff
```

</div>

---

## Case 10: Architecture Design Review
**Role:** Tech Lead/Architect  
**Scenario:** Significant design requires peer and governance review

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Context[Present business context]
    Context --> NFRs[Explain NFRs and constraints]
    NFRs --> Diagrams[Walk through architecture diagrams]
    Diagrams --> DataFlows[Explain data flows]
    DataFlows --> Tradeoffs[Explain trade-offs and alternatives]
    Tradeoffs --> Rationale[Provide rationale for choices]
    Rationale --> Standards[Review standards and compliance]
    Standards --> Security[Review security alignment]
    Security --> Risks[Discuss risks and scalability]
    Risks --> Performance[Discuss performance plans]
    Performance --> Capture[Capture feedback]
    Capture --> Decisions[Record decisions in ADR]
    Decisions --> End([Meeting ends])
    
    style Context fill:#4A90E2,color:#fff
    style NFRs fill:#4A90E2,color:#fff
    style Diagrams fill:#4A90E2,color:#fff
    style DataFlows fill:#4A90E2,color:#fff
    style Tradeoffs fill:#4A90E2,color:#fff
    style Rationale fill:#4A90E2,color:#fff
    style Standards fill:#4A90E2,color:#fff
    style Security fill:#4A90E2,color:#fff
    style Risks fill:#4A90E2,color:#fff
    style Performance fill:#4A90E2,color:#fff
    style Capture fill:#4A90E2,color:#fff
    style Decisions fill:#4A90E2,color:#fff
```

</div>

---

## Case 11: Incident Postmortem / Root Cause Analysis (RCA)
**Role:** Incident Lead  
**Scenario:** Analyze causes and fixes after a major incident

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Timeline[Reconstruct incident timeline]
    Timeline --> Impact[Present impact assessment]
    Impact --> RootCause[Present root cause analysis]
    RootCause --> Method[Explain 5 Whys or fishbone]
    Method --> Worked[Review what worked in response]
    Worked --> Failed[Review what failed]
    Failed --> Corrective[Propose corrective actions]
    Corrective --> Preventive[Propose preventive actions]
    Preventive --> Assign[Assign owners and target dates]
    Assign --> Metrics[Define success metrics]
    Metrics --> Learnings[Share learnings]
    Learnings --> Comms[Plan communications]
    Comms --> End([Meeting ends])
    
    style Timeline fill:#4A90E2,color:#fff
    style Impact fill:#4A90E2,color:#fff
    style RootCause fill:#4A90E2,color:#fff
    style Method fill:#4A90E2,color:#fff
    style Worked fill:#4A90E2,color:#fff
    style Failed fill:#4A90E2,color:#fff
    style Corrective fill:#4A90E2,color:#fff
    style Preventive fill:#4A90E2,color:#fff
    style Assign fill:#4A90E2,color:#fff
    style Metrics fill:#4A90E2,color:#fff
    style Learnings fill:#4A90E2,color:#fff
    style Comms fill:#4A90E2,color:#fff
```

</div>

---

## Case 15: Cross-Team Sync / Alignment
**Role:** Coordinator  
**Scenario:** Multiple teams align on dependencies and plans

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Objectives[State shared objectives]
    Objectives --> Outcomes[Clarify desired outcomes]
    Outcomes --> DependencyMap[Review dependency map]
    DependencyMap --> Interfaces[Review interface contracts]
    Interfaces --> Ownership[Resolve ownership questions]
    Ownership --> Sequencing[Resolve sequencing and timelines]
    Sequencing --> Risks{Risks identified?}
    Risks -->|Yes| SurfaceRisks[Surface risks and constraints]
    Risks -->|No| Milestones
    SurfaceRisks --> Capacity[Discuss capacity changes]
    Capacity --> Milestones[Confirm shared milestones]
    Milestones --> CommsPlans[Confirm communications plan]
    CommsPlans --> Record[Record decisions]
    Record --> Integration[Set integration test dates]
    Integration --> End([Meeting ends])
    
    style Objectives fill:#4A90E2,color:#fff
    style Outcomes fill:#4A90E2,color:#fff
    style DependencyMap fill:#4A90E2,color:#fff
    style Interfaces fill:#4A90E2,color:#fff
    style Ownership fill:#4A90E2,color:#fff
    style Sequencing fill:#4A90E2,color:#fff
    style SurfaceRisks fill:#4A90E2,color:#fff
    style Capacity fill:#4A90E2,color:#fff
    style Milestones fill:#4A90E2,color:#fff
    style CommsPlans fill:#4A90E2,color:#fff
    style Record fill:#4A90E2,color:#fff
    style Integration fill:#4A90E2,color:#fff
```

</div>

---

## Case 21: Training Workshop / Enablement
**Role:** Trainer/Facilitator  
**Scenario:** Upskill the team on a tool, process, or skill

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Agenda[Share agenda and objectives]
    Agenda --> Prerequisites[Review prerequisites]
    Prerequisites --> Concepts[Deliver key concepts]
    Concepts --> Demo[Provide live demo]
    Demo --> Exercises[Guide through exercises]
    Exercises --> Monitor[Monitor participation]
    Monitor --> Check[Check understanding]
    Check --> Practice[Provide practice scenarios]
    Practice --> Feedback[Provide feedback on practice]
    Feedback --> Resources[Offer resources and cheat sheets]
    Resources --> Recording[Share recording info]
    Recording --> Collect[Collect feedback]
    Collect --> FollowUp[Set follow-up practice]
    FollowUp --> End([Meeting ends])
    
    style Agenda fill:#4A90E2,color:#fff
    style Prerequisites fill:#4A90E2,color:#fff
    style Concepts fill:#4A90E2,color:#fff
    style Demo fill:#4A90E2,color:#fff
    style Exercises fill:#4A90E2,color:#fff
    style Monitor fill:#4A90E2,color:#fff
    style Check fill:#4A90E2,color:#fff
    style Practice fill:#4A90E2,color:#fff
    style Feedback fill:#4A90E2,color:#fff
    style Resources fill:#4A90E2,color:#fff
    style Recording fill:#4A90E2,color:#fff
    style Collect fill:#4A90E2,color:#fff
    style FollowUp fill:#4A90E2,color:#fff
```

</div>

---

## Case 26: Go/No-Go Release Readiness
**Role:** Release Manager  
**Scenario:** Decide whether to proceed with a launch/deployment

<div align="center">

```mermaid
graph TD
    Start([Start Meeting]) --> Checklist[Review readiness checklist]
    Checklist --> Tests[Confirm test completion]
    Tests --> Docs[Confirm documentation status]
    Docs --> Training[Confirm training completion]
    Training --> Cutover[Confirm cutover plan]
    Cutover --> Rollback[Confirm rollback plan]
    Rollback --> Comms[Confirm communications plan]
    Comms --> Monitoring[Verify monitoring setup]
    Monitoring --> OnCall[Verify on-call readiness]
    OnCall --> Capacity[Verify capacity]
    Capacity --> OpenRisks{Open risks?}
    OpenRisks -->|Yes| Evaluate[Evaluate risks and mitigations]
    OpenRisks -->|No| Decision
    Evaluate --> Decision[Record Go/No-Go decision]
    Decision --> SignOffs[Collect sign-offs]
    SignOffs --> Contingencies[Record contingencies]
    Contingencies --> Schedule[Schedule post-release validation]
    Schedule --> End([Meeting ends])
    
    style Checklist fill:#4A90E2,color:#fff
    style Tests fill:#4A90E2,color:#fff
    style Docs fill:#4A90E2,color:#fff
    style Training fill:#4A90E2,color:#fff
    style Cutover fill:#4A90E2,color:#fff
    style Rollback fill:#4A90E2,color:#fff
    style Comms fill:#4A90E2,color:#fff
    style Monitoring fill:#4A90E2,color:#fff
    style OnCall fill:#4A90E2,color:#fff
    style Capacity fill:#4A90E2,color:#fff
    style Evaluate fill:#4A90E2,color:#fff
    style Decision fill:#4A90E2,color:#fff
    style SignOffs fill:#4A90E2,color:#fff
    style Contingencies fill:#4A90E2,color:#fff
    style Schedule fill:#4A90E2,color:#fff
```

</div>

---

**End of Stage 1 Output**
