"""

Milestone definitions module for the SO challenge.

This module defines milestones for the project.

"""

import pandas as pd


def overlay_milestones(axes, milestones):
    """
    Overlay milestone markers on a matplotlib axes.

    Args:
        axes: Matplotlib axes object.
        milestones: Dict of date strings to milestone names.
    """
    if not isinstance(milestones, dict):
        raise ValueError("Milestones must be a dictionary")

    # Sort milestones by date
    sorted_milestones = sorted(milestones.items(), key=lambda x: pd.to_datetime(x[0]))

    for date_str, name in sorted_milestones:
        date = pd.to_datetime(date_str)
        # Add vertical line
        axes.axvline(x=date, color='red', linestyle='--')
        # Add label
        axes.text(date, axes.get_ylim()[1] * 0.9, name, rotation=90, verticalalignment='top', fontsize=8)