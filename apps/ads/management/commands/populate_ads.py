from random import randint

from django.core.management import BaseCommand
from faker import Faker

from ads.models import Advert

fake = Faker()


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("user", type=int)

    def handle(self, *args, **options):
        ads = []
        f = Faker()

        self.stdout.write(self.style.SUCCESS("Populating database..."))

        for i in range(options['user']):
            ads.append(Advert(
                name=f.name(),
                slug=f.name(),
                status=f.random_choices(elements=Advert.Status.choices, length=1)[0][0],
                price_type=f.random_choices(elements=Advert.PaymentType.choices, length=1)[0][0],
                price=randint(100, 1000),
                description=f.text(),
                view_count=randint(10, 100),
                is_new=f.boolean(),
                is_business=f.boolean(),
                contact=f.json(),
                auto_renewal=f.boolean(),
                owner_id=f.random_int(12, 18),
                category_id=randint(1, 109),
                city_id=randint(1, 181),
                extra_filed_info=f.json(),
            ))

        Advert.objects.bulk_create(ads)
        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated ads")
        )
