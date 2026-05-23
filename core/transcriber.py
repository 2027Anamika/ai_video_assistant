import os
import requests
from pydub import AudioSegment

# Sarvam sync API accepts max ~30s audio.
# We split into 25s pieces for safety.
SARVAM_PIECE_SECONDS = 25

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

SARVAM_STT_TRANSLATE_URL = (
    "https://api.sarvam.ai/speech-to-text-translate"
)

SARVAM_MODEL = os.getenv(
    "SARVAM_STT_MODEL",
    "saaras:v2.5"
)


def _send_to_sarvam(piece_path: str) -> str:
    """
    Send one audio piece to Sarvam API
    and return transcript text.
    """

    headers = {
        "api-subscription-key": SARVAM_API_KEY
    }

    with open(piece_path, "rb") as f:

        files = {
            "file": (
                os.path.basename(piece_path),
                f,
                "audio/wav"
            )
        }

        data = {
            "model": SARVAM_MODEL,
            "with_diarization": "false"
        }

        response = requests.post(
            SARVAM_STT_TRANSLATE_URL,
            headers=headers,
            files=files,
            data=data,
            timeout=120,
        )

    if not response.ok:

        print(f"\n❌ Sarvam returned {response.status_code}")
        print(f"Response body: {response.text}\n")

        response.raise_for_status()

    return response.json().get("transcript", "")


def transcribe_chunk(chunk_path: str) -> str:
    """
    Split chunk into smaller pieces
    and transcribe using Sarvam API.
    """

    if not SARVAM_API_KEY:
        raise RuntimeError(
            "SARVAM_API_KEY is not set"
        )

    audio = AudioSegment.from_wav(chunk_path)

    piece_ms = SARVAM_PIECE_SECONDS * 1000

    full_text = ""

    total_pieces = (
        (len(audio) + piece_ms - 1)
        // piece_ms
    )

    for i, start in enumerate(
        range(0, len(audio), piece_ms)
    ):

        piece = audio[start:start + piece_ms]

        piece_path = (
            f"{chunk_path}_sv_{i}.wav"
        )

        piece.export(
            piece_path,
            format="wav"
        )

        try:

            print(
                f"→ Sarvam piece "
                f"{i + 1}/{total_pieces}"
            )

            full_text += (
                _send_to_sarvam(piece_path)
                + " "
            )

        finally:

            if os.path.exists(piece_path):
                os.remove(piece_path)

    return full_text.strip()


def transcribe_all(chunks: list) -> str:
    """
    Transcribe all audio chunks.
    """

    full_transcript = ""

    print(
        "Using Sarvam AI for transcription."
    )

    for i, chunk in enumerate(chunks):

        print(
            f"Transcribing chunk "
            f"{i + 1}/{len(chunks)}..."
        )

        text = transcribe_chunk(chunk)

        full_transcript += text + " "

    print("Transcription complete.")

    return full_transcript.strip()