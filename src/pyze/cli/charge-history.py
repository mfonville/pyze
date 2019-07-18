from .common import add_history_args, add_vehicle_args, get_vehicle
from datetime import datetime


help_text = 'Show charge history for your vehicle.'


def configure_parser(parser):
    add_vehicle_args(parser)
    add_history_args(parser)


def run(parsed_args):
    v = get_vehicle(parsed_args)

    now = datetime.utcnow()

    if parsed_args.from_date:
        from_date = min(parsed_args.from_date, now)
    else:
        from_date = now.replace(day=1)

    if parsed_args.to:
        to_date = min(parsed_args.to, now)
    else:
        to_date = now

    print(v.charge_history(from_date, to_date))
    print('NOTE: The format for this data isn\'t yet known, so raw output is shown above.')