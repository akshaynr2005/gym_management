
from mysql import connector
from datetime import datetime


class gymMember:

    def get_connection(self):
        try:
            self.connect = connector.connect(
                host='localhost',
                user='root',
                db='gym_db',
                password='akshaynr_@2005'
            )
            return self.connect

        except Exception as e:
            print(e)
            return None

    # GET OBJECT
    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM member WHERE id=%s"
            values = (id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)
            return None


class GymMember(DbConnect):

    def __init__(self):
        try:
            self.connection = super().get_connection()

            if self.connection:
                self.cursor = self.connection.cursor()
                print("Successfully Connected")

        except Exception as e:
            print(e)

    # INSERT
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """INSERT INTO member
            (name, place, plan, mobile, fee, joining_date)
            VALUES (%s, %s, %s, %s, %s, %s)"""

            values = (
                kwargs['name'],
                kwargs['place'],
                kwargs['plan'],
                kwargs['mobile'],
                kwargs['fee'],
                kwargs['joining_date']
            )

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Member added successfully!")

        except Exception as e:
            print(e)

    # DISPLAY ALL RECORDS
    def get(self):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM member"

            self.cursor.execute(query)
            records = self.cursor.fetchall()

            return records

        except Exception as e:
            print(e)

    # RETRIEVE SINGLE RECORD
    def retreive(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is not None:
                print(record)

            else:
                print("No members found!")

        except Exception as e:
            print(e)

    # DELETE
    def delete(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is not None:

                self.cursor = self.connection.cursor()

                query = "DELETE FROM member WHERE id=%s"

                self.cursor.execute(query, (id,))
                self.connection.commit()

                print("Member deleted successfully!")

            else:
                print("No members found!")

        except Exception as e:
            print(e)

    # UPDATE
    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record is not None:

                self.cursor = self.connection.cursor()

                allowed_columns = {
                    'name', 'place', 'plan',
                    'mobile', 'fee', 'joining_date'
                }

                if not kwargs:
                    print("No values provided for update!")
                    return

                if not set(kwargs).issubset(allowed_columns):
                    print("Invalid column name!")
                    return

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += f"{k}=%s,"

                placeholder = placeholder.rstrip(",")

                query = f"UPDATE member SET {placeholder} WHERE id=%s"

                values = list(kwargs.values())
                values.append(id)

                self.cursor.execute(query, values)
                self.connection.commit()

                print("Member updated successfully!")

            else:
                print("No members found!")

        except Exception as e:
            print(e)


# OBJECT CREATION

g1 = GymMember()


# INSERT
g1.post(
    name='Sreerag',
    place='Kochi',
    plan='3 months',
    mobile=9363926484,
    fee=2000,
    joining_date=datetime.now().strftime('%Y-%m-%d')
 )


# DISPLAY ALL
records = g1.get()
print(records)


# RETRIEVE
# g1.retreive(id=1)


# DELETE
# g1.delete(id=2)


# UPDATE
# g1.put(id=1, place='Kochi', fee=2500)


# CLOSE CONNECTION
if g1.connection and g1.connection.is_connected():
    g1.cursor.close()
    g1.connection.close()

