Features and Changes:
- Player and Tree are now subclasses of Entity
- Added class for Text messages
- Added pause button
- Fixed some bugs
- Logs last error message before crashing

Fixed Bugs:
- Fixed a bug where objects moved horizontally with the player
- Fixed a bug where the swapped player model only updated when player moved
- Fixed a bug where the player spawned to a random location


Present Issues:
- Formatting causes tree and player to jump over a vertical row when moving to same row
- Pause message shifts everything above it upwards
- Going too far above the frame causes the player model to be printed repeatedly in the same column
- Full screen causes lots of flickering
- Entities consisting of multiple rows don't work correctly
- Crashes if player moves outside the left/right/top border
- Exiting the area through the left side sometimes causes the player to teleport to other side

