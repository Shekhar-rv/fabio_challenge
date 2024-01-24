from typing import List
from model_filter import filter_by_bounding_box, filter_by_faces, filter_by_volume
from utils import (
    get_data,
    get_dict_stats,
    area_data_checker,
    score_calc
    )
from json import dumps


if __name__ == "__main__":
    print("Loading the data ...\n")
    # Get the data and compare the stats
    attempt1 = get_data(file_name="attempt1.json")
    attempt2 = get_data(file_name="attempt2.json")
    attempt3 = get_data(file_name="attempt3.json")
    attempt4 = get_data(file_name="attempt4.json")
    target = get_data(file_name="target.json")

    print("Computing the stats ... \n")
    # Compute the stats for each model
    attempt1_stats = get_dict_stats(data=attempt1)
    attempt2_stats = get_dict_stats(data=attempt2)
    attempt3_stats = get_dict_stats(data=attempt3)
    attempt4_stats = get_dict_stats(data=attempt4)
    target_stats = get_dict_stats(data=target)

    attempted_models=[attempt1, attempt2, attempt3, attempt4]

    print("\nFiltering the models ... \n")
    # Filtering the models based on the bounding box, volume and faces
    filtered_models, incorrect_models = filter_by_bounding_box(
        target_model=target,
        attempted_models=attempted_models
    )
    filtered_models, incorrect_models = filter_by_volume(
        target_model=target,
        attempted_models=filtered_models,
        incorrect_models=incorrect_models
    )
    filtered_models, incorrect_models = filter_by_faces(
        target_model=target,
        attempted_models=filtered_models,
        incorrect_models=incorrect_models
    )

    print(f"\nThe following models matches with the target model: {[filtered_model['file_name'] for filtered_model in filtered_models]} \n")

    # Compute the stats for each model
    attempt1_stats = area_data_checker(target_model=target, attempted_model=attempt1, stats_dict=attempt1_stats)
    attempt2_stats = area_data_checker(target_model=target, attempted_model=attempt2, stats_dict=attempt2_stats)
    attempt3_stats = area_data_checker(target_model=target, attempted_model=attempt3, stats_dict=attempt3_stats)
    attempt4_stats = area_data_checker(target_model=target, attempted_model=attempt4, stats_dict=attempt4_stats)

    # Compute the score for each model
    attempt1_stats = score_calc(stats_dict=attempt1_stats)
    attempt2_stats = score_calc(stats_dict=attempt2_stats)
    attempt3_stats = score_calc(stats_dict=attempt3_stats)
    attempt4_stats = score_calc(stats_dict=attempt4_stats)

    print("\nScoring the models ... \n")
    print(f"attempt1_stats: {attempt1_stats}")
    print(f"attempt2_stats: {attempt2_stats}")
    print(f"attempt3_stats: {attempt3_stats}")
    print(f"attempt4_stats: {attempt4_stats}")

    # Combine the stats
    stats_list = [attempt1_stats, attempt2_stats, attempt3_stats, attempt4_stats]

    # Save the results
    print("\nSaving the results ... \n")
    with open("output/results.json", "w") as f:
        f.write(dumps(stats_list))

