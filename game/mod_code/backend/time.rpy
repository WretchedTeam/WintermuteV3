define wm_game_time = _wm_time.WintermuteTime()

init -150 python in _wm_time:
    from store import NoRollback, persistent, config
    from datetime import (
        datetime,
        date,
        timedelta
    )

    class WintermuteTime(NoRollback):
        game_start_date = date(2029, 7, 13)
        persistent_date_field = "current_date"

        def __init__(self):
            self.__last_update = None
            self.__current_time = None

        @property
        def persistent_date(self):
            value = getattr(persistent, self.persistent_date_field)

            if value is None:
                setattr(persistent, self.persistent_date_field, self.game_start_date)
                return self.game_start_date

            return value

        @persistent_date.setter
        def persistent_date(self, value):
            setattr(persistent, self.persistent_date_field, value)

        def now(self):
            return datetime.combine(self.today(), self.current_time())

        def current_time(self):
            return datetime.now().time()

        def today(self):
            return self.persistent_date
