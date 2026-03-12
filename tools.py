from agents import function_tool, RunContextWrapper
from models import RestaurantContext


def estimate_price(item_name: str) -> str:
    """
    Return a deterministic estimated price range based on the item name.
    This is not a real database price. It is only a generated estimate.
    """
    name = item_name.lower().strip()

    # Category-based baseline pricing
    if any(word in name for word in ["steak", "ribeye", "sirloin", "t-bone"]):
        return "$28"
    elif any(word in name for word in ["lobster", "salmon", "tuna", "sashimi", "seafood platter"]):
        return "$22"
    elif any(word in name for word in ["pizza", "pasta", "risotto", "burger", "ramen", "pho", "noodle"]):
        return "$12"
    elif any(word in name for word in ["salad", "soup", "dumpling", "appetizer", "fries", "side"]):
        return "$6"
    elif any(word in name for word in ["cake", "dessert", "ice cream", "tiramisu", "cookie"]):
        return "$5"
    elif any(word in name for word in ["coffee", "latte", "tea", "juice", "soda", "drink"]):
        return "$3"
    elif any(word in name for word in ["set", "course", "combo", "platter"]):
        return "$18"

    # Fallback pseudo-estimate
    base = 8 + (sum(ord(c) for c in name) % 18)
    high = base + 6
    return f"${base}-${high}"


@function_tool
def place_order(
    wrapper: RunContextWrapper[RestaurantContext],
    item_name: str,
    quantity: int,
    special_request: str = ""
) -> str:
    estimated_price = estimate_price(item_name)
    return (
        f"Order placed for {wrapper.context.name}: "
        f"{quantity} x {item_name}. "
        f"Estimated price per item: {estimated_price}. "
        f"Special request: {special_request or 'None'}."
    )


@function_tool
def modify_order(
    wrapper: RunContextWrapper[RestaurantContext],
    order_id: str,
    updated_item: str
) -> str:
    estimated_price = estimate_price(updated_item)
    return (
        f"Order {order_id} has been updated to: {updated_item}. "
        f"Estimated price: {estimated_price}."
    )


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
        items = ["Margherita Pizza", "Carbonara Pasta", f"{preference.title()} Special"]
    else:
        items = ["Margherita Pizza", "Carbonara Pasta", "Caesar Salad"]

    formatted = []
    for item in items:
        formatted.append(f"{item} (estimated price: {estimate_price(item)})")

    if preference:
        return f"Recommended menu items for '{preference}': " + ", ".join(formatted) + "."
    return "Recommended menu items: " + ", ".join(formatted) + "."


@function_tool
def get_dish_details(
    wrapper: RunContextWrapper[RestaurantContext],
    dish_name: str
) -> str:
    estimated_price = estimate_price(dish_name)
    return (
        f"{dish_name}: popular dish with balanced flavor, fresh ingredients, "
        f"and medium portion size. Estimated price: {estimated_price}."
    )