#!/usr/bin/python3
from requests import *
from os import system

AppsDictionary = {}
AppsNameList = []
AppInterpretation = []

system('clear')
try:
	print('Checking version status via cloud...')
	CloudRequestVersion = get('https://gist.githubusercontent.com/AnniePrograms/29c5e07f6be1694c70d5372627f77a01/raw/Version.txt')
	CloudRequestVersion.raise_for_status()
	if CloudRequestVersion.text.splitlines()[1] == 'n':
		print('OpenOS closed for development purposes, sorry!')
		exit()
except Exception as ErrorDetails1:
	print(f'Something went wrong checking the version!\n\nError details:\n{ErrorDetails1}')
	exit()

try:
	print('Loading Apps via cloud...')
	CloudRequestAppsList = get('https://gist.githubusercontent.com/AnniePrograms/29c5e07f6be1694c70d5372627f77a01/raw/AppsList.txt')
	CloudRequestAppsList.raise_for_status()
	for AppItem in CloudRequestAppsList.text.splitlines():
		CloudRequestAppItem = get(AppItem)
		CloudRequestAppItem.raise_for_status()
		AppsDictionary[CloudRequestAppItem.text.splitlines()[0]] = CloudRequestAppItem.text.splitlines()[1:]
		AppsNameList.append(CloudRequestAppItem.text.splitlines()[0])
except Exception as ErrorDetails2:
	print(f'Something went wrong loading the apps!\n\nError Details:\n{ErrorDetails2}')
	exit()
system('clear')

while True:
	print('\033[36;1mOpenOS Apps:\033[0m')
	for ItemIndex in range(len(AppsDictionary)):
		print(f'{ItemIndex + 1}. {AppsNameList[ItemIndex][1:]}')
	try:
		ItemInput = int(input('Choose app (Index) > '))
		system('clear')
		for CodeLine in ''.join(AppsDictionary[AppsNameList[ItemInput - 1]]).split('--nl'):
                	AppInterpretation.append(CodeLine)
		exec('\n'.join(AppInterpretation))
		AppInterpretation.clear()
		input('\033[36;1mApp closed -\033[0m ')
		system('clear')
	except (TypeError, IndexError) as ErrorDetails3:
		system('clear')
		print('Looks like you entered the wrong index, try again!\n')
