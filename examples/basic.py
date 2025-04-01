#!/usr/bin/env python
"""
Example demonstrating basic usage of the Pica client.
"""

import os
import sys
from pica_ai import PicaClient
from pica_ai.models import PicaClientOptions

def main():
    pica_secret = os.environ.get("PICA_SECRET")

    if not pica_secret:
        print("ERROR: PICA_SECRET environment variable must be set")
        sys.exit(1)

    pica = PicaClient(
        secret=pica_secret, 
        options=PicaClientOptions(
            authkit=True,
            connectors=["*"],
        )
    )

    connections = pica.get_connections()

    print("Available connections:", len(connections))

    actions = pica.get_available_actions("gmail")

    print("Available actions:", len(actions.data))

    system_prompt = pica.generate_system_prompt()
    
    print("System prompt first 100 characters:", system_prompt[:100], "...")

if __name__ == "__main__":
    main() 
