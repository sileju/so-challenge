# 011 — Write Tests for Milestones

**Date**: 2026-03-23
**Tool**: GitHub Copilot
**Model**: Grok Code Fast 1
**Iterations**: 1

## Prompt

**2026-03-23 00:00**

Write pytest tests for milestones.py. The module should:

Accept a visualization (e.g., a timeline or plot) of AI developments
Overlay markers for key AI breakthroughs from the course’s Interactive AI Timeline:
Transformer (June 2017)
ChatGPT (November 2022)
GPT-4 (March 2023)
Cursor and AI IDEs (August 2023)
Claude Code (February 2025)
GitHub Copilot Agent Mode (February 2025)

Write the tests BEFORE implementing the milestone overlay logic. Use mocking if necessary to avoid actually generating files or rendering plots in tests. Include tests for:

Correct placement of milestone markers on the timeline according to the dates
Labels for milestones match the breakthrough names exactly
Markers appear in the correct order along the time axis
The function accepts correctly formatted input data

Save the diary entry and commit everything with a proper commit message describing what was added.