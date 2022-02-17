from models import User, Phone


def phone_saver(name: str, phones: str) -> bool:
    """ Gets name and phones and saves them as related objects in DB """
    if name and phones:
        user = User.add(name)
        for phone in phones.split("\n"):
            Phone.add(phone, user)
        return True
    return False


def show_all_for_name(name: str) -> list:
    """ Filters contacts by name from DB and returns a list of tuples for displaying contacts in search list"""
    # [("name", "123, 456, 789"), ("name", "123, 456, 789")]
    return [tuple([user.name, ", ".join([phone.phone for phone in user.phones]), user.id]) for user in User.find_by_name(name)]


def show_all_phones():
    """ Gets all contacts from DB and returns a list of tuples to display all contacts """
    return [tuple([user.name, ", ".join([phone.phone for phone in user.phones]), user.id]) for user in User.all()]


def delete_by_id(id_user):
    return User.delete_by_id(id_user)
