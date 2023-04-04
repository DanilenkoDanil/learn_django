from django.core.management.base import BaseCommand
from steam.models import Account, Mail, Game
import random
import string


def generate_random_string():
    random_string = "" 
    str_len = random.randint(6,20)
    for _ in range(str_len):
        random_string += random.choice(string.ascii_letters)
    return random_string     
       
def generate_random_float():
    numbers = list("0123456789.")
    random_float = ""
    float_len = random.randint(3,5)
    for i in range(float_len):
        random_char = random.choice(numbers)
        if random_char == "." and i != 0 and i != float_len - 1:
            numbers = list("0123456789")
        elif random_char != ".":
            pass
        else:
            continue
        random_float += random_char
    return float(random_float)


class Command(BaseCommand):
    help = 'Старт'


    def handle(self, *args, **options):
        mails = list()
        games = list()
        for _ in range(5):
            login = generate_random_string()
            password = generate_random_string()
            mails.append(Mail.objects.create(login=login, password=password))
            name = generate_random_string()
            coast = generate_random_float()
            version = generate_random_string()
            games.append(Game.objects.create(name=name, coast=coast, version=version))

        for _ in range(5):
            games_for_acc = list()
            mail = random.choice(mails)
            login = mail.login
            password = mail.password
            games_for_acc.append(random.choice(games))
            acc = Account.objects.create(login=login, password=password, mail=mail)
            acc.game.set(games_for_acc)
