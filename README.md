# Fabio Technical Challenge

## This exercise aims to give you a very pared-down preview of what we’re trying to achieve at Fabrio with ‘Smart Check’ - comparing submitted CAD models to a target to decide if a model is ‘correct’, and then using the information gathered to provide feedback for ‘incorrect’ models.

### You are given five JSON files, each representing some data exported from a CAD software about a CAD model. Inside each JSON, you are given information about the volume and bounding box of the model itself, as well as a list of all of the faces that make up the model. Each face entry contains information about its area, centroid and bounding box min/max points. ‘target.json’ represents the target model, and ‘attemptx.json’ represent four submitted attempts to recreate the target. One of these attempts is ‘correct’, and three are not. Please complete the following programmatically:

1. Establish which attempted CAD model is ‘correct’
2. For the remaining three ‘incorrect’ models:
    1. Quantify how incorrect they are (e.g. with a percentage)
    2. Provide some feedback for the student to go with the above (can be any format)

### Part 1 has a correct answer, but Part 2 is your chance to show us your own ideas, expertise and display some creative thinking.


## Solution

### Part 1

To identify the correct model, I used the following approach:
  1. Filtered the attempted models by comparing their metrics with the target model based on:
     1. The bounding box of the models. 
     2. The volumes of the models.
     3. The number of faces of the models.
  2. The area of the faces of the models.

I identified the **attempt4 model** as the correct model based on the following (rounding all values to 4 decimal places):
  1. The bounding box of the model is the same as the target model.
  2. The volume of the model is the same as the target model.
  3. The number of faces of the model is the same as the target model.
  4. The area of the faces of the model is the same as the target model.

### Part 2

To quantify how incorrect the incorrect models are, I used the following approach:
  1. I chose to use the `volume` and `area` of the faces of the models as the metrics to quantify how incorrect the models are.
  2. The models are overall scored on a scale of 10, with 0 being the most incorrect and 10 being the most correct.
  3. The models are scored based on the following:
     1. The volume of the model is compared to the target model. The closer the volume of the model is to the target model, the higher the score.
     2. The area of the faces of the model is compared to the target model. The closer the area of the faces of the model is to the target model, the higher the score.

## Feedback

### Attempt 1
This model had an overall score of 9.8/10 as the model is very close to the target model. However, this model has 205 faces compared to the target model which has 34 faces but 33 of the faces area matches with that of the target model.

### Attempt 2
This model had an overall score of 7.3/10. This model has 50 faces compared to the target model which has 34 faces but only 16 of the faces area matches with that of the target model. The volume of the model is slightly higher than the target model.

### Attempt 3
This model had an overall score of 6.8/10. This model has 16 faces compared to the target model which has 34 faces but only 14 of the faces area matches with that of the target model. The volume of the model is significantly lower than the target model.

### Attempt 4
This model had an overall score of 10/10. This model has 34 faces compared to the target model which has 34 faces and all of the faces area matches with that of the target model. The volume of the model is the same as the target model.

## The stats calculated for each model are saved in the output directory as a json file.

## How to run the code

### Prerequisites
   Python 3.7 or higher

### Steps
    1. Clone the repository.
    2. Navigate to the root directory of the repository.
    3. Run the following command to run the code:
        ```
        make run-python-script
        ```
    4. The output will be saved in the output directory.