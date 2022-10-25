from UserInterface import UserInterface
from MenuRepository import MenuRepository
from Order import Order
from Menu import Menu



def test_get_user_input(monkeypatch):
    #arrange 
    menu_repository = MenuRepository()
    user_interface = UserInterface(menu_repository)

    #act 
    monkeypatch.setattr('builtins.input', lambda _: "5 10")
    testes = user_interface.get_user_input()

    #assert
    assert testes.code == 5
    assert testes.quantity == 10


def test_get_total_price():
    #arrange
    menu_repository = MenuRepository()
    menu_repository.set_menu_item(Menu(1, "Hot dog", 4.00))
    user_interface = UserInterface(menu_repository)
    teste = Order(1, 8)

    #act
    total = user_interface.get_total_price(teste)

    #assert
    assert total == 32
    

    



    






