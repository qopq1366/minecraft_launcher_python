import minecraft_launcher_lib
import subprocess

versions = input('Enter Minecraft versions: ')
username = input('Enter Username: ')

minecraft_launcher_lib.install.install_minecraft_version(versionid=versions, minecraft_directory='.minecraftversions')


options = {
    'username': username,
    "uuid": '',
    "token": ''
}

subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=versions, minecraft_directory='.minecraftversions', options=options))
