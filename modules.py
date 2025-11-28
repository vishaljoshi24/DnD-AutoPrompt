import dspy
from signatures import PlayerRoleSignature, GameMasterRoleSignature, ScenarioPremiseSignature


class GeneratePlayerInstruction(dspy.Module):
    def __init__(self):
        super().__init__()
        self.player_instruction = dspy.ChainOfThought(PlayerRoleSignature)
    
    def forward(self, player_role: str, turn_data: str):
        return self.player_instruction(player_role, turn_data)

class GenerateGameMasterInstruction(dspy.Module):
    def __init__(self):
        super().__init__()
        self.gm_instruction = dspy.ChainOfThought(GameMasterRoleSignature)

    def forward(self, gm_qualities:str, gm_direction: str):
        return self.gm_instruction(gm_qualities, gm_direction)

class GeneratePremise(dspy.Module):
    def __init__(self):
        super().__init__()
        self.premise = dspy.ChainOfThought(ScenarioPremiseSignature)

    def forward(self, context:str):
        return self.premise(context)
