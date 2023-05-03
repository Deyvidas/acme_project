from datetime import date


def get_day_to_brt(birth_date: date) -> int:
    """Возвращает количество дней до дня рождения."""
    today = date.today()
    brday = birth_date
    tod_y = today.year
    brt_m = brday.month
    brt_d = brday.day
    days_to_brtday = (date(tod_y, brt_m, brt_d) - today).days

    if days_to_brtday < 0:
        days_to_brtday = (date(tod_y+1, brt_m, brt_d) - today).days
    return days_to_brtday
