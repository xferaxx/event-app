class Comment:
    def __init__(self, Cevent_id, Cuser_id, comment):
        self._CEID = Cevent_id
        self._CUID = Cuser_id
        self._comment = comment

    @property
    def Cevent_id(self):
        return self._CEID

    @property
    def Cuser_id(self):
        return self._CUID

    @property
    def comment(self):
        return self._comment

    @Cevent_id.setter
    def Cevent_id(self, e_id):
        self._CEID = e_id

    @Cuser_id.setter
    def Cuser_id(self, u_id):
        self._CUID = u_id

    @comment.setter
    def comment(self, c):
        self._comment = c

    def __str__(self):
        return "Event ID = " + str(self.Cevent_id) + "  | User ID = " + str(self.Cuser_id) + "  | Comment = " + str(self.comment)






