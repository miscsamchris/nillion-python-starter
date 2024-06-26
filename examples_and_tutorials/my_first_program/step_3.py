import argparse
import asyncio
import py_nillion_client as nillion
import os
import sys
import pytest
import importlib

from dotenv import load_dotenv

from config import (
    CONFIG_PARTY_1,CONFIG_PARTY_2
)

store_secret_party_1 = importlib.import_module("step_1")
store_secret_party_n = importlib.import_module("step_2")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from helpers.nillion_client_helper import create_nillion_client
from helpers.nillion_keypath_helper import getUserKeyFromFile, getNodeKeyFromFile

load_dotenv()

async def main(args = None):
    parser = argparse.ArgumentParser(
        description="Create a secret on the Nillion network with set read/retrieve permissions"
    )

    parser.add_argument(
        "--program_id",
        required=True,
        type=str,
        help="Program ID of the millionaires program",
    )

    parser.add_argument(
        "--party_ids_to_store_ids",
        required=True,
        nargs='+',
        type=str,
        help="List of partyid:storeid pairs of the secrets, with each pair separated by a space",
    )


    args = parser.parse_args(args)

    cluster_id = os.getenv("NILLION_CLUSTER_ID")

    # Alice initializes a client
    client_alice = create_nillion_client(
        getUserKeyFromFile(CONFIG_PARTY_1["userkey_file"]), 
        getNodeKeyFromFile(CONFIG_PARTY_1["nodekey_alternate_file"])
    )
    party_id_alice = client_alice.party_id

    # Create computation bindings for millionaires program
    compute_bindings = nillion.ProgramBindings(args.program_id)

    # Add Alice as an input party
    compute_bindings.add_input_party(CONFIG_PARTY_1["party_name"], party_id_alice)

    # Add an output party (Alice). 
    # The output party reads the result of the blind computation
    compute_bindings.add_output_party(CONFIG_PARTY_1["party_name"], party_id_alice)

    print(f"Computing using program {args.program_id}")

    # Also add Bob as input parties
    party_ids_to_store_ids = {}
    i=0
    for pair in args.party_ids_to_store_ids:
        party_id, store_id = pair.split(':')
        party_name = CONFIG_PARTY_2['party_name']
        compute_bindings.add_input_party(party_name, party_id)
        party_ids_to_store_ids[party_id] = store_id
        i=i+1
    print("Rock... Paper ... Scissors :")
    #Thanks ChatGPT. XD
    print("1 = Rock")
    print("    _______")
    print("---'   ____)")
    print("      (_____)")
    print("      (_____)")
    print("      (____)")
    print("---.__(___)")
    print()
    print("2 = Paper")
    print("     _______")
    print("---'    ____)____")
    print("           ______)")
    print("          _______)")
    print("         _______)")
    print("---.__________)")
    print()
    print("3 = Scissors")
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("       __________)")
    print("      (____)")
    print("---.__(___)")
    print()
    choice = input("Enter the number corresponding to your choice: ")
    # Add any computation time secrets
    # Alice provides her salary at compute time
    party_name_alice = CONFIG_PARTY_1["party_name"]
    compute_time_secrets = nillion.Secrets({
        "choice_1": nillion.SecretInteger(int(choice)),
        "Rock": nillion.SecretInteger(1),
        "Paper": nillion.SecretInteger(2),
        "Scissor": nillion.SecretInteger(3),
    })

    # Compute on the secret with all store ids. Note that there are no compute time secrets or public variables
    compute_id = await client_alice.compute(
        cluster_id,
        compute_bindings,
        list(party_ids_to_store_ids.values()), # Bob and Charlie's stored secrets
        compute_time_secrets, # Alice's computation time secret
        nillion.PublicVariables({}),
    )

    # Print compute result
    print(f"The computation was sent to the network. compute_id: {compute_id}")
    while True:
        compute_event = await client_alice.next_compute_event()
        if isinstance(compute_event, nillion.ComputeFinishedEvent):
            print(f"✅  Compute complete for compute_id {compute_event.uuid}")
            print(f"🖥️  The output result is {compute_event.result.value}")

            # The compute result is an index
            # Map it to the corresponding party name who should pay for lunch
            # ['Alice', 'Bob', 'Charlie']
            result=compute_event.result.value["Result"]
            winner="No One"
            if result==404:
                print(f"Error with the choices")
            elif result==0:
                print(f"Tie!!! No winner")
            else:
                winner= "Alice" if result==100 else "Bob"
                print(f"The Winner is {winner}")
            return winner
    
if __name__ == "__main__":
    asyncio.run(main())

