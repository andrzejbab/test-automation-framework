from enum import Enum


class TypeEnum(str, Enum):
    FITNESS_STUDIO = "fitness_studio"
    FOOTBALL_PITCH = "football_pitch"
    GYM = "gym"
    OTHER = "other"
    SPORTS_HALL = "sports_hall"
    SWIMMING_POOL = "swimming_pool"
    TENNIS_COURT = "tennis_court"

    def __str__(self) -> str:
        return str(self.value)
