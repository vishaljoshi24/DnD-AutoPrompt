from __future__ import annotations

import argparse

from modules import AgentProfile, TwoAgentConversation, configure_lm

DEFAULT_SCENARIO = (
    "Charlie owns Wizard Tower Brewing Company and needs help with a rat infestation "
    "in the brewery basement. Alice and Bob are adventurers deciding how to proceed."
)

DEFAULT_TASK = (
    "You should discuss a strategy for clearing out the rat infestation"
)
    
DEFAULT_OPENING = "I think we should ask Charlie what he has seen before we go downstairs."

DEFAULT_INSTRUCTION = (
        'The instructions for how to play the role of a D&D player are as '
        'follows. This is a short scenario in which you '
        f'play the role of a character named {name}. This scenario '
        'is structured as a Dungeons & Dragons game. '
        'The goal is to be consistent, but creative. It is '
        'important to play the role of a Dungeons & Dragons player as '
        'accurately as possible, i.e., by responding in ways that you think '
        'it is likely a player would respond, and taking '
        'into account all information that you have. '
        'It is important that you collaborate with with the user who is the '
        'other player, on the task at hand.'
        'Always use first-person limited perspective.'

)


def build_demo_conversation() -> TwoAgentConversation:
    return TwoAgentConversation(
        agent_a=AgentProfile(
            name="Alice",
            character="Alice, a direct dwarf barbarian who prefers practical action.",
            instructions=DEFAULT_INSTRUCTION,
            inventory = [
                "One set of common clothes"",
                "Two daggers",
                "One axe",
                "50 feet of rope",
                "One tinderbox",
                "One torch",
            ],
        ),
        agent_b=AgentProfile(
            name="Bob",
            character="Bob, a cautious but curious wizard.",
            instructions=DEFAULT_INSTRUCTION,
            inventory = [
                "One Wizard's Staff",
                "One can of oil",
                "One tinderbox",
                "Thunderwave spell: You unleash a wave of thunderous energy.",
                "Command spell: You speak a one-word command to a creature you can see within range."
            ],
        ),
        scenario=DEFAULT_SCENARIO,
        task=DEFAULT_TASK
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run two DSPy D&D player agents in conversation.")
    parser.add_argument("--rounds", type=int, default=4, help="Number of generated turns after the opening.")
    parser.add_argument("--model", default="ollama_chat/qwen3:8b", help="DSPy model identifier.")
    parser.add_argument("--api-base", default="http://localhost:11434", help="Local model API base URL.")
    args = parser.parse_args()

    configure_lm(model=args.model, api_base=args.api_base)
    conversation = build_demo_conversation()
    for line in conversation.run(opening_message=DEFAULT_OPENING, rounds=args.rounds):
        print(line)


if __name__ == "__main__":
    main()
