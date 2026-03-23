# 009 — Write Tests for Plotter

**Date**: 2026-03-23
**Tool**: GitHub Copilot
**Model**: Grok Code Fast 1
**Iterations**: 1

## Prompt

**2026-03-23 00:00**

Write pytest tests for plotter.py. The module should:

Accept a pandas DataFrame with columns: year_month and question_count
Generate a visualization where:
The x-axis is labeled Month and covers the timespan in the data
The y-axis is labeled Questions
A blue line shows the monthly question counts
A red line shows the 12-month rolling average

Write the tests BEFORE implementing the plotting logic. Use mocking if necessary to avoid actually generating files or rendering plots in tests. Include tests for:

The function accepts correctly formatted DataFrames
The resulting plot contains two lines with the correct colors
Axes are labeled correctly
Rolling average is calculated correctly for the given data

Save the diary entry and commit everything with a proper commit message describing what was added.