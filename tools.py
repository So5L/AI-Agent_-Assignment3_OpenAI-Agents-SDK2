from agents import function_tool, RunContextWrapper
from models import RestaurantContext


@function_tool
def place_order(
    wrapper: RunContextWrapper[RestaurantContext],
    item_name: str,
    quantity: int,
    special_request: str = ""
) -> str:
    return (
        f"Order placed for {wrapper.context.name}: "
        f"{quantity} x {item_name}. "
        f"Special request: {special_request or 'None'}."
    )


@function_tool
def modify_order(
    wrapper: RunContextWrapper[RestaurantContext],
    order_id: str,
    updated_item: str
) -> str:
    return f"Order {order_id} has been updated to: {updated_item}."


@function_tool
def cancel_order(
    wrapper: RunContextWrapper[RestaurantContext],
    order_id: str
) -> str:
    return f"Order {order_id} has been canceled."


@function_tool
def check_order_status(
    wrapper: RunContextWrapper[RestaurantContext],
    order_id: str
) -> str:
    return f"Order {order_id} is currently being prepared."


@function_tool
def create_reservation(
    wrapper: RunContextWrapper[RestaurantContext],
    date: str,
    time: str,
    party_size: int
) -> str:
    return (
        f"Reservation created for {wrapper.context.name}: "
        f"{party_size} people on {date} at {time}."
    )


@function_tool
def update_reservation(
    wrapper: RunContextWrapper[RestaurantContext],
    reservation_id: str,
    new_date: str,
    new_time: str,
    new_party_size: int
) -> str:
    return (
        f"Reservation {reservation_id} updated to "
        f"{new_party_size} people on {new_date} at {new_time}."
    )


@function_tool
def cancel_reservation(
    wrapper: RunContextWrapper[RestaurantContext],
    reservation_id: str
) -> str:
    return f"Reservation {reservation_id} has been canceled."


@function_tool
def check_availability(
    wrapper: RunContextWrapper[RestaurantContext],
    date: str,
    time: str,
    party_size: int
) -> str:
    return (
        f"Availability checked for {party_size} people on {date} at {time}. "
        f"Tables are available."
    )


@function_tool
def get_menu_recommendations(
    wrapper: RunContextWrapper[RestaurantContext],
    preference: str = ""
) -> str:
    if preference:
        return f"Recommended menu items for '{preference}': Margherita Pizza, Carbonara Pasta."
    return "Recommended menu items: Margherita Pizza, Carbonara Pasta, Caesar Salad."


@function_tool
def get_dish_details(
    wrapper: RunContextWrapper[RestaurantContext],
    dish_name: str
) -> str:
    return f"{dish_name}: popular dish with balanced flavor, fresh ingredients, and medium portion size."