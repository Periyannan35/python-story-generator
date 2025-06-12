# story_generator.py
def generate_story(name, hobby, location, pet, emotion):
    story = f"""
{name} lived in a place called {location}.
{name} liked to do {hobby}. It was fun!
{name} had a pet. The pet's name was {pet}.
One day, {name} saw a magic door.
{name} held {pet} and felt {emotion}.
They walked into the door.

Wow! Something new was there.
It was the start of a big, fun story!
"""
    return story.strip()


def get_input(prompt_text):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("Oops! Please type something.")


def main():
    print("Welcome to the Tiny Story Maker!")

    while True:
        name = get_input("What is your name? ")
        hobby = get_input("What do you like to do? ")
        location = get_input("Tell a fun place name: ")
        pet = get_input("What is your pet's name? ")
        emotion = get_input("How do you feel? (happy, scared, etc.): ")

        story = generate_story(name, hobby, location, pet, emotion)

        print("\nHere is your story:\n")
        print(story)

        save = input("\nDo you want to save your story? (yes/no): ").lower()
        if save == "yes":
            filename = f"{name}_story.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(story)
            print(f"Yay! Story saved as '{filename}'")

        again = input("\nDo you want to make another story? (yes/no): ").lower()
        if again != "yes":
            print("Bye bye! Thanks for playing!")
            break


if __name__ == "__main__":
    main()
