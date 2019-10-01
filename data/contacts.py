from model.contact import Contact

testdata = [
                     Contact(firstname="", middlename="", lastname="", nickname="", company=""
                             , address="", home_phone="", mobile_phone="",
                             work_phone="", secondary_phone="", email="", homepage="", address2="")] + [
                     Contact(firstname="fname1", middlename="mname1", lastname="lname1", nickname="nname1",
                             company="company1", address="address1", home_phone="123456", mobile_phone="234567",
                             work_phone="345678", secondary_phone="456789", email="email1@email.com",
                             homepage="homepage1.com", address2="address2_1"),
                     Contact(firstname="fname2", middlename="mname2", lastname="lname2", nickname="nname2",
                             company="company2", address="address2", home_phone="1234562", mobile_phone="2345672",
                             work_phone="3456782", secondary_phone="4567892", email="email2@email.com",
                             homepage="homepage2.com", address2="address2_2")
                    ]