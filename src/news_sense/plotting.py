import matplotlib.pyplot as plt
import seaborn as sns


def set_plot_style():
    """Set the global plotting style for the News-Sense project."""
    
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        font_scale=1.0,
    )

    plt.rcParams.update({
        "figure.figsize": (8, 5),
        "figure.dpi": 120,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "axes.labelweight": "medium",
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.titlesize": 16,
    })

def get_colour(name):
    """Return a News-Sense project colour by name."""
    
    if name not in NEWS_SENSE_PALETTE:
        raise ValueError(
            f"Unknown colour '{name}'. "
            f"Choose from: {', '.join(NEWS_SENSE_PALETTE)}"
        )

    return NEWS_SENSE_PALETTE[name]

def get_palette(n):
    """Return a categorical palette with n colours."""
    
    return sns.blend_palette(
        [
            NEWS_SENSE_PALETTE["primary"],
            NEWS_SENSE_PALETTE["secondary"],
            NEWS_SENSE_PALETTE["accent"],
        ],
        n_colors=n,
    )

global NEWS_SENSE_PALETTE
NEWS_SENSE_PALETTE = {
    "primary": "#2F5D62",
    "secondary": "#5E8C8A",
    "accent": "#D97A3A",
    "positive": "#4C956C",
    "negative": "#D1495B",
    "neutral": "#8A8A8A",
}