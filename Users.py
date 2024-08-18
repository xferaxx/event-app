class User:

    def __init__(self, user_id, user_name, email, credit=0):
        self._user_id = user_id
        self._user_name = user_name
        self._email = email
        self._credit = credit

    @property
    def user_id(self):
        return self._user_id

    @property
    def user_name(self):
        return self._user_name

    @property
    def email(self):
        return self._email

    @property
    def credit(self):
        return self._credit

    @user_id.setter
    def user_id(self, u_id):
        self._user_id = u_id

    @user_name.setter
    def user_name(self, name):
        self._user_name = name

    @email.setter
    def email(self, mail):
        self._email = mail

    @credit.setter
    def credit(self, crd):
        self._credit = crd

    def __eq__(self, other):
        return self._user_id == other.user_id

    def __str__(self):
        return "ID = " + str(self.user_id) + \
               "  | Full Name = " + self.user_name + "  | Email = " + self.email + "  | Credit = " + str(self.credit)
