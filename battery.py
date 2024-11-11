from datetime import datetime
from math import ceil

def time_pass(full: str, curr: str) -> int:
    # Время полного заряда
    full_charge_time = datetime.strptime(full.strip(), "%H:%M")
    # Текущее время
    current_time = datetime.strptime(curr.strip(), "%H:%M")

    # Вычисляем разницу во времени
    time_diff = current_time - full_charge_time

    # Calculate the difference in timedelta format
    diff_ = time_diff.seconds / 3600 + time_diff.days * 24
    return ceil(diff_)

def current_battery_mAh(*args) -> int|float:
    """
    :param capacity:   int|float
    :param do_hours:   int|float
    :param curr_hours: int|float
    """
    for e in args:
        if not isinstance(e, (int, float)):
            raise TypeError(
                '%s %s is not supported argument type' % (
                    e, type(e)
                )
            )
    capacity, do_hours, curr_hours = args
    return ceil(
        capacity * (
            curr_hours / do_hours
        )
    )

original_capacity = 5000 # mAh
# original_battery_life = 19 # hours
current_battery_life = time_pass(
    '7:00',
    '21:25'
) # hours
# current_battery_life = 28

current_capacity = current_battery_mAh(
    original_capacity,
    19,
    current_battery_life
)
current_capacity = ceil(
    current_capacity
)
print('current_battery_usage in work: %s' % current_battery_life)
print('in work 24/7 (%s): %s ~ %s mAh' % (
    19, current_capacity,
    (original_capacity - current_capacity)
))
current_capacity = current_battery_mAh(
    original_capacity,
    36,
    current_battery_life
)
current_capacity = ceil(
    current_capacity
)
print('in weekend (%s): %s ~ %s mAh' % (
    36, current_capacity,
    (original_capacity - current_capacity)
))

def gt() -> str:
    return datetime.now().strftime(
        '%H:%M'
    )

def per_hour(_d: dict[str, int]) -> float|int:
    # Вычисляем разницу в процентах
    from_, to_ = _d.keys()
    initial, final, = _d[from_], _d[to_]
    _used = initial - final
    
    # Рассчитываем процент, который уходит в час
    per_hour = _used / time_pass(
        from_, to_
    )
    return per_hour

_hour = per_hour({
    '7:00': 100,
    '21:17': 16
})
if str(_hour).endswith('.0'):
    _hour = str(_hour)
    _hour = _hour[:-2]
    _hour = int(_hour)
print('Процент в час: %s' % (
    round(_hour, 2)
) + '%')
