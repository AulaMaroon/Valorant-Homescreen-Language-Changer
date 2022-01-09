@echo off
start "" "H:\Github\Valorant Language Changer\VALORANT"

:check
tasklist /nh /fi "imagename eq VALORANT.exe" | findstr /i "VALORANT.exe" >nul && (goto copyfile)|| (echo Waiting For Valorant && goto check)

:copyfile
xcopy "H:\Github\Valorant Language Changer\Videos" "C:\Riot Games\VALORANT\live\ShooterGame\Content\Movies\Menu" /K /H /Y
xcopy "H:\Github\Valorant Language Changer\Paks" "C:\Riot Games\VALORANT\live\ShooterGame\Content\Paks" /K /H /Y

