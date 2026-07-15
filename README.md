# PENCIL MAYHEM — Web Prototype Playtest

**DRAW. FLICK. WRECK.**

Public M1.2 playtest for the 2D hand-drawn pencil-flick battle game.

Play: <https://soulfunny.github.io/pencil-mayhem-playtest/>

## Controls

1. In the default **1P VS CPU** mode, you control Blue and the computer controls Red.
2. Select any tank belonging to the current player.
3. Press near the tank and pull the pencil opposite the intended travel direction.
4. Pull a little for the minimum distance or pull farther for the maximum distance. The range preview shows the predicted travel distance.
5. Release to fire. Releasing before the minimum pull cancels the shot without spending the turn.
6. Press **H** or the **Hold** button to stay in place and pass the turn.
7. A stroke that crosses an enemy tank destroys it. Eliminate all three enemy tanks to win.

Use **M** or the mode button to switch between **1P VS CPU** and **2P LOCAL**. Use the in-game **Stable / Real / Naughty** presets to compare flick feel.

## Playtest scope

This is prototype `M1.2-20260715`. It tests the core 3-vs-3 pencil-flick movement, player-controlled minimum-to-maximum travel distance, hold-position turns, collision, win conditions and a deterministic local computer opponent. The CPU chooses from the same legal range and uses the same movement and hit resolver as the player; it does not call an external AI API. Final art, traps, destructible objects, Doodle Garage, roguelite progression and online multiplayer are not included.

The M1.2 build has no account system, analytics or online save. The repository intentionally contains only the static deployment bundle and deployment checks; development source and design documents are not published here.

Feedback: <https://github.com/Soulfunny/pencil-mayhem-playtest/issues>

© 2026 Soulfunny. All rights reserved. No license is granted for reuse or redistribution.
