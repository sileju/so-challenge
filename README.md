# SO Challenge

A Python project for analyzing Stack Overflow question trends from 2008-2024, visualizing monthly counts with a 12-month rolling average, and overlaying key AI development milestones.

## Features

- **Data Fetching**: Retrieves monthly question counts from Stack Overflow API with caching and retry logic.
- **Visualization**: Plots monthly trends and rolling averages using matplotlib.
- **Milestones**: Overlays markers for major AI breakthroughs on the timeline.

## Modules

- `data_fetcher.py`: Fetches and caches SO data.
- `plotter.py`: Generates plots with rolling averages.
- `milestones.py`: Adds milestone overlays.
- `main.py`: Combines everything into a full workflow.

## Requirements

See `docs/requirements.md` for detailed functional and non-functional requirements.

## Setup

1. Install dependencies: `uv sync`
2. Run the project: `PYTHONPATH=. uv run python main.py`

## Testing

Run all tests: `PYTHONPATH=. uv run pytest`

## Dependencies

Managed via `pyproject.toml` with uv:
- pandas
- matplotlib
- requests
- pytest (dev)