#Ensure that the exercises are going to be randomly selected within the criteria
# import brings in the random library so Python can make random choices for the plan
import random
 
 
 
#Ask user a question and they type in their answer. (choosing pilates class type only option)
# input() waits for the user to type answer & saves what they typed
# Type ust used to display the class style at the top of the plan so like pilates
Type = input("What class style are you planning today?: ")
 
#collect the three main variables for the plan
#(.lower() so it can be written in any format with captials without error
#.split(",") seperate user's answer into a list 
#.lower() stops capitals and non capitals in answers being treated as different things
# level and prop are single answers so they stay as text. muscles list because user can pick multiple
level = input("Choose your class level (beginner, intermediate, advanced): ").lower()
muscles = input("Choose up to 3 target muscles (glutes, abs, quads, arms, back), separated by commas: ").lower().split(",")
prop = input("Which prop would you like? (ball, band, block): ").lower()
 
#list comprehension remove spaces from the muscle groups so no confusion when user types
# after split() the second muscle still has a space in front- .strip() fixes it
# it goes through each muscle in the list then saves the clean list back into muscles
muscles = [muscle.strip() for muscle in muscles]
 
 
 
# these variables control how long plan is
# regular_count means how many exercises without a prop are picked for each muscle group
# prop_count means how many prop exercises are picked for each muscle
# They can't be bigger than the shortest list otherwise random.sample will give an error.
# shortest regular list has 4 exercises and shortest prop list has 2 so 4 & 2 max
# 6 exercises per muscle group in total
regular_count = 4
prop_count = 2
 
# dictionary links each level to a rep range the plan so higher level to higher rep range
reps = {
    "beginner": "8-10 reps",
    "intermediate": "12-15 reps",
    "advanced": "15-20 reps"
}
 
 
 
# conditional statements for the class level depending on whats picked
# == checks if the level matches exactly python checks each one in order until one is true?
if level == "beginner":
    print("Generating your beginner Pilates class...")
 
elif level == "intermediate":
    print("Generating your intermediate Pilates class...")
 
elif level == "advanced":
    print("Generating your advanced Pilates class...")
 
# else runs if none of the levels above match like typos
# *ALSO FIX -checks the level so an invalid level shows two error messages????
else:
    print("level not valid. Please choose beginner, intermediate or advanced.")
 
 
 
 
    
#exercise Dictionary. nested dictionary (dictionary contains other dictionaries and lists)
# layers- level, muscle group, list of exercises
# these are the regular exercises that don't need a prop
 
exercises = {
    "beginner": {
        "glutes": [
            "Glute bridges",
            "Sidelying Clamshells",
            "Donkey kicks",
            "Sidelying leg lifts",
            "Prone leg lifts"
        ],
        "abs": [
            "Dead bugs",
            "Toe taps",
            "Basic ab curls",
            "Pelvic tilts",
            "Kneeling plank hold"
        ],
        "quads": [
            "Narrow squats",
            "Reverse 9090 lunges",
            "Kneeling hinge",
            "Slow tempo squats"
        ],
        "arms": [
            "Arm circles",
            "Barre push ups",
            "Kneeling push ups",
            "Tricep dips",
            "Tabletop shoulder taps"
        ],
        "back": [
            "Superman holds",
            "Bird dog",
            "Cat cow",
            "Back extensions with T arms",
            "Back extensions with W arms"
        ]
    },
 
    "intermediate": {
        "glutes": [
            "Single leg glute bridges",
            "Fire hydrants",
            "Glute bridge marches",
            "Sidelying leg circles",
            "Donkey kick pulses"
        ],
        "abs": [
            "Plank shoulder taps",
            "Bicycle crunches",
            "Side plank hip lifts",
            "Single leg stretch",
            "Criss cross"
        ],
        "quads": [
            "Curtsy lunges",
            "Pulse squats",
            "Lateral lunges",
            "Split squats",
            "Squat holds with heel raise"
        ],
        "arms": [
            "Push ups",
            "Tricep push ups",
            "Plank to pike",
            "Tricep dips with leg lift",
            "Commandos"
        ],
        "back": [
            "Swimming",
            "Superman pulses",
            "Bird dog crunches",
            "Back extension hold",
            "Swan prep"
        ]
    },
 
    "advanced": {
        "glutes": [
            "Single leg bridge pulses",
            "Standing glute kickbacks",
            "Single leg hip thrusts",
            "Sidelying leg lift series",
            "Single leg deadlifts"
        ],
        "abs": [
            "Teaser",
            "Plank to pike",
            "Double leg lowers",
            "Roll ups",
            "The hundred"
        ],
        "quads": [
            "Jump squats",
            "Plyo lunges",
            "Alternating narrow squat to lunge",
            "Bulgarian split squats",
            "Lunge pulses"
        ],
        "arms": [
            "Diamond push ups",
            "Pike push ups",
            "Plank walkouts",
            "Archer push ups",
            "Plank shoulder tap push ups"
        ],
        "back": [
            "Swan",
            "Single leg kicks",
            "Double leg kicks",
            "Swimming with pulses",
            "Superman with arm sweeps"
        ]
    }
}
# exercise bank for props: organised by level, muscle group & prop
# Second dictonary to be able to combine exercises from both banks- not every exercise needs to use a prop idk
# layers: level- muscle group- prop- list of exercises
#possibly try to condense these if time
 
