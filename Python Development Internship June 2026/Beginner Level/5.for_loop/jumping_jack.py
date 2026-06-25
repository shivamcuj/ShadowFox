def perform_jumping_jack(target):
    print("Perform 10 Jumping Jack")
    target = target - 10
    return target

target = 100
while target > 0:
    target = perform_jumping_jack(target)
    tired = input("Are you tired? ").lower()
    if tired == 'y' or tired == 'yes':
        skip = input("Do you want to skip the remaining sets? ").lower()
        if skip == 'y' or skip == 'yes':
            print(f"You completed a total of {100-target} jumping jacks.")
            break

        elif skip == 'n' or skip == 'no':
            print(f"{target} jumping jacks left")
            continue

    elif tired == 'n' or tired == 'no':
        print(f"{target} jumping jacks left")
        continue

if target == 0:
    print("Congratulations! You completed the workout")