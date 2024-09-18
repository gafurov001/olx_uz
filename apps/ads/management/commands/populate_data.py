from hashlib import sha256
from random import randint

from django.core.management import BaseCommand
from faker import Faker

from users.models import User

fake = Faker()


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("user", type=int)

    def handle(self, *args, **options):
        users = []
        f = Faker()

        self.stdout.write(self.style.SUCCESS("Populating database..."))

        for i in range(options['user']):
            users.append(User(
                name=f.name(),
                phone_number=f"998{f.msisdn()[:9]}",
                social_network_account_type=f.random_choices(elements=User.SocialNetworkAccountType.choices, length=1)[0][0],
                email=f.email(),
                is_staff=f.boolean(),
                is_active=f.boolean(),
                is_online=f.boolean(),
                is_business=f.boolean(),
                is_superuser=f.boolean(),
                last_login=f.date(),
                password=f.password(),
                city_id=randint(1, 181),
            ))

        User.objects.bulk_create(users)
        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['user']} users")
        )
