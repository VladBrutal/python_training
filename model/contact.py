from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None,
                 nickname=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None,
                 email=None, email2=None, email3=None,
                 all_phones_from_home_page=None, all_email=None,
                 homepage=None, address2=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email = all_email

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname
                                   , self.home_phone, self.homepage, self.email)

    # self.home_phone, self.mobile_phone,
    # self.work_phone, self.secondary_phone

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
