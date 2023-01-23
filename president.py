from datetime import date


class President():
    def __init__(self, index):
        self._get_data(index)

    @staticmethod
    def _mkdate(raw_date):
        if raw_date != "NONE":
            raw_year, raw_month, raw_day = raw_date.split('-')
            d = date(int(raw_year), int(raw_month), int(raw_day))
        else:
            d = None

        return d

    def _get_data(self, index):
        # Note: replace the following code to use the DB API to get
        # data from the presidents.db database.
        # You will probably need to access it as "DATA/presidents.db"
        # You will no longer need the _mkdate() method
        with open("DATA/presidents.txt") as pfile:
            for line in pfile:
                flds = line.split(":")
                if int(flds[0]) == int(index):
                    self._lname = flds[1]

                    self._fname = flds[2]

                    self._bdate = self._mkdate(flds[3])
                    self._ddate = self._mkdate(flds[4])

                    self._bplace = flds[5]
                    self._bstate = flds[6]

                    self._ts_date = self._mkdate(flds[7])
                    self._te_date = self._mkdate(flds[8])

                    self._party = flds[9]

                    break
            else:
                raise ValueError("Invalid term number")

    @property
    def last_name(self):
        return self._lname

    @property
    def first_name(self):
        return self._fname

    @property
    def birth_date(self):
        return self._bdate

    @property
    def death_date(self):
        return self._ddate

    @property
    def birth_place(self):
        return self._bplace

    @property
    def birth_state(self):
        return self._bstate

    @property
    def term_start_date(self):
        return self._ts_date

    @property
    def term_end_date(self):
        return self._te_date

    @property
    def party(self):
        return self._party
