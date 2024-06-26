from nada_dsl import *

def nada_main():
    party1 = Party(name="Alice")
    party2 = Party(name="Bob")
    choice_1 = SecretInteger(Input(name="choice_1", party=party1))
    Rock = SecretInteger(Input(name="Rock", party=party1))
    Paper = SecretInteger(Input(name="Paper", party=party1))
    Scissor = SecretInteger(Input(name="Scissor", party=party1))
    choice_2 = SecretInteger(Input(name="choice_2", party=party2))
    tie_condition=choice_1.public_equals(choice_2)
    rock_1_condition=choice_1.public_equals(Rock)
    scissor_2_condition=choice_2.public_equals(Scissor)
    paper_1_condition=choice_1.public_equals(Paper)
    rock_2_condition=choice_2.public_equals(Rock)
    scissor_1_condition=choice_1.public_equals(Scissor)
    paper_2_condition=choice_2.public_equals(Paper)
    # result=tie_condition.if_else(SecretBlob(bytearray("It's a Tie","utf-8")),SecretBlob(bytearray("Not a Tie","utf-8")))
    result=tie_condition.if_else(Integer(0),
      rock_1_condition.if_else(
        scissor_2_condition.if_else(
          Integer(100),Integer(200)
        ),
        paper_1_condition.if_else(
          rock_2_condition.if_else(
            Integer(100),Integer(200)
          ),
          scissor_1_condition.if_else(
            paper_2_condition.if_else(
              Integer(100),Integer(200)
            ),Integer(404)
          )
        )
      )
    )
    return [Output(result, "Result", party1)]