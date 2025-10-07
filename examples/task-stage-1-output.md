# Stage 1 Output: Speaking Flow Diagrams

This document contains Mermaid diagrams demonstrating the speaking flow for different meeting types tailored for an ML Engineer with 5 years of experience at Google.

## Case 1: Daily Stand-up Meeting (Attendee)

<div align="center">

```mermaid
graph TD
    Start([Join Meeting]) --> A1[Listen actively to ongoing updates]
    A1 --> A2[Wait for your turn]
    A2 --> B1[Greet the team briefly]
    B1 --> B2[Share yesterday's accomplishments]
    B2 --> B3[Outline today's planned work]
    B3 --> B4[Mention any blockers or dependencies]
    B4 --> C1[Listen to other teammates' updates]
    C1 --> C2{Need to follow up?}
    C2 -->|Yes| C3[Ask clarifying questions or offer help]
    C2 -->|No| C4[Acknowledge and take notes]
    C3 --> End([Meeting Continues])
    C4 --> End

    style B1 fill:#4A90E2,color:#fff
    style B2 fill:#4A90E2,color:#fff
    style B3 fill:#4A90E2,color:#fff
    style B4 fill:#4A90E2,color:#fff
    style C3 fill:#4A90E2,color:#fff
```

</div>

## Case 2: Weekly Stand-up Meeting (Attendee)

<div align="center">

```mermaid
graph TD
    Start([Join Meeting]) --> A1[Listen actively to ongoing updates]
    A1 --> A2[Wait for your turn]
    A2 --> B1[Greet the team]
    B1 --> B2[Summarize last week's key achievements]
    B2 --> B3[Highlight significant ML metrics or model improvements]
    B3 --> B4[Outline this week's priorities and goals]
    B4 --> B5[Discuss any blockers or resource needs]
    B5 --> C1[Listen to other teammates' updates]
    C1 --> C2{Need to follow up or collaborate?}
    C2 -->|Yes| C3[Propose collaboration or offer assistance]
    C2 -->|No| C4[Acknowledge and note action items]
    C3 --> End([Meeting Continues])
    C4 --> End

    style B1 fill:#4A90E2,color:#fff
    style B2 fill:#4A90E2,color:#fff
    style B3 fill:#4A90E2,color:#fff
    style B4 fill:#4A90E2,color:#fff
    style B5 fill:#4A90E2,color:#fff
    style C3 fill:#4A90E2,color:#fff
```

</div>

## Case 3: Knowledge Sharing Meeting (Facilitator)

<div align="center">

```mermaid
graph TD
    Start([Meeting Start Time]) --> A1[Welcome everyone as they join]
    A1 --> A2[Wait for attendees to settle in]
    A2 --> B1[Open the meeting with greeting]
    B1 --> B2[Provide context for the session]
    B2 --> B3[Introduce the presenter with background]
    B3 --> B4[Introduce the topic and its relevance]
    B4 --> B5[Set expectations for Q&A format]
    B5 --> C1[Hand over to presenter]
    C1 --> C2[Monitor presentation and time]
    C2 --> D1{Q&A time?}
    D1 -->|Yes| D2[Facilitate Q&A session]
    D1 -->|No| E1[Summarize key takeaways]
    D2 --> E1
    E1 --> E2[Thank the presenter]
    E2 --> E3[Provide closing remarks]
    E3 --> E4[Announce next session details if applicable]
    E4 --> End([End Meeting])

    style B1 fill:#4A90E2,color:#fff
    style B2 fill:#4A90E2,color:#fff
    style B3 fill:#4A90E2,color:#fff
    style B4 fill:#4A90E2,color:#fff
    style B5 fill:#4A90E2,color:#fff
    style D2 fill:#4A90E2,color:#fff
    style E1 fill:#4A90E2,color:#fff
    style E2 fill:#4A90E2,color:#fff
    style E3 fill:#4A90E2,color:#fff
    style E4 fill:#4A90E2,color:#fff
```

</div>

## Case 4: Technical Meeting / Code Review (Presenter/Communicator)

<div align="center">

```mermaid
graph TD
    Start([Meeting Scheduled]) --> A1[Prepare materials and context]
    A1 --> B1[Greet attendees and thank them for joining]
    B1 --> B2[State the purpose and agenda of the meeting]
    B2 --> B3[Provide background context of the technical issue]
    B3 --> B4[Explain why this issue matters to the team/project]
    B4 --> C1[Present the technical problem in detail]
    C1 --> C2[Walk through code or system architecture]
    C2 --> C3[Propose solution approach and alternatives]
    C3 --> C4[Explain trade-offs and your recommendation]
    C4 --> D1[Open floor for questions and feedback]
    D1 --> D2{Concerns or suggestions raised?}
    D2 -->|Yes| D3[Address concerns and discuss alternatives]
    D2 -->|No| E1[Summarize agreement or key points]
    D3 --> D4{Need more discussion?}
    D4 -->|Yes| D1
    D4 -->|No| E1
    E1 --> E2[Outline next steps and action items]
    E2 --> E3[Assign ownership and deadlines]
    E3 --> E4[Thank everyone for their input]
    E4 --> End([End Meeting])

    style B1 fill:#4A90E2,color:#fff
    style B2 fill:#4A90E2,color:#fff
    style B3 fill:#4A90E2,color:#fff
    style B4 fill:#4A90E2,color:#fff
    style C1 fill:#4A90E2,color:#fff
    style C2 fill:#4A90E2,color:#fff
    style C3 fill:#4A90E2,color:#fff
    style C4 fill:#4A90E2,color:#fff
    style D1 fill:#4A90E2,color:#fff
    style D3 fill:#4A90E2,color:#fff
    style E1 fill:#4A90E2,color:#fff
    style E2 fill:#4A90E2,color:#fff
    style E3 fill:#4A90E2,color:#fff
    style E4 fill:#4A90E2,color:#fff
```

</div>
