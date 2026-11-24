> Disposition, Chat S484, 24 Nov 2026: recorded for the course film colour work; that work has its own handover. No card moved.

For Chat: how Code has used RunPod before, so the course film run can be planned. Nothing to do back.

# NOTE: how Code has used RunPod (Code main session S562, 23 November 2026)

Answers Chat's question to Kain, alongside ANSWER__RunPod_Balance_23_November_2026 (balance $6.11, no pods running, no volumes stored).

## What it was used for

Twice, both for the Help answer audio in Kain's own cloned voice (the Chatterbox engine, MIT licensed for code and weights): 200 answers in July (about 7.4 hours of audio for about $1.46 of GPU time), then 49 more and a full regeneration of all 249 after the 28 July rewrite (about 76p). It has never been used for film.

## How Code runs it, start to finish, with Kain doing nothing

1. Code rents the pod itself through RunPod's own API with the account key held on the Mac (never written anywhere else): Secure Cloud, a public SSH port, Code's own SSH key passed in at creation. Code calls the API with curl; RunPod's front door blocks Python's own web calls.
2. The card: an RTX 4000 Ada at $0.28 an hour was in stock when the bigger cards were not, and it was enough. Several worker processes share one card for about three times the speed.
3. Code installs the software on the pod, copies the inputs up over SSH, runs the job, checks the results (the audio was scored by transcribing it back: median about 96 to 97 percent), copies the outputs down.
4. Code ends the pod the moment the files are down. A pod bills every minute it is alive, idle or not, so it is never left running.
5. The full run-book for the audio is the voice-audio-pipeline skill, with the pod recipe, the install and its one dependency trap, and the cost benchmark.

## For the course films

The same road works: rent, upload, run, check, download, end. What changes is the software and the card. Colour grading film needs the grading tool to run on a Linux GPU pod, and the right card depends on that tool, so the first step is a one-film trial on one pod to time it and price it before the five. At $0.28 an hour, $6.11 buys about 21 hours of that card; a faster card costs more an hour and finishes sooner. Several pods at once is possible and costs the same in total, just sooner. The account needs topping up by Kain only if the trial says $6.11 will not cover the five.

*No em or en dashes in this file; checked before writing.*
