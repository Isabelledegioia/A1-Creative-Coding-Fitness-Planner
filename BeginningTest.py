
#Ensure that the exercises are going to be randomly selected within the criteria
import random



#Ask user a question and they type in their answer. (choosing pilates class type)
Type = input("What class style are you planning today?: ")

#collect the three main variables for the plan
#(.lower() so it can be written in any format with captials
#.split(",") separates the user's answer into a list.
level = input("Choose your class level (beginner, intermediate, advanced): ").lower()
muscles = input("Choose up to 3 target muscles (glutes, abs, quads), separated by commas: ").lower().split(",")
prop = input("Which prop would you like? (ball, band, block): ").lower()

#List comprehension: removes the unnessesary spaces from the muscle groups so no confusion
muscles = [muscle.strip() for muscle in muscles]



# conditional statements for the class level
if level == "beginner":
    print("Generating your beginner Pilates class...")

elif level == "intermediate":
    print("Generating your intermediate Pilates class...")

elif level == "advanced":
    print("Generating your advanced Pilates class...")

else:
    print("level not valid. Please choose beginner, intermediate or advanced.")




    
#exercise Dictionary. nested dictionary (dictionary contains other dictionaries and lists.)
exercises = {
    "beginner": {
        "glutes": [
            "Glute bridges",
            "Sidelying Clamshells",
            "Donkey kicks"
        ],
        "abs": [
            "Dead bugs",
            "Toe taps",
            "Basic ab curls"
        ],
        "quads": [
            "Narrow squats",
            "Reverse 9090 lunges",
            "Kneeling hinge"
        ]
    },

    "intermediate": {
        "glutes": [
            "Single leg glute bridges",
            "Fire hydrants",
            "Glute bridge marches"
        ],
        "abs": [
            "Plank shoulder taps",
            "Bicycle crunches",
            "Side plank hip lifts"
        ],
        "quads": [
            "Curtsy lunges",
            "Pulse squats",
            "Lateral lunges"
        ]
    },

    "advanced": {
        "glutes": [
            "Single leg bridge pulses",
            "Standing glute kickbacks",
            "Single leg hip thrusts"
        ],
        "abs": [
            "Teaser",
            "Plank to pike",
            "Double leg lowers"
        ],
        "quads": [
            "Jump squats",
            "Plyo lunges",
            "Alternating narrow squat to lunge"
        ]
    }
}
# exercise bank for props: organised by level, muscle group and equipment
# Second dictonary so python can combine exercises from both banks: not every exercise needs to use a prop.

prop_exercises = {
    "beginner": {
        "glutes": {
            "ball": ["Ball between knees glute bridges"],
            "band": ["Banded sidelying clamshells"],
            "block": ["block between knees glute bridges"]
        },
        "abs": {
            "ball": ["Ball supported ab curls"],
            "band": ["Banded dead bugs"],
            "block": ["Block between knees toe taps"]
        },
        "quads": {
            "ball": ["Narrow squats with ball"],
            "band": ["Banded narrow to wide alternating squats"],
            "block": ["Block squeeze narrow squats"]
        }
    },

    "intermediate": {
        "glutes": {
            "ball": ["Single leg bridges with ball"],
            "band": ["Banded fire hydrants"],
            "block": ["Glute bridges with block squeeze"]
        },
        "abs": {
            "ball": ["Ab curls with ball"],
            "band": ["Banded bicycle crunches"],
            "block": ["Dead bugs with block"]
        },
        "quads": {
            "ball": ["Narrow squat pulses with ball"],
            "band": ["Banded squat pulses"],
            "block": ["Narrow squats with block squeeze"]
        }
    },

    "advanced": {
        "glutes": {
            "ball": ["Single leg glute bridges with ball"],
            "band": ["Banded glute bridge pulses"],
            "block": ["Single leg bridge with block squeeze"]
        },
        "abs": {
            "ball": ["Teaser with ball"],
            "band": ["Banded double leg lowers"],
            "block": ["Teaser with block"]
        },
        "quads": {
            "ball": ["9090 lunge with ball under heel"],
            "band": ["Banded jump squats"],
            "block": ["Narrow squat pulses with block under heels"]
        }
    }
}

# function to generate a pilates class plan
def generate_class_plan():

    # check the user has entered valid class options
    if level in exercises and 1 <= len(muscles) <= 3 and prop in ["ball", "band", "block"]:

        # Display the user's selected class information
        print("\n*** MAT PILATES CLASS PLAN ***")

        print("Class Style:", Type)
        print("Class Level:", level.capitalize())
        print("Target Muscles:", ", ".join(muscles))
        print("Selected Prop:", prop.capitalize())

        print("\nYour Exercises:")

        # loop through each muscle group selected by the user
        for muscle in muscles:

            # check that the muscle group exists in the dictionary
            if muscle in exercises[level]:

                # Randomly select 2 regular exercises
                regular_exercises = random.sample(
                    exercises[level][muscle], 2
                )

                # randomly select 1 exercise using chosen prop
                equipment_exercises = random.sample(
                    prop_exercises[level][muscle][prop], 1
                )

                # combine both exercise lists
                selected_exercises = regular_exercises + equipment_exercises

                # shuffle the order of exercises
                random.shuffle(selected_exercises)

                print("\n" + muscle.capitalize() + ":")

                for exercise in selected_exercises:
                    print("-", exercise)

            else:
                print("Sorry!", muscle, "is not a valid muscle group.")

    else:
        print("Please choose a valid level, 1-3 muscles and a valid prop.")

# call the function to generate the class plan
generate_class_plan()

