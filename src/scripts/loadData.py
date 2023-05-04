from event.models import Registered
import csv


def run():
    with open('event/participant.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        Registered.objects.filter(Qrid="").delete()

        # for row in reader:
        #     print(row)

        #     student, _ = Registered.objects.get_or_create(Name=row[-1])

        #     film = Registered(Name=row[0],
        #                 Qrid=row[1])
        #     film.save()