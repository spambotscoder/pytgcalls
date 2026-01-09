from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION_STRING")

app = Client(
    "mic-userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

vc = PyTgCalls(app)

@app.on_message(filters.command("joinvc", prefixes="."))
async def joinvc(_, msg):
    await vc.join_group_call(
        msg.chat.id,
        AudioPiped(
            "mic",
            ffmpeg_parameters="-af volume=1.8"
        )
    )
    await msg.reply("🎤 Mic VC joined (Boost ON)")

@app.on_message(filters.command("leavevc", prefixes="."))
async def leavevc(_, msg):
    await vc.leave_group_call(msg.chat.id)
    await msg.reply("❌ VC left")

app.start()
vc.start()
idle()
