from guest_book import *

guest_book = GuestBook()

kunitsa = Guest(name="Kunitsa Devitsa", room=3)
york = Guest(name="York", room=4)

guest_book.guest_in(kunitsa)
guest_book.guest_in(york)

# ...

guest_book.guest_out(kunitsa)
guest_book.guest_out(york)

guest_book.write_book()
guest_book.list_book()
# guest_book.remove_book_file()
