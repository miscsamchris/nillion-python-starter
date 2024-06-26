import asyncio
import os
import sys
import pytest

from dotenv import load_dotenv
from config import (
    CONFIG_PROGRAM_NAME,
    CONFIG_PARTY_1
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from helpers.nillion_client_helper import create_nillion_client
from helpers.nillion_keypath_helper import getUserKeyFromFile, getNodeKeyFromFile

load_dotenv()

async def main():
    cluster_id = os.getenv("NILLION_CLUSTER_ID")
    client_alice = create_nillion_client(
        getUserKeyFromFile(CONFIG_PARTY_1["userkey_file"]), getNodeKeyFromFile(CONFIG_PARTY_1["nodekey_file"])
    )

    program_name = "my_first_program"
    
    # Note: check out the code for the full millionaires program in the programs folder
    program_mir_path=f"../../programs-compiled/{CONFIG_PROGRAM_NAME}.nada.bin"

    # Store millionaires program in the network
    print(f"Storing program in the network: {program_name}")
    await client_alice.store_program(
        cluster_id, program_name, program_mir_path
    )

    user_id_alice = client_alice.user_id
    program_id = f"{user_id_alice}/{program_name}"

    print(f"Alice stores Rock-Paper-Scissor program at program_id: {program_id}")
    print(f"Alice tells Bob and Charlie her user_id and the millionaires program_id")

    print("\n📋⬇️ Copy and run the following command to store Bob and Charlie's salaries in the network")
    print(f"\npython3 step_2.py --user_id_1 {user_id_alice} --program_id {program_id}")
    return [user_id_alice, program_id]

if __name__ == "__main__":
    asyncio.run(main())

@pytest.mark.asyncio
async def test_main():
    pass
