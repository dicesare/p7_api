import os


def get_model_path():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    model_base_directory = os.path.join(current_directory, "model_saved", "Sentiment140")

    model_paths = [os.path.join(model_base_directory, dir_name) for dir_name in os.listdir(model_base_directory)]
    model_paths = [path for path in model_paths if os.path.isdir(path)]

    # Trier les chemins de modèle en fonction de leur date de modification
    model_paths = sorted(model_paths, key=os.path.getmtime, reverse=True)

    most_recent_model_path = model_paths[0] if model_paths else None

    return most_recent_model_path
