class User:
    """Model a user"""
    def __init__(
        self, first_name, last_name,
        favorite_manga, favorite_anime
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_manga = favorite_manga
        self.favorite_anime = favorite_anime

    def describe_user(self):
        describer = f"You, {self.first_name.title()} {self.last_name.title()},"
        describer += f" likes {self.favorite_manga.title()} (manga) "
        describer += f"and {self.favorite_anime.title()} (anime).\n"

        print(describer)

    def greet_user(self):
        print(f"Hi {self.first_name.title()} {self.last_name.title()}!")

cs = User('computer', 'scientist', 'komi-san', 'hotaru no haka')
duende = User('tener', 'duende', 'angel densetsu', 'tonari no totoro')
runningman = User('running', 'man', 'one punch man', 'boku no hero academia')

cs.greet_user()
cs.describe_user()

duende.greet_user()
duende.describe_user()

runningman.greet_user()
runningman.describe_user()