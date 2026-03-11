from agents import Agent, RunContextWrapper, Runner
from models import RestaurantContext, InputGuardrailOutput, OutputGuardrailOutput


def input_guardrail_instructions(
    wrapper: RunContextWrapper[RestaurantContext],
    agent: Agent[RestaurantContext],
):
    return """
You are a safety and relevance classifier for a restaurant support chatbot.

Your job:
1. Detect whether the user's message is inappropriate.
2. Detect whether the user's message is off-topic for a restaurant support system.

Mark is_blocked = true if the message contains:
- threats
- hate speech
- severe harassment
- sexual misconduct
- illegal violent intent
- extremely abusive content

Mark is_off_topic = true if the message is unrelated to:
- food ordering
- reservations
- menu questions
- restaurant complaints
- customer support for restaurant services

Be conservative and precise.
Return structured output only.
"""


input_guardrail_agent = Agent[RestaurantContext](
    name="Input Guardrail Agent",
    instructions=input_guardrail_instructions,
    output_type=InputGuardrailOutput,
)


def output_guardrail_instructions(
    wrapper: RunContextWrapper[RestaurantContext],
    agent: Agent[RestaurantContext],
):
    return """
You are a safety reviewer for assistant responses in a restaurant support chatbot.

Your job:
Check whether the assistant's response is inappropriate.

Block responses that are:
- rude, insulting, mocking, or hostile
- hateful or discriminatory
- sexually inappropriate
- encouraging violence or wrongdoing
- clearly off-domain in a restaurant support conversation
- exposing unsafe, harmful, or policy-violating content

Allow responses that are:
- polite
- empathetic
- professional
- relevant to restaurant ordering, reservations, menu help, and complaint handling

Return structured output only.
"""


output_guardrail_agent = Agent[RestaurantContext](
    name="Output Guardrail Agent",
    instructions=output_guardrail_instructions,
    output_type=OutputGuardrailOutput,
)


def run_input_guardrail_sync(
    context: RestaurantContext,
    user_input: str,
) -> InputGuardrailOutput:
    result = Runner.run_sync(
        input_guardrail_agent,
        user_input,
        context=context,
    )
    return result.final_output


def run_output_guardrail_sync(
    context: RestaurantContext,
    assistant_output: str,
) -> OutputGuardrailOutput:
    result = Runner.run_sync(
        output_guardrail_agent,
        assistant_output,
        context=context,
    )
    return result.final_output