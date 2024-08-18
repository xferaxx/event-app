class Events:

    def __init__(self, event_id, type, description, address, dangerous_level, user_id, approves=0):
        self._event_id = event_id
        self._type = type
        self._description = description
        self._address = address
        self._dangerous_level = dangerous_level
        self._user_id = user_id
        self._approves = approves

    @property
    def event_id(self):
        return self._event_id

    @property
    def type(self):
        return self._type

    @property
    def description(self):
        return self._description

    @property
    def address(self):
        return self._address

    @property
    def dangerous_level(self):
        return self._dangerous_level

    @property
    def approves(self):
        return self._approves

    @event_id.setter
    def event_id(self, e_id):
        self._event_id = e_id

    @type.setter
    def type(self, typ):
        self._type = typ

    @property
    def user_id(self):
        return self._user_id

    @description.setter
    def description(self, desc):
        self._description = desc

    @address.setter
    def address(self, adrs):
        self._address = adrs

    @dangerous_level.setter
    def dangerous_level(self, dang_lvl):
        self._dangerous_level = dang_lvl

    @approves.setter
    def approves(self, apr):
        self._approves = apr

    @user_id.setter
    def user_id(self, u_id):
        self._user_id = u_id

    def __eq__(self, other):
        return self._event_id == other.event_id

    def __str__(self):
        return "ID = " + str(
            self.event_id) + "  | Type = " + self.type + "  | Description = " + self.description + \
               "  | Address = " + self.address + " | Dangerous level = " + self.dangerous_level + " | Approves = " \
               + str(self.approves)
