from agents import Agent
from models import RestaurantContext

from my_agents.triage_agent import dynamic_triage_agent_instructions
from my_agents.order_agent import dynamic_order_agent_instructions
from my_agents.reservation_agent import dynamic_reservation_agent_instructions
from my_agents.menu_agent import dynamic_menu_agent_instructions

# tools 예시
from tools import (
    place_order,
    modify_order,
    cancel_order,
    check_order_status,
    create_reservation,
    update_reservation,
    cancel_reservation,
    check_availability,
    get_menu_recommendations,
    get_dish_details,
)

triage_agent = Agent[RestaurantContext](
    name="Triage Agent",
    instructions=dynamic_triage_agent_instructions,
    handoff_description="Routes the user to the correct restaurant support specialist.",
)

order_agent = Agent[RestaurantContext](
    name="Order Agent",
    instructions=dynamic_order_agent_instructions,
    tools=[
        place_order,
        modify_order,
        cancel_order,
        check_order_status,
    ],
    handoff_description="Handles food ordering, order changes, and order questions.",
)

reservation_agent = Agent[RestaurantContext](
    name="Reservation Agent",
    instructions=dynamic_reservation_agent_instructions,
    tools=[
        create_reservation,
        update_reservation,
        cancel_reservation,
        check_availability,
    ],
    handoff_description="Handles table booking, reservation changes, and cancellations.",
)

menu_agent = Agent[RestaurantContext](
    name="Menu Agent",
    instructions=dynamic_menu_agent_instructions,
    tools=[
        get_menu_recommendations,
        get_dish_details,
    ],
    handoff_description="Handles menu recommendations, ingredients, and dish explanations.",
)

# handoff 연결
triage_agent.handoffs = [order_agent, reservation_agent, menu_agent]

order_agent.handoffs = [triage_agent, reservation_agent, menu_agent]
reservation_agent.handoffs = [triage_agent, order_agent, menu_agent]
menu_agent.handoffs = [triage_agent, order_agent, reservation_agent]