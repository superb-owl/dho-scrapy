import plotly.express as px

from data_models.message_db import MessageDB
from experiments.utils.paths import jsonl_path


def main():
    experiment()


def experiment(show_plot: bool = True):

    # Load data
    messages = MessageDB.from_file(jsonl_path=jsonl_path).get_all_messages()

    # Experiment
    # ...

    # Plot
    fig = px.scatter(title="Experiment Template")
    if show_plot:
        fig.show()


if __name__ == "__main__":
    main()
