from linkedlist import LinkedList


class Contact(LinkedList):
    def seed(self):
        for i in range(10):
            category = "cell"

            if i % 2 == 0:
                category = "telp"

            self.append({
                "name": f"Person {i+1}",
                "number": f"08321{i}",
                "category": category
            })

    def getAll(self) -> list:
        contacts = []
        temp = self.head
        iterate = 0
        while temp is not None:
            iterate += 1

            contacts.append([
                iterate,
                temp.data["name"],
                temp.data["number"],
                temp.data["category"]
            ])

            temp = temp.next_node

        return contacts
