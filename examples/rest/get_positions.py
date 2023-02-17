# python -c "import examples.rest.get_positions"

import os
import time

from bfxapi.client import Client, REST_HOST

bfx = Client(
    REST_HOST=REST_HOST,
    API_KEY=os.getenv("BFX_API_KEY"),
    API_SECRET=os.getenv("BFX_API_SECRET")
)

now = int(round(time.time() * 1000))

positions_snapshot = bfx.rest.auth.get_positions_snapshot(end=now, limit=50)
print(positions_snapshot)

positions_history = bfx.rest.auth.get_positions_history(end=now, limit=50)
print(positions_history)

positions_audit = bfx.rest.auth.get_positions_audit(end=now, limit=50)
print(positions_audit)