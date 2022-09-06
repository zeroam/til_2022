from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from polls.models import Question as Poll


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args: Any, **options: Any) -> str | None:
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError(f'Poll {poll_id} does not exist')

            poll.opened = False
            poll.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully closed poll {poll_id}'))
