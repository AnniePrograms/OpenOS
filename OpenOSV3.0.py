#!/usr/bin/python3
from requests import *
from os import system

AppsDictionary = {}
AppsNameList = []
AppInterpretation = []

system('clear')
print('''\033[36;1m    ███████                                     ███████     █████████ 
  ███░░░░░███                                 ███░░░░░███  ███░░░░░███
 ███     ░░███ ████████   ██████  ████████   ███     ░░███░███    ░░░ 
░███      ░███░░███░░███ ███░░███░░███░░███ ░███      ░███░░█████████ 
░███      ░███ ░███ ░███░███████  ░███ ░███ ░███      ░███ ░░░░░░░░███
░░███     ███  ░███ ░███░███░░░   ░███ ░███ ░░███     ███  ███    ░███
 ░░░███████░   ░███████ ░░██████  ████ █████ ░░░███████░  ░░█████████ 
   ░░░░░░░     ░███░░░   ░░░░░░  ░░░░ ░░░░░    ░░░░░░░     ░░░░░░░░░  
               ░███                                                   
               █████                                                  
              ░░░░░                                                   
Developed by Annie\033[0m''')
try:
	print('\nChecking version status...')
	CloudRequestVersion = get('https://gist.githubusercontent.com/AnniePrograms/29c5e07f6be1694c70d5372627f77a01/raw/Version.txt')
	CloudRequestVersion.raise_for_status()
	if CloudRequestVersion.text.splitlines()[1] == 'n':
		print('\033[31mOpenOS closed for development purposes, sorry!\033[0m')
		input('\033[36;1mLoad Terminated -\033[0m ')
		exit()
except Exception as ErrorDetails1:
	print(f'\033[31;1mSomething went wrong checking the version!\n\nError details:\n{ErrorDetails1}\033[0m')
	input('\033[31;1mLoad Failed, submit an issue at https://github.com/AnniePrograms/OpenOS/ -\033[0m ')
	exit()
print('Success')
try:
	print('Installing apps...')
	CloudRequestAppsList = get('https://gist.githubusercontent.com/AnniePrograms/29c5e07f6be1694c70d5372627f77a01/raw/AppsList.txt')
	CloudRequestAppsList.raise_for_status()
	for AppItem in CloudRequestAppsList.text.splitlines():
		CloudRequestAppItem = get(AppItem)
		CloudRequestAppItem.raise_for_status()
		AppsDictionary[CloudRequestAppItem.text.splitlines()[0]] = '--nl'.join(CloudRequestAppItem.text.splitlines()[1:])
		AppsNameList.append(CloudRequestAppItem.text.splitlines()[0])
	localapps = open('localappdirlist.txt', 'r').readlines()
	for app in localapps:
		indapp = open(app.strip(),'r').readlines()
		AppsDictionary[indapp[0][0:]] = indapp[1:]
		AppsNameList.append(indapp[0][0:])
except Exception as ErrorDetails2:
	print(f'\033[31;1mSomething went wrong loading the apps!\n\nError Details:\n{ErrorDetails2}\033[0m')
	input('\033[36;1mLoad Failed, submit an issue at https://github.com/AnniePrograms/OpenOS/ -\033[0m ')
	exit()
print('Success')
input('\033[33;1mLoad complete -\033[0m ')
system('clear')

while True:
	print('\033[36;1mOpenOS Apps:\033[0m')
	for ItemIndex in range(len(AppsDictionary)):
		print(f'{ItemIndex + 1}. {AppsNameList[ItemIndex][1:]}')
	try:
		ItemInput = int(input('\033[32;1mChoose app (Index) >\033[0m '))
		system('clear')
		for CodeLine in ''.join(AppsDictionary[AppsNameList[ItemInput - 1]]).split('--nl'):
                	AppInterpretation.append(CodeLine)
		exec('\n'.join(AppInterpretation))
		AppInterpretation.clear()
		input('\033[33;1mApp closed -\033[0m ')
		system('clear')
	except (ValueError, IndexError) as ErrorDetails3:
		system('clear')
		print('Looks like you entered the wrong index, try again!\n')
