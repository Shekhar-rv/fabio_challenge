# Fabio Technical Challenge

## This exercise aims to give you a very pared-down preview of what we’re trying to achieve at Fabrio with ‘Smart Check’ - comparing submitted CAD models to a target to decide if a model is ‘correct’, and then using the information gathered to provide feedback for ‘incorrect’ models.

### You are given five JSON files, each representing some data exported from a CAD software about a CAD model. Inside each JSON, you are given information about the volume and bounding box of the model itself, as well as a list of all of the faces that make up the model. Each face entry contains information about its area, centroid and bounding box min/max points. ‘target.json’ represents the target model, and ‘attemptx.json’ represent four submitted attempts to recreate the target. One of these attempts is ‘correct’, and three are not. Please complete the following programmatically:

1. Establish which attempted CAD model is ‘correct’
2. For the remaining three ‘incorrect’ models:
    - Quantify how incorrect they are (e.g. with a percentage)
    - Provide some feedback for the student to go with the above (can be any format)

### Part 1 has a correct answer, but Part 2 is your chance to show us your own ideas, expertise and display some creative thinking.


## Solution

### Part 1

To identify the correct model, I used the following approach:
  1. Filtered the attempted models by comparing their metrics with the target model based on:
     1. The bounding box of the models. 
     2. The volumes of the models.
     3. The number of faces of the models.
   
Based on the above, I identified the model with the highest number of matching metrics attempt4.json as the correct model.