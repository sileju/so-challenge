# SO Challenge

A Python project for the SO challenge, separating data collection, visualization, and milestone definitions.

## Modules

- `data_fetcher.py`: Handles data collection from various sources.
- `plotter.py`: Manages plotting and data visualization.
- `milestones.py`: Defines project milestones.

## Dependencies

Managed through `pyproject.toml` using uv:

- pandas
- matplotlib
- requests
- pytest (dev)

## Setup

Use uv to install dependencies:

```bash
uv sync
```

Run tests:

```bash
uv run pytest
```