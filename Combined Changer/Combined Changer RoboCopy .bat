@echo off
start "" "H:\Github\Valorant Language Changer\VALORANT"

:check
tasklist /nh /fi "imagename eq VALORANT.exe" | findstr /i "VALORANT.exe" >nul && (goto copyfile)|| (echo Waiting For Valorant && goto check)

:copyfile
robocopy "H:\Github\Valorant Language Changer\Videos" "C:\Riot Games\VALORANT\live\ShooterGame\Content\Movies\Menu" /z /nc /ns /nfl /ndl /np
robocopy "H:\Github\Valorant Language Changer\Paks" "C:\Riot Games\VALORANT\live\ShooterGame\Content\Paks" /z /nc /ns /nfl /ndl /np