prop_exercises = {
    "beginner": {
        "glutes": {
            "ball": ["Ball between knees glute bridges", "Ball squeeze bridge holds", "Ball supported sidelying leg lifts"],
            "band": ["Banded sidelying clamshells", "Banded glute bridges", "Banded donkey kicks"],
            "block": ["Block between knees glute bridges", "Elevated glute bridges with feet on block", "Sidelying leg lifts with block between ankles"]
        },
        "abs": {
            "ball": ["Ball supported ab curls", "Ball squeeze dead bugs", "Ball overhead reach curls"],
            "band": ["Banded dead bugs", "Banded toe taps", "Banded ab curls"],
            "block": ["Block between knees toe taps", "Block squeeze dead bugs", "Block held ab curls"]
        },
        "quads": {
            "ball": ["Narrow squats with ball", "Ball squeeze squat holds"],
            "band": ["Banded narrow to wide alternating squats", "Banded squat holds"],
            "block": ["Block squeeze narrow squats", "Block between knees squat holds"]
        },
        "arms": {
            "ball": ["Ball press chest squeezes", "Barre push ups with ball", "Ball overhead reach"],
            "band": ["Banded bicep curls", "Banded tricep extensions", "Banded chest openers"],
            "block": ["Block squeeze chest press", "Block overhead presses", "Kneeling push ups on blocks"]
        },
        "back": {
            "ball": ["Back extensions over ball", "Ball bird dog", "Ball supported back extensions with T arms"],
            "band": ["Banded rows", "Banded pull aparts", "Banded back extensions with T arms"],
            "block": ["Block bird dog", "Block squeeze superman holds", "Block held back extensions with T arms"]
        }
    },
 
    "intermediate": {
        "glutes": {
            "ball": ["Single leg bridges with ball", "Ball squeeze bridge marches", "Ball between knees bridge pulses"],
            "band": ["Banded fire hydrants", "Banded bridge marches", "Banded sidelying leg circles"],
            "block": ["Glute bridges with block squeeze", "Block squeeze bridge marches", "Block between knees bridge pulses"]
        },
        "abs": {
            "ball": ["Ab curls with ball", "Ball single leg stretch", "Ball criss cross"],
            "band": ["Banded bicycle crunches", "Banded single leg stretch", "Banded criss cross"],
            "block": ["Dead bugs with block", "Block single leg stretch", "Block held bicycle crunches"]
        },
        "quads": {
            "ball": ["Narrow squat pulses with ball", "Split squats with ball"],
            "band": ["Banded squat pulses", "Banded lateral lunges", "Banded split squats"],
            "block": ["Narrow squats with block squeeze", "Block squeeze squat pulses"]
        },
        "arms": {
            "ball": ["Incline push ups on ball", "Ball tricep dips", "Ball plank holds"],
            "band": ["Banded push ups", "Banded tricep kickbacks", "Banded bicep curls with reach"],
            "block": ["Push ups on blocks", "Block tricep dips", "Block press plank taps"]
        },
        "back": {
            "ball": ["Prone swimming over ball", "Ball superman pulses", "Ball bird dog crunches"],
            "band": ["Banded swimming", "Banded rows with reach", "Banded pull aparts"],
            "block": ["Block superman pulses", "Block bird dog crunches", "Block held swimming"]
        }
    },
 
    "advanced": {
        "glutes": {
            "ball": ["Single leg glute bridges with ball", "Ball squeeze single leg hip thrusts", "Ball squeeze bridge pulses"],
            "band": ["Banded glute bridge pulses", "Banded standing kickbacks", "Banded single leg hip thrusts"],
            "block": ["Single leg bridge with block squeeze", "Single leg elevated bridges with foot on block", "Single leg deadlifts with block"]
        },
        "abs": {
            "ball": ["Teaser with ball", "Ball roll ups", "Ball double leg lowers"],
            "band": ["Banded double leg lowers", "Banded roll ups", "Banded teaser"],
            "block": ["Teaser with block", "Block held roll ups", "Block squeeze double leg lowers"]
        },
        "quads": {
            "ball": ["9090 lunge with ball under heel", "Bulgarian split squats with ball", "Ball squeeze jump squats"],
            "band": ["Banded jump squats", "Banded lunge pulses", "Banded Bulgarian split squats"],
            "block": ["Narrow squat pulses with block under heels", "Block squeeze jump squats", "Block squeeze lunge pulses"]
        },
        "arms": {
            "ball": ["Push ups with feet on ball", "Ball diamond push ups", "Ball pike push ups"],
            "band": ["Banded diamond push ups", "Banded pike push ups"],
            "block": ["Block diamond push ups", "Deficit push ups on blocks", "Block plank walkouts"]
        },
        "back": {
            "ball": ["Swan on ball", "Ball single leg kicks", "Ball swimming pulses"],
            "band": ["Banded swan", "Banded double leg kicks", "Banded superman with sweeps"],
            "block": ["Block swan", "Block single leg kicks", "Block held double leg kicks"]
        }
    }
}
 
