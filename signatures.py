import dspy

class PlayerRoleSignature(dspy.Signature):
    player_qualities: str = dspy.InputField(desc="The qualities or behaviour that an agent which plays Dungeons & Dragons should exhibit.")
    turn_data: str = dspy.InputField(desc="Examples of a player's turn in which they describe their actions or utter a dialogue, demonstrating desired qualities or behaviour.")
    player_instruction: str = dspy.OutputField(desc="A comprehensive instruction prompt for a Dungeons & Dragons Player agent on how to act in the game.")

class GameMasterRoleSignature(dspy.Signature):
    gm_qualities: str = dspy.InputField(desc="The qualities or behaviour that a Dungeons & Dragons Game Master should exhibit when directing a game.")
    gm_direction: str = dspy.InputField(desc="Examples of a Game Master's narrative direction in which they guide players' actions")
    gm_instruction: str = dspy.OutputField(desc="A comprehensive instruction prompt for a Dungeons & Dragons Game Master agent on how to act in the game.")
    
class ScenarioPremiseSignature(dspy.Signature):
    context: str = dspy.InputField(desc="A description of the Dungeons & Dragons scenario including the non-player characters involved")
    premise: str = dspy.OutputField(desc="A more concise description of context and task, highlighting the salient pieces of information.")

    



