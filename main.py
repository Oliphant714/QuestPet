# from Personality import Dragon
# from Personality import UserState
# from Personality import Task

import personality2.PetRenderer as PetRenderer
from personality2.PetRenderer import PetRenderer
import personality2.PetAnimation as PetAnimation
from personality2.PetAnimation import PetAnimation

def main():

    renderer = PetRenderer()
    animation = PetAnimation(renderer)
    renderer.run()

if __name__ == "__main__":
    main()