#function to generate pilates class plan
# def creates the function the code inside only runs when from the bottom
def generate_class_plan():
 
# check the user has entered valid class options for all categories
# all 3 checks must be true valid level. 1-3 muscles (len() counts the list). valid prop
# "and" means if any check is false plan won't generate and it goes to the else at the bottom
    if level in exercises and 1 <= len(muscles) <= 3 and prop in ["ball", "band", "block"]:
 
# display the user's selected class information
# \n adds an empty line before the heading so the plan stands out and looks better
        print("\n*** MAT PILATES CLASS PLAN ***")
 
# .title() adds capitals back in for display, inputs were changed to lowercase
# ", ".join() turns the muscles list into text with commas
        print("Class Style:", Type)
        print("Class Level:", level.title())
        print("Target Muscles:", ", ".join(muscles))
        print("Selected Prop:", prop.title())
 
# exercise_number numbers every exercise in the plan, starting at 1
# it's outside the loop so numbering goes across muscle groups instead of restarting
        exercise_number = 1
 
# reps[level] looks up the rep range for the chosen level
        print("\nEXERCISES (" + reps[level] + " each):")
 
# loop through each muscle group selected by the user
# everything under this runs once for each muscle
        for muscle in muscles:
 
# check that the muscle group exists when it runs
            if muscle in exercises[level]:
 
# Randomly select regular exercises 
# random.sample picks different exercises so none are repeated
# exercises[level][muscle] finds the right list the regular_count says how many to pick
                regular_exercises = random.sample(
                    exercises[level][muscle], regular_count
                )
 
# randomly select exercises using chosen prop 
# same as above but finds the list for the chosen prop
                equipment_exercises = random.sample(
                    prop_exercises[level][muscle][prop], prop_count
                )
 
 # combine both exercise lists
 # + joins the two lists into one list of 6 exercises
                selected_exercises = regular_exercises + equipment_exercises
 
# shuffle the order of exercises
# so the prop exercises aren't always stuck at the end
                random.shuffle(selected_exercises)
 
# prints the muscle group as a heading with a capital no matter what
                print("\n" + muscle.title() + ":")
 
# prints the exercise number followed by the exercise name
# then adds 1 to exercise_number so the next exercise gets the next number
                for exercise in selected_exercises:
                    print(exercise_number, exercise)
                    exercise_number = exercise_number + 1
 
# runs if a muscle isn't in the dictionarylike a typo
# the other muscles still print& wrong one is skipped
            else:
                print("Sorry!", muscle, "is not a valid muscle group.")
 
# runs if any of the 3 checks at the top of the function failed
    else:
        print("Please choose a valid level, 1-3 muscles and a valid prop.")
 
# generate the class plan
# this calls the function so all the code inside it will runs
generate_class_plan()
 
