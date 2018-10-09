class JSONReadWritter:
    @staticmethod
    def read_file(file_path: str):
        with open(file_path) as file:
            return file.read()

    @staticmethod
    def write_file(file_path: str, data: str, mode: str = 'w'):
        with open(file_path, mode=mode) as file:
            file.write(data)


class Guest:
    def __init__(self, name: str, room: int):
        import datetime
        import uuid
        self.json_data = dict()
        self.json_data.update(
            {
                "index": uuid.uuid4().hex,
                "name": name,
                "room": room,
                "data_in": "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()),
                "date_out": ""
             })

    def __str__(self):
        import json
        return json.dumps(self.json_data)


class GuestBook:
    guests: list
    book_file: str

    def __init__(self):
        self.guests = list()
        self.book_file = "./book.json"

    def guest_in(self, guest: Guest):
        self.guests.append(guest)

    def guest_out(self, guest: Guest):
        import datetime
        try:
            index = self.guests.index(guest)
            self.guests.remove(guest)
            guest.json_data.update({"date_out": "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())})
            self.guests.insert(index, guest)
        except:
            print("No such guest with index: " + guest.json_data.get("index"))

    def write_book(self):
        import json
        json_data = list()
        for guest in self.guests:
            json_data.append(str(guest))
        json_data = {"Guest book": json_data}
        JSONReadWritter.write_file(self.book_file, json.dumps(json_data, ensure_ascii=False, indent=4))

    def list_book(self):
        import json
        json_data = JSONReadWritter.read_file(self.book_file)
        count = 1
        for guest in dict(json.loads(json_data)).get("Guest book"):
            print("Record [" + str(count) + "]")
            count += 1
            guest = json.loads(guest)
            for key in guest:
                print(key + ": " + str(dict(guest).get(key)))
            print()

    def remove_book_file(self):
        import os
        os.remove(self.book_file)

    def set_book_file(self, path):
        self.book_file = path


if __name__ == "__main__":
    print("Demo is activated")

    guest_book = GuestBook()

    kunitsa = Guest(name="Kunitsa Devitsa", room=1)
    york = Guest(name="York", room=2)

    guest_book.guest_in(kunitsa)
    guest_book.guest_in(york)

    # ...

    guest_book.guest_out(kunitsa)
    guest_book.guest_out(york)

    guest_book.write_book()
    guest_book.list_book()
    # guest_book.remove_book_file()
