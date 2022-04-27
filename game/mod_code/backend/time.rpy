define wm_game_time = _wm_time.WintermuteTime()

label quit():
    $ wm_game_time.on_quit()
    return

init -150 python in _wm_time:
    from store import NoRollback, persistent, config
    from datetime import (
        datetime,
        date,
        timedelta
    )

    class WintermuteTime(NoRollback):
        game_start_date = date(2029, 7, 13)
        persistent_time_field = "current_time"

        def __init__(self):
            self.__last_update = None
            self.__current_time = None

        @property
        def persistent_time(self):
            value = getattr(persistent, self.persistent_time_field)

            if value is None:
                game_datetime = datetime.combine(self.game_start_date, datetime.now().time())
                setattr(persistent, self.persistent_time_field, game_datetime)
                return game_datetime

            return value

        @persistent_time.setter
        def persistent_time(self, value):
            setattr(persistent, self.persistent_time_field, value)

        def advance_time(self, delta):
            self.__update()
            self.__current_time += delta

        def now(self):
            self.__update()
            return self.__current_time

        def __update(self):
            if self.__current_time is None:
                self.__current_time = self.persistent_time

            now = datetime.now()

            if self.__last_update is not None:
                delta = now - self.__last_update
                self.__current_time += delta

            self.__last_update = now

        def on_quit(self):
            self.persistent_time = self.__current_time
