# story_generator.py

def generate_story(name, hobby, location, pet, emotion):
    story = f"""
    🌟 Once upon a time in {location}, lived a curious person named {name}.
    Every day, {name} enjoyed {hobby} while spending time with their pet {pet}.
    One evening, a mysterious portal appeared in front of them.
    Holding {pet} close, {name} stepped into the portal, feeling {emotion}.
    What they discovered changed their lives forever...
    🌈 The end of the beginning!
    """
    return story

print("✨ Welcome to the Story Generator ✨")
name = input("Enter your name: ")
hobby = input("Enter your favorite hobby: ")
location = input("Enter a magical location: ")
pet = input("Enter your pet's name: ")
emotion = input("Enter an emotion (e.g., excited, scared): ")


print("\n📜 Your Generated Story:")
print(generate_story(name, hobby, location, pet, emotion))
